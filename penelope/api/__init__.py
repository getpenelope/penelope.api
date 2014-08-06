from collections import OrderedDict
from datetime import datetime, date
from pyramid.config import Configurator
from pyramid.renderers import JSON
from sqlalchemy import engine_from_config
from sqlalchemy import inspect
from sqlalchemy.ext import hybrid
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
from penelope.models import Base, BasePenelopeModel


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


def datetime_adapter(obj, request):
    return obj.isoformat()


def sqlalchemy_adapter(obj, request):
    result = OrderedDict()
    for desc in inspect(obj.__class__).all_orm_descriptors:
        if isinstance(desc, InstrumentedAttribute):
            if hasattr(desc.property, 'target'): # probably a relation
                continue
            key = desc.property.key
        elif desc.extension_type is hybrid.HYBRID_PROPERTY:
            key = desc.__name__
        else:
            continue
        result[key] = getattr(obj, key)
    return result


def main(global_config, **settings):
    config = Configurator(settings=settings)
    json_renderer = JSON()

    json_renderer.add_adapter(datetime, datetime_adapter)
    json_renderer.add_adapter(date, datetime_adapter)
    json_renderer.add_adapter(BasePenelopeModel, sqlalchemy_adapter)

    config.add_renderer('simplejson', json_renderer)

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config.include("cornice")
    config.scan("penelope.api.views")
    return config.make_wsgi_app()

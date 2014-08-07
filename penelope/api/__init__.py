import os
from eve import Eve
from eve.auth import TokenAuth
from eve.io.sql import SQL as SQLAlchemy

from penelope.models import Base


class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        if token == 'redturtle':
            return True
        else:
            return False


def run():
    DIR = os.path.dirname(__file__)
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', '5000'))
    app = Eve(data=SQLAlchemy, auth=TokenAuth, settings='{0}/settings.py'.format(DIR))
    db = app.data.driver
    Base.metadata.bind = db.engine
    db.Model = Base
    db.create_all()
    app.run(host=host, port=port, use_reloader=False)

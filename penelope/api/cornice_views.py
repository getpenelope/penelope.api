""" Cornice services.
"""
import json

from webob import Response, exc
from cornice import Service

from penelope.models import User, Project
from penelope.api import DBSession


users = Service(name='users', path='/users', description="Users")
projects = Service(name='projects', path='/projects', description="Projects")


class _401(exc.HTTPError):
    def __init__(self, msg='Unauthorized'):
        body = {'status': 401, 'message': msg}
        Response.__init__(self, json.dumps(body))
        self.status = 401
        self.content_type = 'application/json'


@users.get()
def get_users(request):
    session = DBSession()
    return session.query(User).all()


@projects.get()
def get_projects(request):
    session = DBSession()
    return session.query(Project).all()

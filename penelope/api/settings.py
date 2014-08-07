import os
from eve.io.sql.decorators import registerSchema
from penelope.models import User

DEBUG = bool(int(os.environ.get('EVE_DEBUG', '0')))
SERVER_NAME = os.environ.get('SERVER_NAME')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#SQLALCHEMY_ECHO = True
API_VERSION = 'v1'
IF_MATCH = False
BANDWIDTH_SAVER = False

registerSchema('users')(User)
User._eve_schema['users']['resource_methods'] = ['GET', 'POST']
User._eve_schema['users']['item_methods'] = ['GET', 'PATCH']


DOMAIN = {
    'users': User._eve_schema['users'],
}

"""PytSite Auth Google Plugin API
"""
from typing import Union as _Union, List as _List
from oauth2client import client as _oauth2_client
from googleapiclient.discovery import build as _google_discovery_build
from pytsite import settings as _settings, router as _router, auth as _auth
from . import _error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get_client_id():
    """Get client ID from settings
    """
    client_id = _settings.get('google.client_id')
    if not client_id:
        raise _error.ClientIdNotDefined()

    return client_id


def get_client_secret():
    """Get client secret from settings
    """
    client_secret = _settings.get('google.client_secret')
    if not client_secret:
        raise _error.ClientSecretNotDefined()

    return client_secret


def create_oauth2_flow(scope: _Union[str, _List[str]] = None, redirect_uri: str = None, client_id: str = None,
                       client_secret: str = None, **kwargs):
    """Create OAuth2 web server flow
    """
    flow = _oauth2_client.OAuth2WebServerFlow(client_id or get_client_id(), client_secret or get_client_secret(),
                                              scope or '', redirect_uri or _router.current_url(), **kwargs)
    flow.params['access_type'] = 'offline'

    return flow


def get_authorization_url(scope: _Union[str, _List[str]] = None):
    """Get URL of the PytSite's location which start process of requesting user authorization
    """
    rule_args = {}

    if isinstance(scope, list):
        rule_args['scope'] = ','.join(scope)
    elif isinstance(scope, str):
        rule_args['scope'] = scope

    return _router.rule_url('google@authorization', rule_args)


def get_user_credentials(user: _auth.model.AbstractUser) -> _oauth2_client.OAuth2Credentials:
    """Get user's Google credentials
    """
    if 'google_oauth2_credentials' not in user.options:
        raise _error.UserCredentialsNotFound(user)

    return _oauth2_client.OAuth2Credentials.from_json(user.get_option('google_oauth2_credentials'))


def build_service_resource(name: str, version: str, user: _auth.model.AbstractUser = None):
    """Build service resource object
    """
    return _google_discovery_build(name, version, credentials=get_user_credentials(user) if user else None)

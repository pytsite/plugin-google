"""PytSite Google Plugin Init
"""
from . import _error as error
from ._api import get_client_id, get_client_secret, create_oauth2_flow, get_authorization_url, get_user_credentials, \
    build_service_resource

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, permissions, settings, router, assetman
    from . import _settings_form, _eh, _controllers

    # Language resources
    lang.register_package(__name__, alias='google')
    lang.register_global('google_admin_settings_url', lambda language, args: settings.form_url('google'))

    # Assets
    assetman.register_package(__name__, alias='google')
    assetman.t_js(__name__ + '@**')
    assetman.js_module('pytsite-google', __name__ + '@js/google')

    # Permissions
    permissions.define_permission('google.settings.manage', 'google@manage_google_settings', 'app')

    # Settings
    settings.define('google', _settings_form.Form, 'google@google', 'fa fa-google', 'google.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)

    # Routes
    router.handle(_controllers.Authorization(), '/google/authorization', 'google@authorization',
                  filters='pytsite.auth_web@authorize')


_init()

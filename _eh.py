"""PytSite Auth Google Plugin Event Handlers
"""
from pytsite import settings as _settings, auth as _auth, lang as _lang, router as _router, metatag as _metatag

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """pytsite.router.dispatch
    """
    c_user = _auth.get_current_user()
    if not (_settings.get('google.client_id') and _settings.get('google.client_secret')) \
            and c_user.has_permission('google.settings.manage'):
        _router.session().add_warning_message(_lang.t('google@plugin_setup_required_warning'))

    if _settings.get('google.client_id'):
        _metatag.t_set('pytsite-google-client-id', _settings.get('google.client_id'))

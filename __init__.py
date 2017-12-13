"""PytSite Google Plugin Init
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from plugins import assetman

    # Assets
    assetman.register_package(__name__)
    assetman.t_js(__name__)
    assetman.js_module('pytsite-google', __name__ + '@js/google')

"""PytSite Google Plugin Init
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import assetman

    # Assets
    assetman.register_package(__name__, alias='google')
    assetman.t_js(__name__ + '@**')
    assetman.js_module('pytsite-google', __name__ + '@js/google')


_init()

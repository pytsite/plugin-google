define(['jquery', 'assetman'], function ($, assetman) {
    var ready = false;

    return {
        getClientId: function () {
            var meta = $('meta[name=pytsite-google-client-id]');
            if (meta.length)
                return meta[0];
        },

        ready: function (func) {
            if (ready) {
                func(window.gapi);
            }
            else {
                window.onGAPILoad = function () {
                    ready = true;
                    func(window.gapi);
                };

                assetman.loadJS('https://apis.google.com/js/platform.js?onload=onGAPILoad');
            }
        }
    }
});

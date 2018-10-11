const assetman = require('@pytsite/assetman');

let isReady = false;

function ready(func) {
    if (isReady) {
        func(window.gapi);
    }
    else {
        window.onGAPILoad = function () {
            isReady = true;
            func(window.gapi);
        };

        assetman.loadJS('https://apis.google.com/js/platform.js?onload=onGAPILoad');
    }
}

export {ready}

var odoo = odoo || {};
var _ = _ || {};

odoo.define('gpsi.webclient', function(require) {
    var WebClient = require('web.WebClient');
    WebClient.include({
        init: function(parent, client_options) {
            this._super(parent, client_options);
            this.set('title_part', {"zopenerp": "GlobalSTD"});
        },
    });
});

/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
const { patch } = require("web.utils");

patch(
    WebClient.prototype,
    "brand_change_window_title/static/src/js/webclient.js",
    {
        setup() {
            this._super();
            this.title.setParts({ zopenerp: "Lomaq S.A." });
        },
    }
);

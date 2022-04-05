# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Change the Window Title",
    "summary": """
        This overwrites the window title to replace 'Odoo'. It's intended to be copied
        inside the client repository and customize the code.""",
    "author": "Federico Gregori",
    "maintainers": ["Federico Gregori"],
    "website": "https://fedegregori.dev/",
    "license": "AGPL-3",
    "category": "Web",
    "version": "15.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": ["web"],
    "data": [
        "views/webclient_templates.xml",
    ],
    "assets": {
        "web.assets_common": [
            "brand_change_window_title/static/src/js/webclient.js",
        ],
    },
}

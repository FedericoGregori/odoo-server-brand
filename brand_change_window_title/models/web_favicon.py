import hashlib

from odoo import models, fields, api, _


class WebFavicon(models.AbstractModel):
    _name = "web.favicon"
    _description = "Web favicon getter"

    @api.model
    def url_favicon(self, field, size=None):
        """Returns a local url that points to the image field of a given browse record."""
        record = self.env.company
        sudo_record = record.sudo()
        sha = hashlib.sha512(
            str(getattr(sudo_record, "__last_update")).encode("utf-8")
        ).hexdigest()[:7]
        size = "" if size is None else "/%s" % size
        return "/web/image/%s/%s/%s%s?unique=%s" % (
            record._name,
            record.id,
            field,
            size,
            sha,
        )

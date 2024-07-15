from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_booking = fields.Boolean(string='Is Booking', default=False)

    def write(self, vals):
        for record in self:
            if record.is_booking:
                vals['name'] = self.env['ir.sequence'].next_by_code('request.quotation') or _('New')
        return super(PurchaseOrder, self).write(vals)
from odoo import models, fields, api


class BookingOrderConfig(models.Model):
    _name = 'booking.order.config'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Booking Order Configuration'

    max_booking_order = fields.Float(string='Max Booking Order', compute='_compute_max_booking_order', store=True, tracking=True)
    qty_limit_percentage = fields.Float(string='Quantity Limit Percentage', tracking=True)
    product_id = fields.Many2one('product.template', 'product template')

    @api.depends('product_id', 'qty_limit_percentage')
    def _compute_max_booking_order(self):
        print('product on hand ini di klik')
        for record in self:
            stock_quant = self.env['stock.quant'].search([], limit=1)
            qty_on_hand = sum(stock_quant.mapped('inventory_quantity'))
            record.max_booking_order = qty_on_hand + (qty_on_hand * record.qty_limit_percentage / 100)
#             belum berhasil



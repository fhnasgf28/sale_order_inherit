from odoo import models, fields


class BookingOrderConfig(models.Model):
    _name = 'booking.order.config'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Booking Order Configuration'

    max_booking_order = fields.Float(string='Max Booking Order', store=True, tracking=True)
    qty_limit_percentage = fields.Float(string='Quantity Limit Percentage', tracking=True)
    product_template_id = fields.Many2one('product.template', 'product template')


# payment_controller.py

from odoo import http
from odoo.http import request
from odoo import fields
from dateutil.relativedelta import relativedelta


class PaymentController(http.Controller):

    @http.route('/payments', auth='user', website=True)
    def list_payments(self):
        if request.env.user.has_group('models.group_manager'):
            payments = request.env['models.payment'].search([('date', '>=', fields.Date.today() - relativedelta(days=7))])
        elif request.env.user.has_group('models.group_admin'):
            payments = request.env['models.payment'].search([])
        else:
            payments = None

        return request.render('views.payment_views', {'payments': payments})

    @http.route('/payments/<int:payment_id>', auth='user', website=True)
    def view_payment(self, payment_id):
        payment = request.env['models.payment'].browse(payment_id)
        return request.render('views.payment_details_views', {'payment': payment})

    @http.route('/payments/<int:payment_id>/edit', type='http', auth='user', website=True)
    def edit_payment(self, payment_id, **post):
        # Check user role
        if request.env.user.has_group('models.group_admin'):
            payment = request.env['models.payment'].browse(payment_id)
            # Update payment based on form data
            return http.request.redirect('/payments/%d' % payment_id)
        else:
            return http.request.redirect('/payments')

    @http.route('/payments/new', type='http', auth='user', website=True)
    def create_payment(self, **post):
        # Check user role
        if request.env.user.has_group('models.group_admin'):
            # Create new payment based on form data
            return http.request.redirect('/payments')
        else:
            return http.request.redirect('/payments')

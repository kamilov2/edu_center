from odoo import http
from odoo.http import request


class GroupController(http.Controller):

    @http.route('/groups', auth='user', website=True)
    def list_groups(self):
        groups = request.env['models.group'].search([])
        return request.render('views.groups_views', {'groups': groups})

    @http.route('/groups/<int:group_id>', auth='user', website=True)
    def view_group(self, group_id):
        group = request.env['models.group'].browse(group_id)
        return request.render('views.group_detail_views', {'group': group})

    @http.route('/groups/<int:group_id>/payments', auth='user', website=True)
    def view_group_payments(self, group_id):
        group = request.env['models.group'].browse(group_id)
        students = group.student_ids  # Assuming group has a One2many field 'student_ids' related to students
        payments = request.env['models.payment'].search([('student_id', 'in', students.ids)])
        return request.render('models.group_payments_views', {'group': group, 'payments': payments})

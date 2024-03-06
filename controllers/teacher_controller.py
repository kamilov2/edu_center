from odoo import http
from odoo.http import request


class TeacherController(http.Controller):

    @http.route('/teachers', auth='user', website=True)
    def list_teachers(self):
        teachers = request.env['models.teacher'].search([])
        return request.render('views.teacher_views', {'teachers': teachers})

    @http.route('/teachers/<int:teacher_id>', auth='user', website=True)
    def view_teacher(self, teacher_id):
        teacher = request.env['models.teacher'].browse(teacher_id)
        return request.render('models.teacher_detail_views', {'teacher': teacher})

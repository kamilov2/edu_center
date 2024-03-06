from odoo import http
from odoo.http import request


class StudentController(http.Controller):

    @http.route('/students', auth='user', website=True)
    def list_students(self):
        students = request.env['views.student'].search([])
        return request.render('views.student_views', {'students': students})

    @http.route('/students/<int:student_id>', auth='user', website=True)
    def view_student(self, student_id):
        student = request.env['views.student'].browse(student_id)
        return request.render('views.student_detail_views', {'student': student})

    @http.route('/students/<int:student_id>/payments', auth='user', website=True)
    def view_student_payments(self, student_id):
        student = request.env['views.student'].browse(student_id)
        payments = student.payment_ids  # Assuming student has a One2many field 'payment_ids' related to payments
        return request.render('views.student_payments_views', {'student': student, 'payments': payments})

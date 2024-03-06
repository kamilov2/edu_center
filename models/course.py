from odoo import fields, models

class Course(models.Model):
    _name = 'edu.course'
    _description = 'Курс'

    name = fields.Char(string='Название', required=True)
    description = fields.Text(string='Описание')
    teacher_ids = fields.Many2many('edu.teacher', string='Преподаватели')

    def create_course(self, vals):
        return self.create(vals)

    def update_course(self, vals):
        return self.write(vals)

    def delete_course(self):
        return self.unlink()

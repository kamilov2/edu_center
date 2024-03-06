from odoo import fields, models

class Group(models.Model):
    _name = 'edu.group'
    _description = 'Группа'

    name = fields.Char(string='Название', required=True)
    course_id = fields.Many2one('edu.course', string='Курс', required=True)
    teacher_id = fields.Many2one('edu.teacher', string='Преподаватель', required=True)
    student_ids = fields.Many2many('edu.student', string='Студенты')

    # Метод для создания группы
    def create_group(self, vals):
        # Создание записи о группе с переданными значениями
        return self.create(vals)

    # Метод для обновления группы
    def update_group(self, vals):
        # Обновление записи о группе с переданными значениями
        return self.write(vals)

    # Метод для удаления группы
    def delete_group(self):
        # Удаление записи о группе
        return self.unlink()

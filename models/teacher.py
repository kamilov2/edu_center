from odoo import fields, models

class Teacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Преподаватель'

    # Определение полей модели для хранения информации о преподавателе
    name = fields.Char(string='Имя', required=True)
    age = fields.Integer(string='Возраст')
    gender = fields.Selection([('male', 'Мужской'), ('female', 'Женский')], string='Пол')
    email = fields.Char(string='Email')
    courses_taught = fields.Many2many('edu.course', string='Преподаваемые курсы')

    # Метод для создания преподавателя
    def create_teacher(self, vals):
        # Создание записи о преподавателе с переданными значениями
        return self.create(vals)

    # Метод для обновления информации о преподавателе
    def update_teacher(self, vals):
        # Обновление записи о преподавателе с переданными значениями
        return self.write(vals)

    # Метод для удаления преподавателя
    def delete_teacher(self):
        # Удаление записи о преподавателе
        return self.unlink()

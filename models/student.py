from odoo import fields, models

class Student(models.Model):
    _name = 'edu.student'
    _description = 'Студент'

    # Определение полей модели для хранения информации о студенте
    name = fields.Char(string='Имя', required=True)
    age = fields.Integer(string='Возраст')
    gender = fields.Selection([('male', 'Мужской'), ('female', 'Женский')], string='Пол')
    email = fields.Char(string='Email')

    # Метод для создания студента
    def create_student(self, vals):
        # Создание записи о студенте с переданными значениями
        return self.create(vals)

    # Метод для обновления информации о студенте
    def update_student(self, vals):
        # Обновление записи о студенте с переданными значениями
        return self.write(vals)

    # Метод для удаления студента
    def delete_student(self):
        # Удаление записи о студенте
        return self.unlink()

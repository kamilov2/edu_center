from odoo import fields, models

class Payment(models.Model):
    _name = 'edu.payment'
    _description = 'Платеж'

    # Определение полей модели для хранения информации о платеже
    date = fields.Date(string='Дата', required=True)
    amount = fields.Float(string='Сумма', required=True)
    description = fields.Text(string='Описание')
    receipt = fields.Char(string='Чек')
    manager_id = fields.Many2one('edu.manager', string='Менеджер', required=True)
    student_id = fields.Many2one('edu.student', string='Студент', required=True)

    # Метод для создания платежа
    def create_payment(self, vals):
        # Создание записи о платеже с переданными значениями
        return self.create(vals)

    # Метод для обновления платежа
    def update_payment(self, vals):
        # Обновление записи о платеже с переданными значениями
        return self.write(vals)

    # Метод для удаления платежа
    def delete_payment(self):
        # Удаление записи о платеже
        return self.unlink()

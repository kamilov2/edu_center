{
    'name': 'Education Center Management',
    'version': '1.0',
    'summary': 'Manage payments, courses, students, and teachers in an education center.',
    'description': """
        This module automates the payment system for an education center, allowing management of payments, courses, students, and teachers. 
        It provides functionalities for administrators and managers to view and control payments, courses, and related data.
    """,
    'category': 'Education',
    'author': 'Your Name',
    'website': 'http://www.example.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/group_views.xml',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/payment_views.xml',
        'views/dashboard_views.xml',
        'views/course_form_view.xml',
        'views/student_form_view.xml',
        'views/teacher_form_view.xml',
        'views/group_form_view.xml',
        'views/payment_form_view.xml',
        'views/student_list_view.xml',
        'views/student_details_view.xml',
        'controllers/payment_controller.py',
        'views/payment_details_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

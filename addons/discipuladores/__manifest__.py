{
    'name': 'Discipuladores',
    'version': '1.0',
    'summary': 'Gestión de discipuladores',
    'description': 'Módulo para registrar y gestionar discipuladores vinculados a personas.',
    'author': 'Israel Vargas',
    'depends': ['base', 'personas'],
    'data': [
        'security/ir.model.access.csv',
        'views/discipulador_views.xml',
        'views/discipulador_menu.xml',
    ],
    'installable': True,
    'application': True,
}

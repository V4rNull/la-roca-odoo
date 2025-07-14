{
    'name': 'Familias',
    'version': '1.0',
    'summary': 'Gestión de familias en el ministerio La Roca',
    'description': 'Módulo para registrar familias y sus miembros con relaciones familiares.',
    'author': 'Israel Vargas',
    'category': 'La Roca',
    'depends': ['base', 'personas'],
    'data': [
        'security/ir.model.access.csv',
	'views/familia_menu.xml',
        'views/familia_views.xml',
    ],
    'installable': True,
    'application': True,
}


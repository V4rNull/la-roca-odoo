{
    'name': 'Confrontaciones',
    'version': '1.0',
    'category': 'La Roca',
    'summary': 'Gestión de Confrontaciones',
    'depends': ['base', 'personas'],
    'data': [
        'security/ir.model.access.csv',
        'views/confrontacion_views.xml',
        'views/confrontacion_menu.xml',
    ],
    'installable': True,
    'application': True,
}

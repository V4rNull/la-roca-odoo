{
    'name': 'Historial',
    'version': '1.0',
    'summary': 'Registro de historial de personas',
    'category': 'la_roca',
    'author': 'La Roca',
    'depends': ['base', 'personas'],
    'data': [
        'security/ir.model.access.csv',
        'views/historial_views.xml',
        'views/historial_menu.xml',
    ],
    'installable': True,
    'application': False,
}

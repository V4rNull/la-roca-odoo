{
    'name': 'Bitácora',
    'version': '1.0',
    'summary': 'Seguimiento y confrontación de personas',
    'author': 'La Roca',
    'depends': ['base', 'personas'],
    'data': [
        'security/ir.model.access.csv',
        'views/bitacora_views.xml',
        'views/bitacora_menu.xml',
    ],
    'installable': True,
    'application': True,
}

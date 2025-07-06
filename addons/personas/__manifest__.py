{
    'name': 'Personas',
    'version': '1.0',
    'summary': 'Gestión de personas en el ministerio La Roca',
    'description': 'Módulo para registrar miembros, discipuladores y relaciones.',
    'author': 'Israel Vargas',
    'category': 'La Roca',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/persona_views.xml',
    ],
    'installable': True,
    'application': True,
}


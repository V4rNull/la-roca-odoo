
{
    'name': 'Personas',
    'version': '1.0',
    'summary': 'Gestión de personas de la iglesia',
    'category': 'Custom',
    'author': 'Israel Vargas',
    'depends': ['base'],
    'data': [
	'security/groups.xml',
        'security/ir.model.access.csv',
        'views/persona_views.xml',
        'views/persona_menu.xml',
	'views/city_views.xml',
        'data/cities.xml',
    ],
    'installable': True,
    'application': True,
}

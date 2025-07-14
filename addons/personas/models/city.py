from odoo import models, fields

class City(models.Model):
    _name = 'la_roca.city'
    _description = 'Ciudad'

    name = fields.Char(string='Nombre', required=True)

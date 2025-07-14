from odoo import models, fields

class Familia(models.Model):
    _name = 'la_roca.familia'
    _description = 'Familia'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Familia', required=True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    pais = fields.Many2one('res.country', string='País') 
    miembros_ids = fields.One2many('la_roca.familia.miembro', 'familia_id', string='Miembros')

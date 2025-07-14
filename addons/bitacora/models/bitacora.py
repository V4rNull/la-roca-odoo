from odoo import models, fields

class Bitacora(models.Model):
    _name = 'la_roca.bitacora'
    _description = 'Bitácora'

    persona_id = fields.Many2one('la_roca.persona', string='Persona', required=True)
    tipo = fields.Selection([
        ('seguimiento', 'Seguimiento'),
        ('correccion', 'Corrección'),
        ('confrontacion', 'Confrontación'),
        ('avance', 'Avance'),
    ], string='Tipo', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha', default=fields.Date.today)
    responsable_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)

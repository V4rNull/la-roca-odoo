from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Confrontacion(models.Model):
    _name = 'la_roca.confrontacion'
    _description = 'Confrontación'

    persona_id = fields.Many2one('la_roca.persona', string='Persona', required=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.today, required=True)
    descripcion = fields.Text(string='Descripción')
    responsable_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)

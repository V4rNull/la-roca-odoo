from odoo import models, fields, api

class Historial(models.Model):
    _name = 'la_roca.historial'
    _description = 'Historial de Seguimiento'

    persona_id = fields.Many2one('la_roca.persona', string='Persona', required=True)
    descripcion = fields.Text(string='Descripción', required=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.today, required=True)
    responsable_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user, required=True)

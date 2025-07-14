from odoo import models, fields

class Discipulador(models.Model):
    _name = 'la_roca.discipulador'
    _description = 'Discipulador'
    _rec_name = 'persona_id'

    persona_id = fields.Many2one('la_roca.persona', string='Persona', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    activo = fields.Boolean(string='Activo', default=True)
    observaciones = fields.Text(string='Observaciones')

from odoo import models, fields

class FamiliaMiembro(models.Model):
    _name = 'la_roca.familia.miembro'
    _description = 'Miembro de Familia'

    persona_id = fields.Many2one('la_roca.persona', string='Persona', required=True)
    familia_id = fields.Many2one('la_roca.familia', string='Familia', required=True)
    parentesco = fields.Selection([
        ('conyuge', 'Cónyuge'),
        ('hijo', 'Hijo/a'),
        ('padre', 'Padre'),
        ('madre', 'Madre'),
        ('hermano', 'Hermano/a'),
        ('otro', 'Otro'),
    ], string='Parentesco', required=True)


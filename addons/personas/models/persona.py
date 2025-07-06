from odoo import models, fields, api
from datetime import date

class Persona(models.Model):
    _name = 'la_roca.persona'
    _description = 'Miembro de la Iglesia'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    edad = fields.Integer(string='Edad', compute='_compute_edad', store=True)
    ciudad = fields.Char(string='Ciudad')
    telefono = fields.Char(string='Teléfono')

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                hoy = date.today()
                record.edad = hoy.year - record.fecha_nacimiento.year - (
                    (hoy.month, hoy.day) < (record.fecha_nacimiento.month, record.fecha_nacimiento.day)
                )
            else:
                record.edad = 0


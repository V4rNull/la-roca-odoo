from odoo import models, fields, api

class Persona(models.Model):
    _name = 'la_roca.persona'
    _description = 'Persona'
    _rec_name = 'nombre_completo'

    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('nuevo', 'Nuevo'),
    ], string='Estado', default='activo', required=True)

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    edad = fields.Integer(string='Edad')
    telefono = fields.Char(string='Teléfono')
    city_id = fields.Many2one('la_roca.city', string='Ciudad')
    discipulador_id = fields.Many2one('la_roca.persona', string='Discipulador', ondelete='set null')
    ultimo_registro = fields.Date(string='Último Registro')

    crear_usuario = fields.Boolean(string="¿Crear usuario?")
    user_id = fields.Many2one('res.users', string='Usuario Vinculado', readonly=True)

    nombre_completo = fields.Char(string='Nombre Completo', compute='_compute_nombre_completo', store=True)

    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for rec in self:
            rec.nombre_completo = f"{rec.nombre or ''} {rec.apellido or ''}".strip()

    @api.model
    def create(self, vals):
        record = super().create(vals)
        if vals.get('crear_usuario'):
            usuario = self.env['res.users'].create({
                'name': record.nombre_completo,
                'login': f"{record.nombre.lower()}.{record.apellido.lower()}",
                'password': 'temporal123',
                'groups_id': [(6, 0, [
                    self.env.ref('personas.group_persona_miembro').id
                ])]
            })
            record.user_id = usuario.id
        return record

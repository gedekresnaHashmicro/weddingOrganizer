from odoo import api, fields, models


class Partner(models.Model):
    _name = 'wedding.partner'
    _description = 'Standard Class Partners'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='Telepon/HP')
    
    

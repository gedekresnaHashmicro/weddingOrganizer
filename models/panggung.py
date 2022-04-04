from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Panggung untuk wedding'

    name = fields.Char(string='Name', required=True)
    # pelaminan = fields.Char(string='Tipe Pelaminan')
    pelaminan_id = fields.Many2one(comodel_name='wedding.pelaminan', string='Tipe Pelaminan', required=True)
    # bunga = fields.Char(string='Tipe Bunga')
    bunga = fields.Selection(string='Tipe Bunga', selection=[('bunga mati', 'Bunga Mati'), ('bunga hidup', 'Bunga Hidup'),])
    accesories = fields.Char(string='Accessoris Pelaminan')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    kursipengantin_id = fields.Many2one(comodel_name='wedding.kursipengantin', string='Tipe Kursi Pengantin',required=True)
    
    
    @api.depends('pelaminan_id','kursipengantin_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan_id.harga + record.kursipengantin_id.harga

    stok = fields.Integer(string='Stok Paket Panggung')

    des_pelaminan = fields.Char(string='Dskripsi Pelaminan',compute='_compute_des_pelaminan')

    @api.depends('pelaminan_id')
    def _compute_des_pelaminan(self):
        for record in self:
            record.des_pelaminan = record.pelaminan_id.deskripsi

    des_kursipengantin = fields.Char(string='Deskripsi Kursi Pengantin',compute='_compute_des_kursipengantin')

    @api.depends('kursipengantin_id')
    def _compute_des_kursipengantin(self):
        for record in self:
            record.des_kursipengantin = record.kursipengantin_id.deskripsi
    
     
    
    
    
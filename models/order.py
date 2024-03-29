from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'wedding.order'
    _description = 'New Description'

    orderpanggungdetail_ids = fields.One2many(comodel_name='wedding.orderpanggungdetail', inverse_name='order_id', string='Order Detail')

    orderkursitamudetail_ids = fields.One2many(comodel_name='wedding.orderkursitamudetail', inverse_name='orderk_id', string='Order Kursi Tamu')

    name = fields.Char(string='Kode Order',required=True)
    
    tanggal_pesan = fields.Datetime(
        string='Tanggal Pemesanan',
        default=fields.Datetime.now,
    )
    
    
    tanggal_pengiriman = fields.Date(
        string='Tanggal Pengiriman',
        default=fields.Date.context_today,
    )

    pemesan = fields.Many2one(comodel_name='res.partner', string='pemesanan', domain=[('is_customernya','=',True)],store=True)

    total = fields.Integer(string='Total',compute='_compute_total', store=True )
    
    @api.depends('orderpanggungdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['wedding.orderpanggungdetail'].search([('order_id', '=' ,record.id)]).mapped('harga'))
            b = sum(self.env['wedding.orderkursitamudetail'].search([('orderk_id', '=' ,record.id)]).mapped('harga'))
            record.total = a + b
    
    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    
    def invoice(self):
        invoices = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.pemesan,
            'invoice_date': self.tanggal_pesan,
            'date': fields.Datetime.now(),
            'invoice_line_ids': [(0,0,{
                'product_id': 0,
                'name': 'xxx',
                'quantity': 1,
                'name': 'product test 1',
                'discount': 0,
                'price_unit': self.total,
                'price_subtotal': self.total,
            })]
        })
        self.sudah_kembali=True
        return invoices
    
    
class OrderPanggungDetail(models.Model):
        _name = 'wedding.orderpanggungdetail'
        _description = 'New Description'

        order_id = fields.Many2one(comodel_name='wedding.order', string='Order')
        panggung_id = fields.Many2one(comodel_name='wedding.panggung', string='Panggung')
    
        name =fields.Char(string='Name')
        harga = fields.Integer(string='harga', compute='_compute_harga')
        
        qty = fields.Integer(string='Quantity')
                
        harga_satuan = fields.Integer(string='harga_satuan', compute='_compute_harga_satuan')

        @api.depends('panggung_id')
        def _compute_harga_satuan(self):
            for record in self:
                record.harga_satuan = record.panggung_id.harga

        @api.depends('qty','harga_satuan')
        def _compute_harga(self):
            for record in self:
                record.harga = record.harga_satuan + record.qty

        @api.model 
        def create(self,vals):
            record =  super(OrderPanggungDetail,self).create(vals)
            if record.qty:
                self.env['wedding.panggung'].search([('id', '=' , record.panggung_id.id)]).write({'stok':record.panggung_id.stok-record.qty})
                return record
        
class OrderKursiTamuDetail(models.Model):
        _name = 'wedding.orderkursitamudetail'
        _description = 'New Description'
        
        orderk_id = fields.Many2one(comodel_name='wedding.order', string='Order Kursi')
        kursitamu_id = fields.Many2one(comodel_name='wedding.kursitamu', string='Kursi Tamu') 

        name = fields.Char(string='Name')
        harga_satuan = fields.Integer(string='Harga Satuan',compute='_compute_harga_satuan')
            
        @api.depends('kursitamu_id')
        def _compute_harga_satuan(self):
            for record in self:
                record.harga_satuan = record.kursitamu_id.harga

        qty = fields.Integer(string='Quantity')

            
        @api.constrains('qty')
        def _check_stok(self):
            for record in self:
                bahan = self.env['wedding.kursitamu'].search([('stok','<',record.qty),('id','=',record.id)])
                if bahan:
                    raise ValidationError("Stok bahan yang dipilih tidak cukup")

        harga = fields.Integer(string='harga', compute='_compute_harga')

        @api.depends('harga_satuan','qty')
        def _compute_harga(self):
            for record in self:
                record.harga = record.harga_satuan * record.qty 
            
        @api.model
        def create(self,vals):
            record = super(OrderKursiTamuDetail, self).create(vals) 
            if record.qty:
                self.env['wedding.kursitamu'].search([('id','=',record.kursitamu_id.id)]).write({'stok':record.kursitamu_id.stok-record.qty})
                return record

        
            
            
                         
          
    

        
        
    
    
    
    

from odoo import http, fields, models
from odoo.http import request
import json


class KursiTamu(http.Controller):
    @http.route(['/kursitamu','/kursitamu/<int:idnya>'], auth='public', methods=['GET'], csrf=True,type='json') 
    def getKursiTamu(self, idnya=None, **kwargs):
        kursi = request.env['wedding.kursitamu'].search([])
        value = []
        if not idnya:
            for k in kursi:
                value.append({"id":k.id,
                            "nama kursi":k.name , 
                            "tipe bahan":k.tipe,
                            "stok kursi": k.stok,
                            "harga sewa": k.harga})
            return json.dumps(value)
        else:
            kursi_id = request.env['wedding.kursitamu'].search([('id','=',idnya)])
            for k in kursi_id:
                value.append({"id":k.id,
                            "nama kursi":k.name , 
                            "tipe bahan":k.tipe,
                            "stok kursi": k.stok,
                            "harga sewa": k.harga})
            return json.dumps(value)

    @http.route('/createkursi', auth='user' ,methods=['POST'], type='json')
    def createKursiTamu(self, **kw):
        if request.jsonrequest:
            if kw['name']:
                vals={
                    'name': kw['name'],
                    'tipe': kw['tipe'],
                    'stok': kw['stok'],
                    'harga': kw['harga']
                }
                kursi_baru = request.env['wedding.kursitamu'].create(vals)
                args = {'success':True, 'ID':kursi_baru.id}
                return args
    
    @http.route(['/deletekursi','/deletekursi/<int:idnya>'], auth='user' ,methods=['DELETE'], type='json')
    def deleteKursiTamu(self, idnya=None, **kw):
        if idnya:
            kursi_id = request.env['wedding.kursitamu'].search([('id','=',idnya)]).unlink()
            return kursi_id
                
                    
               
# -*- coding: utf-8 -*-
{
    'name': "weddingorganizer",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/panggung_view.xml',
        'views/pelaminan_view.xml',
        'views/kursipengantin_view.xml',
        'views/kursitamu_view.xml',
        'views/order_view.xml',
        'views/pegawai_view.xml',
        'views/customer_view.xml',
        'views/pengembalian_view.xml',
        'views/akunting_view.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
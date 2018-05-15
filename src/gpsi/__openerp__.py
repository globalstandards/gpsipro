# -*- coding: utf-8 -*-

{
    'name': 'GPSI Module Extension',
    'version': '0.1',
    'category': 'Gpsi',
    'sequence': 35,
    'summary': 'Global Performance System Integrated',
    'description': '',
    'website': 'wwww.globalstd.com',
    'depends': ['mail', 'crm', 'sale'],
    'data': [
        'data/qms_data.xml',
        'views/sale_partner_views.xml',
        'views/sale_views.xml',
        'views/standarization_views.xml',
        'views/qms_views.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

# -*- coding: utf-8 -*-

{
    'name': 'Modulo para eliminar transacciones de pago en borrador LAPI',
    'version': '15.0.0.1',
    'description': 'Modulo para eliminar transacciones de pago en borrador LAPI',
    'author': 'Meridasoft',
    'category': 'third-party',
    'depends': [
        'website','website_sale','payment',
    ],
    'data': [
        'data/ir_cron_transaction.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}

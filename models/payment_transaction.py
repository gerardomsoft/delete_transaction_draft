# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
import datetime

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def run_deltras(self):
        date_real = datetime.datetime.now() - datetime.timedelta(hours=1)

        res_transactions = self.env['payment.transaction'].search([('create_date', '<=', date_real),
                           ('state', '=', 'draft'), ('bill_transaction_id', '=', False), ('bill_external_transaction_id', '=', False)
                           ,('bill_status_code', '=', False),('bill_response_message', '=', False),('bill_error_message', '=', False)])

        if res_transactions:
            res_transactions.unlink()
        else:
            return

        
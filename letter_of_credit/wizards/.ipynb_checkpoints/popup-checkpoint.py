from odoo import models, fields, api
from datetime import datetime,date,time


class LC(models.TransientModel):
    _name = 'popup.windo'
    _description = 'LC'
    percentage = fields.Float ()
    value = fields.Float ()
    percentage_box = fields.Boolean ()
    value_box = fields.Boolean ()
    lc = fields.Many2one('letter_of_credit.letter_of_credit', string = 'lC', readonly = True)
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)
    
    
    def _get_default_currency_id(self):
        return self.env.company.currency_id.id
    currency_id = fields.Many2one("res.currency", string="Valuta", required=True ,default = _get_default_currency_id)
    def create_entry(self, CL):
        return self.env['account.move'].create(CL)
    
    
    
    
    
    
    def action_create(self):
        debitA = 10000*5.1
        creditB =10000*5.1
        intry_vals = {
            'ref':'',
            'currency_id': self.currency_id.id,
            'partner_id': self.company_id.id,
            'journal_id': self.company_id.account_journal.id,
            'line_ids': [(0, 0, {
                        'name':  '/',
                        'debit':debitA,
                        'account_id': self.company_id.bank_account.id,
                        
                    }), (0, 0, {
                        'name': '/',
                        'credit':creditB ,
                        'account_id': self.company_id.credit_reservations.id,          
                    })],
            'company_id': self.company_id.id,}
        self.create_entry(intry_vals)
        
        
        
        
        
        debit = (100000*5)
        debit2 = (100000*0.1*5)
        credit = (100000*0.1*5)+( (100000*5) )
        intry_vals = {
            'ref':'',
            'currency_id': self.currency_id.id,
            'partner_id': self.company_id.id,
            'journal_id': self.company_id.account_journal.id,
            'line_ids': [(0, 0, {
                        'name':  '/',
                        'debit':debit,
                        'account_id': self.company_id.credit_reservations.id,
                        
                    }), (0, 0, {
                        'name':  '/',
                        'debit':debit2,
                        'account_id': self.company_id.bank_account.id,
                        
                    }),(0, 0, {
                        'name': '/',
                        'credit':credit ,
                        'account_id': self.company_id.bank_commission.id,          
                    })],
            'company_id': self.company_id.id,}
        self.create_entry(intry_vals)
        
  
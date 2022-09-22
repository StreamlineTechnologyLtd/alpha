from odoo import models, fields, api ,tools , _

class RealEstate(models.TransientModel):
    _inherit = ['res.config.settings']
    
    bank_account= fields.Many2one(related='company_id.bank_account', string='Banks account', readonly=False)
    letter_of_credit_account = fields.Many2one(related='company_id.credit_letter_of_credit_account', string='Letter of credit account', readonly=False)
    bank_commission= fields.Many2one(related='company_id.bank_commission', string='Bank Commission', readonly=False)
    credit_reservations = fields.Many2one(related='company_id.credit_reservations', string='Credit Reservations', readonly=False)
    account_journal = fields.Many2one(related='company_id.account_journal', string='Account journal', readonly=False)
    
    
    
from odoo import models, fields, api ,tools , _
from odoo.tools import image_process
from odoo.exceptions import RedirectWarning, UserError, ValidationError


class ResCompany(models.Model):
    _inherit = ['res.company']
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)
    bank_account = fields.Many2one('account.account')
    credit_letter_of_credit_account = fields.Many2one('account.account')
    bank_commission = fields.Many2one('account.account')
    credit_reservations = fields.Many2one('account.account')
    account_journal = fields.Many2one('account.journal')
    
class ResCompany(models.Model):
    _inherit = ['res.partner']
    
    bank_account = fields.Many2one('account.account')
    credit_letter_of_credit_account = fields.Many2one('account.account')
    bank_commission = fields.Many2one('account.account')
    credit_reservations = fields.Many2one('account.account')
    account_journal = fields.Many2one('account.journal')
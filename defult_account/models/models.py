# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class defult_account(models.Model):
#      _inherit = 'res.config.settings'
#      currency_exchange_journal_id = fields.Many2one(
#         comodel_name='account.journal',
#         related='company_id.currency_exchange_journal_id', readonly=False,
#         string="Currency Exchange Journal",
#         help='The accounting journal where automatic exchange differences will be registered')











class defult_account(models.Model):
    _name = 'defult_account.defult_account'
    _description = 'defult_account.defult_account'
    
    def _get_default_currency_id(self):
        return self.env.company.currency_id.id
    
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one("res.currency", string="Currency", required=True ,default = _get_default_currency_id)

    currency_exchange_journal_id = fields.Many2one(
        comodel_name='account.journal',
        related='company_id.currency_exchange_journal_id', readonly=False,
        string="Currency Exchange Journal",
        help='The accounting journal where automatic exchange differences will be registered')
    
    income_currency_exchange_account_id = fields.Many2one(
        comodel_name="account.account",
        related="company_id.income_currency_exchange_account_id",
        string="Gain Account",
        readonly=False)
    
    expense_currency_exchange_account_id = fields.Many2one(
        comodel_name="account.account",
        related="company_id.expense_currency_exchange_account_id",
        string="Loss Account",
        readonly=False)
    
    

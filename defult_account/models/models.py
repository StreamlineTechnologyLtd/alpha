# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class defult_account(models.Model):
#      _inherit = 'res.config.settings'
#      currency_exchange_journal_id = fields.Many2one(
#         comodel_name='account.journal',
#         related='company_id.currency_exchange_journal_id', readonly=False,
#         string="Currency Exchange Journal",
#         help='The accounting journal where automatic exchange differences will be registered')











# class defult_account(models.Model):
#     _name = 'defult_account.defult_account'
#     _description = 'defult_account.defult_account'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

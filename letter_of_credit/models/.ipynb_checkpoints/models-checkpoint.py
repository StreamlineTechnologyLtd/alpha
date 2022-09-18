-*- coding: utf-8 -*-

from odoo import models, fields, api


class letter_of_credit(models.Model):
    _name = 'letter_of_credit.letter_of_credit'
    _description = 'letter_of_credit.letter_of_credit'

    name = fields.Char()
    payment_type = fields.selecttion(type = fields.Selection([
        ('outbound', 'Send Mony'),
        ('inbound', 'Receive Mony '),
        ('transfer', 'Internal Transfer')
         ], required=True, default='out')
    moyen = fields.selecttion([
        ('cash', 'Cash'),
        ('check', 'Check '),
        ('transfer', 'Internal Transfer'),
        ('ic','Letter of Credit'),
        ('swift','Swift')
    ], required=True, default='out')
    partner_type = fields.selecttion([
        ('vendor', 'Vendor'),
        ('cust', 'customer'),
        
         ], required=True, default='ic')
    partner_id = fields.Many2one('res.partner', string='Partner')
    amount = fields.Monetary (string = 'Payment Amount', required=True,)
    jornal_id =  fields.Many2one('account.payment', string='Payment Jornal')
    applicant_bank =  fields.Many2one('banks.banks', string='Applicant Bank')
    recever_bank= fields.Many2one('banks.banks', string='Recever Bank')
    notifying_bank = fields.Many2one('banks.banks', string='Notifying Bank')
    inspection_Company = fields.Char(string= 'Inspection Company')
    company_id = fields.Many2one('res.partner', string='Company')  
    country_of_orign = fields.Many2many ('country.of.orign',string = 'Country of Orign')
    continent = fields.Many2many ('continent.continent',string = 'Continent')
    goods_description = fields.Char(string = 'Goods Description')
    payment_date = fields.Date(string='Payment Date')
    communication = fields.Char(string = 'Memo')

    payment_transaction_id = fields.Many2one ('payment.transaction',string='Payment transaction')
    partial = fields.selecttion(type = fields.Selection([
        ('allowed', 'Allowed'),
        ('not allowed', 'Not allowed ')
         ], required=True, default='out')
    incotarm_lc = fields.Many2one('account.incoterms',string = 'Incoterms')
    lc_currency_rate = fields.Float(string = 'Initial Currency Rate')
    lc_currency_final_rate = fields.Float(string = 'Final Currency Rate')
    remaining_amount = fields.Monetary()
    date_of_expiry = fields.Datetime(string='Expiry Date')
    date_of_shipment = fields.Datetime(string='Last Date of Shipment')
    lc_type = fields.selecttion([
        ('diffired_30day_invoice', '30 days starting from invoice date'),
        ('diffired_30day_invoice', '30 days starting from invoice date'),
        ('diffired_30day_invoice','30 days starting from invoice date '),
        ('diffired_30day_invoice','30 days starting from invoice datet'),
        ('diffired_30day_invoice','30 days starting from invoice date'),
        ('diffired_30day_invoice','30 days starting from invoice date'),
        ('diffired_30day_invoice','30 days starting from invoice date')
         ], required=True, default='ic')
    state = fields.selecttion([
        ('draft', 'Draft'),
        ('submit', 'Submit'),
        ('transfer','Bank Transfer'),
        ('ic','Letter of Credit'),
        ('swift','Swift')
         ], required=True, default='ic')
                                
    
    def post(self):
        self.state = 'submit'
    
    def check_collected_wizard(self):
        self.state = 'draft'
    
    def check_return_wizard(self):
        self.state = 'draft'
    
    def open_submit_lc(self):
        self.state = 'draft'
    
    def open_swift_lc(self):
        self.state = 'draft'
    
    def open_close_lc(self):
        self.state = 'draft'

                                
    def nsurance_fees(self):
        self.state = 'draft'
                                
                                
    def cancel_insurance_fees(self):
        self.state = 'draft'
                                
    def amend_lc(self):
        self.state = 'draft'
                                
        

class banks(models.Model):
    _name = 'banks.banks'
    _description = 'banks'

    bank_name = fields.Char(string = 'Applicant Bank')
                                     
                                     
class countryOrignTag(models.Model):
    _name = 'country.of.orign'
    _description = 'country of orign'

    tag_nane = fields.Char(string = 'Applicant Bank')
                                     
class continent(models.Model):
    _name = 'continent.continent'
    _description = 'continent'

    tag_nane = fields.Char(string = 'Continent')    
    
   
          
class PaymentTransaction(models.Model):
    _name = 'payment.transaction'
    _description = 'payment_transaction'

    Payment transaction = fields.Char(string = 'Continent')    
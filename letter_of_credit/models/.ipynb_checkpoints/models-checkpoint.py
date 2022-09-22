
from odoo import models, fields, api


class letter_of_credit(models.Model):
    _name = 'letter_of_credit.letter_of_credit'
    _description = 'letter_of_credit.letter_of_credit'

    
    
    def _get_default_currency_id(self):
        return self.env.company.currency_id.id
    
    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)
    currency_id = fields.Many2one("res.currency", string="Currency", required=True ,default = _get_default_currency_id)
    name = fields.Char()   
    payment_type = fields.Selection([
        ('outbound', 'Send Mony'),
        ('inbound', 'Receive Mony '),
        ('transfer', 'Internal Transfer')
         ], required=True, default='out')
    moyen = fields.Selection([
        ('cash', 'Cash'),
        ('check', 'Check '),
        ('transfer', 'Internal Transfer'),
        ('lc','Letter of Credit'),
        ('swift','Swift')
    ], required=True, default='out')
    partner_type = fields.Selection([
        ('vendor', 'Vendor'),
        ('cust', 'customer'),
        
         ], required=True, default='cust')
    partner_id = fields.Many2one('res.partner', string='Partner')
    amount = fields.Monetary (string = 'Payment Amount', required=True,currency_field="currency_id",defult=0)
    insurance_lc_fees = fields.Monetary (string = 'insurance lc fees', required=True,currency_field="currency_id")
    journal_id =  fields.Many2one('account.journal', string='Payment Jornal')
    applicant_bank =  fields.Many2one('banks.banks', string='Applicant Bank')                   
    receiver_bank= fields.Many2one('banks.banks', string='Recever Bank')
    notifying_bank = fields.Many2one('banks.banks', string='Notifying Bank')
    inspection_company = fields.Char(string= 'Inspection Company')
    vendors= fields.Many2one('res.partner', string='Company')  
    country_of_origin = fields.Many2many ('country.orign',string = 'Country of Orign')
    continent = fields.Many2many ('continent.continent',string = 'Continent')
    goods_description = fields.Char(string = 'Goods Description')
    payment_date = fields.Date(string='Payment Date')
    communication = fields.Char()
    remainder_value = fields.Monetary (string = 'Remainder value',currency_field="currency_id")
   #payment_transaction_id = fields.Many2one ('payment.transaction',string='Payment transaction')
    partial = fields.Selection([
        ('allowed', 'Allowed'),
        ('not allowed', 'Not allowed ')
         ], required=True, default='out')
    incoterm_lc = fields.Many2one('account.incoterms',string = 'Incoterms')
    lc_currency_rate = fields.Float(string = 'Initial Currency Rate')
    lc_currency_final_rate = fields.Float(string = 'Final Currency Rate')
    remaining_amount = fields.Monetary(currency_field="currency_id" ,defult=0)
    date_of_expiry = fields.Datetime(string='Expiry Date')
    date_of_shipment = fields.Datetime(string='Last Date of Shipment')
    lc_type = fields.Selection([
        ('diffired_30day_invoice', '30 days starting from invoice date'),
        ('diffired_60day_invoice', '60 days starting from invoice date'),
        ('diffired_90day_invoice','90 days starting from invoice date '),
        ('diffired_120day_invoice','120days starting from invoice date '),
        ('diffired_30day_hawb','30days starting from HAWB date'),
        ('diffired_60day_hawb','60 days starting from HAWB date'),
        ('diffired_90day_hawb','90 days starting from HAWB date'),
        ('diffired_120day_hawb','120days starting from HAWB date')  
         ], required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submit'),
        ('transfer','Bank Transfer'),
        ('lc','Letter of Credit'),
        ('swift','Swift'),
        ('posted','posted'),
        ('closed','Closed'),
        ('cancelled','cancelled'),
        ('reconciled','reconciled'),
        ('approved','approved')
         ], required=True, default='draft')
    bill_of_lading = fields.Boolean ()
    free_sale_certificate = fields.Boolean ()
    health_certificate = fields.Boolean ()
    air_way_bill = fields.Boolean ()
    commercial_invoice = fields.Boolean ()
    packing_list = fields.Boolean ()
    certificate_of_origin = fields.Boolean ()
    certificate_of_analysis = fields.Boolean ()
    certificate_of_inspection = fields.Boolean ()
    insurrance_certificate = fields.Boolean ()
    export_declaration = fields.Boolean ()
    vessel_declaration = fields.Boolean ()
    other_doc = fields.Boolean ()
    under_collection = fields.Boolean ()
                                
    
    
    
    def check_collected_wizard(self):
        self.state = 'draft'
    
    def check_return_wizard(self):
        self.state = 'draft'
    
    def create_entry(self, letter_of_credit):
        return self.env['account.move'].create(letter_of_credit)
    
    def open_submit_lc(self):
        self.state = 'submit'
        company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)
        debit = self.lc_currency_rate*self.amount
        credit =self.lc_currency_rate*self.amount
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
                        'name': '/',
                        'credit':credit ,
                        'account_id': self.company_id.bank_account.id,          
                    })],
            'company_id': self.company_id.id,}
        self.create_entry(intry_vals)
        
        
        
        
    
    def close(self):
        self.state = 'closed'
        company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company)
        debit = self.remainder_value*self.lc_currency_final_rate
        credit =self.remainder_value*self.lc_currency_final_rate
        intry_vals = {
            'ref':'',
            'currency_id': self.currency_id.id,
            'partner_id': self.company_id.id,
            'journal_id': self.company_id.account_journal.id,
            'line_ids': [(0, 0, {
                        'name':  '/',
                        'debit':debit,
                        'account_id': self.company_id.bank_account.id,
                        
                    }), (0, 0, {
                        'name': '/',
                        'credit':credit ,
                        'account_id': self.company_id.credit_letter_of_credit_account.id,          
                    })],
            'company_id': self.company_id.id,}
        self.create_entry(intry_vals)
    
    def open_close_lc(self):
        self.state = 'draft'

                                
    def isurance_fees(self):
        self.state = 'draft'
                                
                                
    def cancel_insurance_fees(self):
        self.state = 'draft'
                                
    def amend_lc(self):
        self.state = 'draft'
    
    def post (self):
        self.state = 'draft'
        
        
       
    def action_draft (self):
        self.state = 'draft'
        
    def insurance_fees (self):
        self.state = 'draft'
        
        

class banks(models.Model):
    
    _name = 'banks.banks'
    _description = 'banks'

    bank_name = fields.Char(string = 'Applicant Bank')
                                     
                                     
class countryOrignTag(models.Model):
    _name = 'country.orign'
    _description = 'country of orign'

    tag_nane = fields.Char(string = 'Applicant Bank')
                                     
class continent(models.Model):
    _name = 'continent.continent'
    _description = 'continent'

    tag_nane = fields.Char(string = 'Continent')    
    
   
          
# class PaymentTransaction(models.Model):
#     _name = 'payment.transaction'
#     _description = 'payment_transaction'

#     Payment_ransaction = fields.Char(string = 'Continent')    
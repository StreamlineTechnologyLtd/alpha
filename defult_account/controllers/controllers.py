# -*- coding: utf-8 -*-
# from odoo import http


# class DefultAccount(http.Controller):
#     @http.route('/defult_account/defult_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/defult_account/defult_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('defult_account.listing', {
#             'root': '/defult_account/defult_account',
#             'objects': http.request.env['defult_account.defult_account'].search([]),
#         })

#     @http.route('/defult_account/defult_account/objects/<model("defult_account.defult_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('defult_account.object', {
#             'object': obj
#         })

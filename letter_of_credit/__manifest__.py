# -*- coding: utf-8 -*-
{
    'name': "letter of credit",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.streamline.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','account_accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizards/popup.xml',
        'views/views.xml',
        'views/settings.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'auto_install': False,
}

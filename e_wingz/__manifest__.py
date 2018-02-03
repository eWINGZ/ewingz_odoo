# -*- coding: utf-8 -*-
{
    'name': "eWINGZ",

    'summary': """
        Aviation Maintenance and Parts Platform""",

    'description': """
This is the base app for eWINGZ
===============================

    Plan Workorders
    Assign Human Resources
    Order Parts
    Issue and handle Discrepancies
    CSR
    Send Invoice
    """,

    'author': "eWINGZ",
    'website': "http://ewingz.aero",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Aviation',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    #    'sale',
    #    'stock',
    #    'web',
    #    'project',
    #    'hr',
    #    'maintenance',
    #‚    'report',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #'css': ['static/src/css/eWINGZ.css'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
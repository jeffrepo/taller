# -*- coding: utf-8 -*-

{
    'name': 'Taller',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para Taller',
    'description': """

""",
    'depends': ['base','sale','purchase', 'project', 'web_studio', 'industry_fsm_report', 'repair', 'infilefel', 'account'],
    'data': [
        'views/repair_order_views.xml'
    ],
    'assets':{},
    'installable': True,
    'auto_install': False,
}

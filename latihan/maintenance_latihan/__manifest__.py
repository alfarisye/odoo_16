# -*- coding: utf-8 -*-
{
    'name': "HIT Maintenance",

    'summary': """
        Maintenance Customization""",

    'description': """
        Enhancement Maintenance Module.
    """,

    'author': "HIT Digital Indonesia",
    'website': "http://www.hitconsulting.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Maintenance',
    'version': '0.1',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'depends': ['maintenance'
                ],

    # always loaded
    # make sure the menu view is on the last
    'data': [
        'security/ir.model.access.csv',
        'data/equipment_master_list_sequence.xml',
        'views/category_views.xml',
        'views/brand_views.xml',
        'views/class_mainten_views.xml',
        'views/model_mainten_views.xml',
        'views/site_views.xml',
        'views/machine_code_views.xml',
        'views/machine_type_views.xml',
        'views/machine_category_views.xml',
        'views/machine_group_views.xml',
        'views/transfer_unit_views.xml',
        'views/service_type_views.xml',
        'views/measuring_reading_views.xml',
        'views/inherit_equipment_views.xml',
        'views/inherit_maintenance_request.xml',
        'views/equipments_menu_views.xml',
        'views/hit_maintenance_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}

# -*- coding: utf-8 -*-
{
    'name': "Hotel Management System",
    'summary': "Hotel Management System",
    'description': "Hotel Guest Registration and Billing System",
    'author': "Fionna Ravina",
    'website': "https://github.com/GGarrd/Hotel",

    'category': 'Uncategorized',
    'version': '11.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/guestregistration.xml',
        'views/mainmenu.xml',
        'views/charges.xml',
        'views/roomtypes.xml',
        'views/rooms.xml',
        'views/guests.xml',
    ],
    'installable': True,
    'application': True,
}

# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Enterprise Backend Theme",
    "summary": "Enterprise Backend Theme",
    "version": "12.0.0.1",
    "category": "Theme-Backend",
    "website": "https://www.youtube.com/c/JuventudProductivaVenezolana?sub_confirmation=1",
	"description": """
		Enterprise Backend Theme for Odoo 12.0 community edition.
		Material Theme
    """,
	'images':[
        'images/screen.png'
	],
    "author": "JUVENTUD PRODUCTIVA VENEZOLANA",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',

    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
		'views/users.xml',
    ],
    'live_test_url': 'https://www.youtube.com/c/JuventudProductivaVenezolana?sub_confirmation=1'

}


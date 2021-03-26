# -*- coding: utf-8 -*-

# I had to change technical name because:
# 1. https://gitlab.openminds.be/mirror/odoo/commit/5439e72a4ebd7716b813c7ec24fd59058151568f#075e6a8a08e3d13cd3291eca8f376670dad599ca_199_248
# 2. There is already a module with name payment_paystack

{
    'name': 'Login to Shop',
    'category': 'eCommerce',
    'summary': '''Users must login to view products''',
    'version': '1.0',
    'license': 'GPL-3',
    'author': 'Ewetoye Ibrahimsh',
    'website': 'https://github.com/EwetoyeIbrahim/login_to_shop',
    'description': "",
    'images': ['static/description/icon.png'],
    'depends': ['website', 'website_sale'],
    'data': ["templates.xml"],
    'installable': True,
}

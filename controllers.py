# -*- coding: utf-8 -*-
from odoo.http import request, route
from odoo.addons.website_sale.controllers.main import WebsiteSale

class ForceLogin(WebsiteSale):
    @route()
    def shop(self):
        if not request.session.uid:    
            return request.redirect('/web/login?redirect=/shop')
        return super(ForceLogin, self).shop()

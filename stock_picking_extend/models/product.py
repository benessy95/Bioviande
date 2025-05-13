# Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2015-2016 AvanzOSC
# Copyright 2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2017 Jacques-Etienne Baudoux <je@bcim.be>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    arab_name = fields.Char(string='Nom en Arab')
    
class ProductProduct(models.Model):
    _inherit = "product.product"
    
    arab_name = fields.Char(string='Nom en Arab',related='product_tmpl_id.arab_name',readonly=False,store=True)
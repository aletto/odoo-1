from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class CustomCheckoutController(WebsiteSale):
    
    def _get_mandatory_fields_billing(self, country_id=False):
        req = ["name", "email"]
        return req

    def _check_shipping_partner_mandatory_fields(self, partner_id):
        ''' return True if all mandatory fields for shipping address are complete '''
        shipping_fields_required = []
        return all(partner_id.read(shipping_fields_required)[0].values())

    def _get_mandatory_fields_shipping(self, country_id=False):
        req = ["name", "phone"]
        return req
    
    def values_preprocess(self, values):
        new_values = {
            'street': 'Indefinido', 
            'street2': '', 
            'city': 'Indefinido', 
            'zip': '1111', 
            'country_id': '10', 
            'state_id': '554',
            'field_required': ''
        }
        for k, v in values.items():
            if k in new_values:
                values[k] = new_values[k]

        return super(CustomCheckoutController, self).values_preprocess(values)
    
    @http.route('/shop/payment/validate', type='http', auth="public", website=True, sitemap=False)
    def shop_payment_validate(self, sale_order_id=None, **post):
        return request.redirect('/shop/confirmation')

    @http.route('/shop/payment', type='http', auth='public', website=True, sitemap=False)
    def shop_payment(self, **post):
        return request.redirect('/shop/confirmation')    
    
    @http.route('/shop/quotation', type='http', auth='public', website=True)
    def process_quotation(self, **post):
        return request.render("website_sale_quotation.quotation_form")
    
class QuotationController(http.Controller):

    @http.route('/shop/quotation_process', type='http', auth='public', website=True, sitemap=False)
    def process_quotation(self, **post):
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        order = request.website.sale_get_order()
        partner = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)
        if partner:
            session.partner_id = partner
        else:
            # Create a new partner
            partner_data = {
                'name': name,
                'email': email,
                'phone': phone
            }
            partner = request.env['res.partner'].sudo().create(partner_data)

        order.partner_id = partner.id
        # request.env['sale.order'].sudo().browse(order.id)
        request.website.sale_reset()

        # Redirect to some page after processing the quotation
        return request.redirect('/thank-you')
    
    
    
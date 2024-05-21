/** @odoo-module **/

import { registry } from '@web/core/registry';
import { AddToCartNotification } from '@website_sale/js/notification/add_to_cart_notification/add_to_cart_notification';

const { Component } = owl;

class CustomAddToCartNotification extends AddToCartNotification {
    static template = 'website_sale_quotation.customAddToCartNotification';

    setup() {
        super.setup();
        // Add custom setup code here
    }

    // Override or extend methods here
}
AddToCartNotification.template = 'website_sale_quotation.customAddToCartNotification'
// registry.category('components').add('AddToCartNotification', CustomAddToCartNotification);

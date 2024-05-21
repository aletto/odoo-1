# __manifest__.py

{
    'name': 'Website Sale Quotation',
    'summary': 'Customize sale process for quotations',
    'description': """
        Customize sale process for quotations:
        - Replace "Add to Cart" labels with "Agregar a la Cotización"
        - Rename "Cart" to "Pedido de Cotización"
        - Modify Cart Wizard to gather required information
        - Create draft sale order after information is completed
        - Display confirmation message
    """,
    'author': 'Andres Letto',
    'version': '1.0',
    'depends': ['base', 'website_sale', 'website', 'web'],
    'data': [
        'views/website_sale_templates.xml',
        'views/sale_order_views.xml',
        'views/confirmation_template.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'website_sale_quotation/static/src/js/custom_add_to_cart_notification.js',
            'website_sale_quotation/static/src/xml/add_to_cart_notification.xml',
        ],
    },
    'installable': True,
    'application': True,
}
from odoo import http

class Registry(http.Controller):
    @http.route("/registry/", auth="public", website=True)
    def index(self, **kw):
        return "Hello World"

    @http.route("/registry/compare/", auth="public", website=True)
    def compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
        return http.request.render('motorcycle_registry.compare_website', {
            'motorcycles' : motorcycles,
        })
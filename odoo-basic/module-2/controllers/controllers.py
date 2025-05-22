# -*- coding: utf-8 -*-
# from odoo import http


# class Module-2(http.Controller):
#     @http.route('/module-2/module-2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-2/module-2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-2.listing', {
#             'root': '/module-2/module-2',
#             'objects': http.request.env['module-2.module-2'].search([]),
#         })

#     @http.route('/module-2/module-2/objects/<model("module-2.module-2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-2.object', {
#             'object': obj
#         })


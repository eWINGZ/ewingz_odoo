# -*- coding: utf-8 -*-
from odoo import http

# class EWingz(http.Controller):
#     @http.route('/e_wingz/e_wingz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e_wingz/e_wingz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('e_wingz.listing', {
#             'root': '/e_wingz/e_wingz',
#             'objects': http.request.env['e_wingz.e_wingz'].search([]),
#         })

#     @http.route('/e_wingz/e_wingz/objects/<model("e_wingz.e_wingz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e_wingz.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'openacademy.student'

    name = fields.Char(string="Name", required="True")
    exam_id = fields.Many2one('openacademy.exam',string="Exam")
   
    
    
    

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'
#     _description = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

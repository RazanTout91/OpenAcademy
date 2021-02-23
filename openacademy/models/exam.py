# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Exam(models.Model):
    _name = 'openacademy.exam'

    name = fields.Char(string="Exam", required="True")
    student_id = fields.One2many('openacademy.student','exam_id')
    mathsubj = fields.Float(string="Math")
    physsubj = fields.Float(string="Physics")
    chemsubj = fields.Float(string="Chemistry")
    
    @api.onchange('mathsubj','physsubj','chemsubj')
    def calculate_average(self): 
        if self.mathsubj == 0 or self.physsubj == 0 or self.chemsubj == 0 :
           return {'warning':{'title':'Error!','message':'your message'}}
        tot =  mathsubj + physsubj + chemsubj
        avg = tot/3
        return avg    
    

    
    
  
    
    
    

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

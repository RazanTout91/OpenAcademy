# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="CourseTitle", required="True")
    description = fields.Text(string="CourseDescription")
    teacher_id = fields.Many2one('openacademy.teacher',string="Teacher")
    
   
    
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(string="Session", required="True")
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number Of Seats")
    course_id = fields.Many2one('openacademy.course',string="Course")
    
    
    

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

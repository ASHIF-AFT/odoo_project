# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Players(models.Model):
    _name = 'players.players'

    name = fields.Char(string="Footballer's Name")
    age = fields.Integer(string="Age")
    position = fields.Char(string="Position")
    salary=fields.Integer(string="Salary")

    manager_id = fields.Many2one('res.partner', string="Manager")
    details = fields.Many2many("player_details", string="Player_Details")

    annual_salary = fields.Integer(string="Annual slary", compute='get_annual_salary')
    status = fields.Selection([("fit", "Fit To Play"), ("injury", "Injured")], string="status", default="fit")

    def get_annual_salary(self):
        for s in self:
            s.annual_salary= 12 * s.salary

    def set_status_to_fit(self):

        self.status="fit"


    def set_status_to_injured(self):
        self.status = "injury"






class Player_details(models.Model):
    _name = "player_details"

    name=fields.Char(string="Name")
    value=fields.Char(string="Value")
#
#     ('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    alias=fields.Char(string='Alias')   

    type_of_contract=fields.Selection([
        ('unique ocassion', 'Unique Ocassion'), 
        ('eventually', 'Eventually'),
        ('proyect','Project'),
        ('fixed','Fixed')])

    payment_method=fields.Selection([
        ('cash', 'Cash'), 
        ('wire transfer', 'Wire Transfer'),
        ('tdde','TDDE'),
        ('credit card','Credit Card')])

    pay_frequency=fields.Selection([
        ('weekly', 'weekly'), 
        ('fortnightly','Fortnightly'),
        ('monthly','Monthly'),
        ('anually','Anually'),
        ('variable','Variable')])

    agreement_tc=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])
        
    contract_signing_date=fields.Date(index=True)

    physical = fields.Boolean('Physical')
    digital = fields.Boolean('Digital')

    validation=fields.Text(string='Validation') 
    
    term=fields.Date(index=True)

    penalty=fields.Text(string='Penalty')

    value_of_the_consideration=fields.Float('Value of the Consideration')
    
    currency=fields.Selection([
        ('mxn','MXN'),
        ('eur','EUR'),
        ('usd','USD'),
        ('cop','COP'),
        ('gbp','GBP'),
        ('other','Other')])

    nda=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])

    constitutive_act=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])

    id_representative=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])

    representative_power=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])

    supplier_score=fields.Selection([
        ('low', 'Low'), 
        ('medium','Medium'),
        ('high','High')])
    
    review_69=fields.Date(index=True)
    
    opinion_on_compliance=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])

    date_annex_32D=fields.Date(index=True)

    csf=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])
    
    proof_of_address=fields.Selection([
        ('yes', 'Yes'), 
        ('pending','Pending'),
        ('no apply','No Apply')])
from odoo import api, fields, models

class Expediteur(models.Model):
    _name = "oflix.expediteur"
    _description = "Le module expediteur"
    
    
    collis_id = fields.One2many('oflix.collis','id_expediteur',string="Collis envoyés")
    nom = fields.Char()
    adresse = fields.Char()
    phone = fields.Char()
    type = fields.Selection([('particulier','Particulier'),('société','Société'),('autres','autres')])
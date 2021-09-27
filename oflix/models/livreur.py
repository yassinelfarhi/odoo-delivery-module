from odoo import api, fields, models

class Livreur(models.Model):
    _name = "oflix.livreur"
    _description = "Le module livreur"


    collis_id = fields.One2many('oflix.collis','id_livreur',string="Collis assignés") 
    id_destinataire = fields.One2many('oflix.destinataire','id_livreur',string="Destinataires")
    name = fields.Char(string="Nom Livreur")
    phone = fields.Char(string="Telephone")

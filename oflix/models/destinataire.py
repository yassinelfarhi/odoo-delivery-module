from odoo import api, fields, models

class Destinataire(models.Model):
    _name = "oflix.destinataire"
    _description = "Le module destinataire"

    id_livreur = fields.Many2one('oflix.livreur',string="Livreur")
    nom_destinataire = fields.Char(string="Nom")
    phone_destinataire = fields.Char(string="Phone")
    addresse_destinataire = fields.Char(string="Adresse")


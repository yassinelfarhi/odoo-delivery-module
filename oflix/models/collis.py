from odoo import api, fields, models

class Collis(models.Model):
    
    _name = "oflix.collis"
    _description = "Le module collis"
   


    id_expediteur = fields.Many2one('oflix.expediteur', string="Expediteur")
    id_livreur = fields.Many2one('oflix.livreur', string="Livreur")
    #expediteur = fields.Many2one('expediteur.nom',string="Expediteur")
    ville_expedition = fields.Selection([
       ('rabat','Rabat'),('casa','Casa'),('tanger','Tanger'),('tetouan','Tetouan')
    ])
    date_arrivee = fields.Date()
    date_depart = fields.Date()
    code_reference = fields.Char()

    nom_destinataire = fields.Char()
    phone_destinataire = fields.Char()
    addresse_destination = fields.Char()
    date_arrivee_prevue = fields.Date()
    status = fields.Selection([
       ('en stock','En stock'),('en cours','en cours'),('livré','livré')
    ])

    #nom_livreur = fields.Many2one('livreur.name',string="Livreur")
    date_depart_prevue = fields.Date()





    

    
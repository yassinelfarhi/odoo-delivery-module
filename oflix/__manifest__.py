

{
    'name': 'OFLIX LIVRAISON',
    'version': '1.0',
    'author' : 'DATA WEB CONSULTING',
    'category': 'Sales/CRM',
    'sequence': -100,
    'summary': 'Logiciel de gestion de collis de la société OFLIX  à NADOR',
    'description': "logiciel de gestion de collis",
    'website': 'https://www.oflix.com/',
    'depends': [],
    'data': [
        'views/expediteurs.xml',
        'views/collis.xml',
        'views/livreurs.xml',
        'views/destinataires.xml',
        'views/calendrier.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
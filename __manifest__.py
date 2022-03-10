{

'name': 'BIRTUM | Nombre del módulo',
'author': 'BIRTUM ©',
'category': 'Extra Tools',
'sequence': 50,
'summary': "Descripción corta del módulo",
'website': 'https://www.birtum.com',
'version': '15.0',
'license': 'LGPL-3', 
'description': """

Nombre del módulo (name)

-------------------------------------------------

Descripción ampliada del módulo:

""",
'depends': [
'contacts',
],
'data': [
    'security/ir.model.access.csv',
    'views/inherit_res_partner_view.xml'
    
],
'demo': [],
'qweb': [],
'installable': True,
'application': True,
'autoinstall': False,
}
from lxml import etree
doc = etree.parse('alquilercoches.xml')

def contador(doc):
	cantidad = doc.xpath('count(//nombre/content)')
	cantidad = int(cantidad)
	return cantidad

print("La cantidad de empresas de alquileres de coches:",contador(doc))
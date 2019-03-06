from lxml import etree
doc = etree.parse('alquilercoches.xml')

def buscar(doc):
	tlf = doc.xpath('//telefono/content/text()')
	#for i in doc:
	#	compañias = doc.xpath('//telefono[content="%s"]/text()/')

	return tlf

print (buscar(doc))
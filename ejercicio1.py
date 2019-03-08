from lxml import etree
doc = etree.parse('alquilercoches.xml')

def buscar(telefono,doc):
	telefonos = doc.xpath('//telefono[content="%s"]/../nombre/content/text()' % telefono) 
	return telefonos

telefono = input("Introduce un numero de telefono: ")

print (buscar(telefono,doc))

#//telefono[starts-with(content,'985')]/../nombre/content/text()
from lxml import etree
doc = etree.parse('alquilercoches.xml')

def buscar(telefono,doc):
	telefonos = doc.xpath('//telefono[content="%s"]/../nombre/content/text()' % telefono) 
	print(telefonos)
	return telefonos

telefono = input("Introduce un numero de telefono: ")

nombres = buscar(telefono,doc)

for i in nombres:
	print (i)

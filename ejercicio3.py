from lxml import etree
doc = etree.parse('alquilercoches.xml')

def calles(nombre,doc):
	calles = doc.xpath('//direccion/element[content="%s"]/../../nombre/content/text()' % nombre)
	return calles

nombre = input("Introduce el nombre de una calle: ")

nombres = calles(nombre,doc)

for i in nombres:
	print ("Nombre de la empresa de alquiler:",i)
	
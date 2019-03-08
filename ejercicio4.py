from lxml import etree
doc = etree.parse('alquilercoches.xml')

def horarios(nombre,doc):
	horarios = doc.xpath('//nombre[content="%s"]/../horario/text()' % nombre) 
	return horarios

nombre = input("Introduce el nombre de una empresa: ")

horarios = horarios(nombre,doc)

for i in horarios:
	print ("Horario de %s: %s" % (nombre,i))


from lxml import etree
doc = etree.parse('alquilercoches.xml')

def variados(direccion,doc):
	nombre = doc.xpath('//direccion/element[content="%s"]/../../nombre/content/text()' % direccion) 
	telefono = doc.xpath('//direccion/element[content="%s"]/../../telefono/content/text()' % direccion) 
	web = doc.xpath('//direccion/element[content="%s"]/../../web/text()' % direccion) 
	localizacion = doc.xpath('//direccion/element[content="%s"]/../../localizacion/content/text()' % direccion) 
	return nombre,telefono,web,localizacion

nombre = input("Introduce el nombre de una calle: ")

nombre,telefono,web,localizacion = variados(nombre,doc)

print ("Nombre de la empresa:",nombre)
print ("Numero de telefono:",telefono)
print ("Direccion de la pagina web:",web)
print ("Coordena de localizacion:",localizacion)
from xml.dom import minidom

if __name__ == '__main__':
    xmldoc = minidom.parse('/Users/maciejnawrocki/Desktop/python/zadania/a.xml')
    itemlist = xmldoc.getElementsByTagName('company')[0]
    itemlist.firstChild.data = "aaa"
    file = open('b.xml', "w")
    xml = xmldoc.toxml()
    file.write(xml)
from xml.etree import ElementTree
def searchingall (filename):
    doc = ElementTree.parse(filename)
    records = doc.findall('record')
    return (records)

from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Вернуть красиво оформленную XML-строку для объекта Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=" ")

import re
from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring
from xml.dom import minidom


def to_camelcase(s):
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)


class XMLWriter(object):

    def __init__(self, reader):
        self.reader = reader

    def write(self, file):
        tree = ElementTree(self.into(Element, 'glyph'))
        tree.write(file, encoding='utf-8', xml_declaration=True)

    def into(self, kind, *args):
        attributes = {to_camelcase(a): str(getattr(self.reader, a))
                        for a in self.reader.attribute_names
                        if getattr(self.reader, a) is not None}

        tree = kind(*args, **attributes)

        xml_items = []

        for element_name in self.reader.element_names:
            element = getattr(self.reader, element_name)
            xml_element = self.__class__(element).into(Element, to_camelcase(element_name))
            xml_items.append(xml_element)

        for collection_name in self.reader.collection_names:
            collection = getattr(self.reader, collection_name)
            for item in collection:
                xml_item = self.__class__(item).into(Element, to_camelcase(collection_name.rstrip('s')))
                xml_items.append(xml_item)

        tree.extend(xml_items)

        return tree

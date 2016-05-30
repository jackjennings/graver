from graver.reader.null_reader import NullReader


class ProxyReader(object):

    def __init__(self, reader=None, *args, **kwargs):
        self.reader = reader or NullReader()

        try:
            super(ProxyReader, self).__init__(*args, **kwargs)
        except:
            pass

    def __eq__(self, other):
        return type(other) is self.__class__ and \
            all((getattr(self, attr) == getattr(other, attr) for attr in self.attribute_names)) and \
            all((getattr(self, attr) == getattr(other, attr) for attr in self.element_names)) and \
            all((getattr(self, attr) == getattr(other, attr) for attr in self.collection_names))

    def __ne__(self, other):
        return not self.__eq__(other)

    def attribute(self, name, kind=str):
        value = self.reader.attribute(name)
        if value is not None:
            return kind(value)

    def element(self, name):
        return self.reader.element(name)

    def elements(self, name):
        return self.reader.elements(name)

    @property
    def attribute_names(self):
        return getattr(self, 'ATTRIBUTES', [])

    @property
    def element_names(self):
        return getattr(self, 'ELEMENTS', [])

    @property
    def collection_names(self):
        return getattr(self, 'COLLECTIONS', [])

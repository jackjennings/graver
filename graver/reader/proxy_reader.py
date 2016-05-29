from graver.reader.null_reader import NullReader


class ProxyReader(object):

    def __init__(self, reader=None, *args, **kwargs):
        self.reader = reader or NullReader()

        try:
            super(ProxyReader, self).__init__(*args, **kwargs)
        except:
            pass

    def attribute(self, name, kind=str):
        value = self.reader.attribute(name)
        if value is not None:
            return kind(value)

    def element(self, name):
        return self.reader.element(name)

    def elements(self, name):
        return self.reader.elements(name)

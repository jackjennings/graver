from graver.reader.null_reader import NullReader


class ProxyReader(object):

    def __init__(self, reader=None, *args, **kwargs):
        self.reader = reader or NullReader()

        try:
            super(ProxyReader, self).__init__(*args, **kwargs)
        except:
            pass

    def attribute(self, name):
        return self.reader.attribute(name)

    def element(self, name):
        return self.reader.element(name)

    def elements(self, name):
        return self.reader.elements(name)

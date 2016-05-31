class attachment(object):

    def __init__(self, attr):
        self.attr = attr

    def attach(self, collection, cls):
        if not hasattr(cls, collection):
            setattr(cls, collection, [])

        getattr(cls, collection).append(self.attr)


class attribute(attachment):

    def __call__(self, cls):
        self.attach('ATTRIBUTES', cls)
        return cls


class element(attachment):

    def __call__(self, cls):
        self.attach('ELEMENTS', cls)
        return cls


class collection(attachment):

    def __call__(self, cls):
        self.attach('COLLECTIONS', cls)
        return cls

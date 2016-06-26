class represents(object):

    def __init__(self, cls, *args):
        self.representation = Representer(cls, *args)

    def __call__(self, fn):
        return self.representation(fn)


class Representer(object):

    def __init__(self, cls, *args):
        self.cls = cls
        self.args = list(args)

    def __call__(self, default):
        self.default = default
        self.name = default.__name__
        self.key = "_" + self.name
        return self

    def __get__(self, inst, *args, **kwargs):
        if not hasattr(inst, self.key):
            setattr(inst, self.key, self.cls(*(self.args + [self.default.__call__(inst)])))

        return getattr(inst, self.key)

    def __set__(self, inst, value):
        setattr(inst, self.key, self.cls(*(self.args + [value])))
        return self.__get__(inst)

class VersionAccessError(Exception): pass


class version(object):

    def __init__(self, *versions):
        self.versions = versions

    def __call__(self, fn):
        for version in self.versions:
            fn = VersionedAttributeDispatcher.wrap(fn).accepting(version)

        return fn


class VersionedObject(object):

    def __init__(self, *args, **kwargs):
        self.version = int(kwargs.get('version'))
        del kwargs['version']
        super(VersionedObject, self).__init__(*args, **kwargs)


class VersionedAttributeDispatcher(object):

    @classmethod
    def wrap(cls, fn):
        if type(fn) is cls:
            return fn
        else:
            return cls(fn)

    def __init__(self, fn):
        self.fn = fn
        self.versions = set()

    def __get__(self, inst, type=None):
        version = inst.version

        if self.accepts(version):
            return self.fn.__get__(inst)
        else:
            raise VersionAccessError

    def __set__(self, inst, value):
        return self.fn.__set__(inst, value)

    def accepting(self, version):
        self.versions.add(version)
        return self

    def accepts(self, version):
        return version in self.versions

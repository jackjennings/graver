class VersionAccessError(Exception): pass


class version(object):

    def __init__(self, version):
        self.version = version

    def __call__(self, fn):
        if type(fn) is property:
            return fn
        else:
            def wrapped(*args, **kwargs):
                return fn(*args, **kwargs)
            return wrapped


class VersionedObject(object):

    def __init__(self, *args, **kwargs):
        self.version = kwargs.get('version')
        del kwargs['version']
        super(VersionedObject, self).__init__(*args, **kwargs)


class VersionedFunctionDispatcher(object): pass


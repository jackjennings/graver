class Collection(list):

    def __init__(self, kind, items=None):
        self.kind = kind
        items = [self.kind(r) for r in (items or [])]
        super(Collection, self).__init__(items)

class Collection(list):

    def __init__(self, kind, *args):
        self.kind = kind
        super(Collection, self).__init__(*args)

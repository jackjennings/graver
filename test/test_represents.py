from graver.represents import represents
from graver.collection import Collection


class Note(object):

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "<Note: {}>".format(self.text)

    def __eq__(self, other):
        return self.text == other.text


class Parent(object):

    @represents(Note)
    def bar(self):
        return 'blah'

    @represents(Collection, Note)
    def foo(self):
        return ['blah']


class TestRepresents(object):

    def test_gets_representation(self):
        p = Parent()
        assert p.bar == Note('blah')

    def test_gets_identical_representation(self):
        p = Parent()
        assert p.bar is p.bar

    def test_gets_representation_with_arguments(self):
        p = Parent()
        assert p.foo == Collection(Note, ['blah'])

    def test_sets_representation(self):
        p = Parent()
        p.bar = 'new note'
        assert p.bar == Note('new note')

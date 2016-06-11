import pytest

from graver.versioned import version, VersionedObject, VersionAccessError


class VersionedClass(VersionedObject):

    @version(1, 2)
    def foo(self):
        return 'foo'

    @version(1)
    @property
    def bar(self):
        return 'bar'

    def baz(self): pass
    baz.prop = 'baz'
    baz = version(1)(baz)


class TestVersioned(object):

    def test_returns_function_from_dispatcher(arg):
        assert VersionedClass(version=1).foo() is 'foo'

    def test_returns_property_from_dispatcher(arg):
        assert VersionedClass(version=1).bar is 'bar'

    def test_version_raises_an_error_with_out_of_bounds_version(self):
        with pytest.raises(VersionAccessError):
            VersionedClass(version=2).bar

    def test_version_hasattr_returns_false_with_out_of_bounds_version(self):
        assert hasattr(VersionedClass(version=2), 'bar') is False

    def test_version_hasattr_returns_true_with_in_bounds_version(self):
        assert hasattr(VersionedClass(version=1), 'bar') is True

    def test_maintains_access_to_decorated_function_dict(self):
        assert VersionedClass(version=1).baz.prop is 'baz'

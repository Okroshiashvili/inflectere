import pytest

from inflectere import Inflectere


def test_singularize():
    inflectere = Inflectere()
    with pytest.raises(NotImplementedError):
        inflectere.singularize("dogs")


def test_pluralize():
    inflectere = Inflectere()
    with pytest.raises(NotImplementedError):
        inflectere.pluralize("dog")


def test_is_singular():
    inflectere = Inflectere()
    with pytest.raises(NotImplementedError):
        inflectere.is_singular()


def test_is_plural():
    inflectere = Inflectere()
    with pytest.raises(NotImplementedError):
        inflectere.is_plural()

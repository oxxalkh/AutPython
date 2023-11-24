import pytest


@pytest.fixture()
def good_word():
    return "печенюшка"

@pytest.fixture()
def bad_word():
    return "печеtнюшшка"
from cards import Card


def test_field_access():
    c = Card("something", "brian", "todo", 123)

    assert c.summary == "something"
    assert c.owner == "brian"
    assert c.state == "todo"
    assert c.id == 123


def test_defaults():
    c = Card()

    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 123)

    assert c1 == c2
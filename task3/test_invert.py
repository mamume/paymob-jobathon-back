from inverter import invert


def test_invert():
    assert invert(None) == ""
    assert invert('') == ""
    assert invert('a') == "a"
    assert invert('abcd') == "dcba"

from um import count


def test_single():
    """Test expressions with one 'um'"""
    assert count('um') == 1
    assert count('um.') == 1
    assert count('um?') == 1


def test_full_sentence():
    """Test full sentences with multiple 'um'"""
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2


def test_no_um():
    """Test expressions with no 'um'."""
    assert count('Thanks for the album.') == 0
    assert count('Umbelieveable') == 0

def test_stacked():
    """Test multiple 'um' stacked."""
    assert count('um, um') == 2
    assert count('um, um, um?') == 3
    assert count('um, um, um') == 3

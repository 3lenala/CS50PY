from working import convert
import pytest


def test_no_to():
    """Test inputs with no 'to'."""
    with pytest.raises(ValueError):
        convert('9:00 AM')
    with pytest.raises(ValueError):
        convert('9 AM')
    with pytest.raises(ValueError):
        convert('9:00 AM 5:00 PM')
    with pytest.raises(ValueError):
        convert('9:00 AM to five PM')
    with pytest.raises(ValueError):
        convert('0 AM to 5 PM')
    with pytest.raises(ValueError):
        convert('0 PM to 5 PM')


def test_24_hour_format():
    """Test inputs with time given in 24-hour format."""
    with pytest.raises(ValueError):
        convert('09:00 to 05:00')


def test_invalid_range():
    """Test out of range values for hour and minutes in 12-hour format."""
    with pytest.raises(ValueError):
        convert('25 AM to 25:30 PM')
    with pytest.raises(ValueError):
        convert('13:00 AM to 15:00 PM')
    with pytest.raises(ValueError):
        convert('9 AM to 5:79 PM')
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:00 PM')


def test_lowercase_meridiem():
    """Test that lowercase am/pm is rejected."""
    with pytest.raises(ValueError):
        convert('9:00 am to 5:00 PM')
    with pytest.raises(ValueError):
        convert('9:00 am to 5:00 pm')


def test_zero_padded_hour():
    """Test that hours with a leading zero are rejected."""
    with pytest.raises(ValueError):
        convert('09:00 AM to 5:00 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM to 05:00 PM')


def test_different_formats():
    """Test valid formats for the input."""
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9:30 AM to 5:30 PM') == '09:30 to 17:30'
    assert convert('9:00 AM to 10:00 AM') == '09:00 to 10:00'
    assert convert('9:00 AM to 9:05 AM') == '09:00 to 09:05'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'

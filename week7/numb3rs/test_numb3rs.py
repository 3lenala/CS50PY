# Test validate function from numb3rs.py script

from numb3rs import validate


def test_non_numeric():
    """Test non numeric strings."""
    assert not validate('a.b.c.d')
    assert not validate('cat.dog.turtle.brasil')
    assert not validate('!.!/$%&.&%$·&.&%%')
    assert not validate('hello.world.cs.50')
    assert not validate('https://twitter.com/username')
    assert not validate('cat')


def test_out_of_range_numbers():
    """Test strings in correct format that contain numbers
    greater than 255."""
    assert not validate('256.256.256.256')
    assert not validate('1.2.3.1000')
    assert not validate('512.512.512.512')
    assert not validate('1.2.3.256')
    assert not validate('1234')


def test_format():
    """Test strings in invalid format:
            - Separation characters different to periods
            - Octets with leading zeros (e.g., 001)
            - Inputs with too few octets."""
    assert not validate('192.168.001.1')
    assert not validate('1?2?3?4')
    assert not validate('1¿2!3!4')
    assert not validate('1-2-3-4')
    assert not validate('1,2,3,4')
    assert not validate('1.2.3')
    assert not validate('255.255')
    assert not validate('175')


def test_valid():
    """Test valid IP addresses."""
    assert validate('1.2.3.4')
    assert validate('1.19.157.237')
    assert validate('19.37.28.49')
    assert validate('194.124.157.189')
    assert validate('250.251.252.255')
    assert validate('200.220.221.210')
    assert validate('127.0.0.1')
    assert validate('255.255.255.255')

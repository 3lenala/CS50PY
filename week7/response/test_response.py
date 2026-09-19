from response import check_validity

def test_special_characters_user():
    """Test special characters in username"""
    assert check_validity('malan@@@harvard.edu') == 'Invalid'
    assert check_validity('malan@@harvard.edu') == 'Invalid'
    assert check_validity('.ab@harvard.edu') == 'Invalid'
    assert check_validity('a..b@harvard.edu') == 'Invalid'
    assert check_validity('"ma@lan"@harvard.edu') == 'Invalid'
    assert check_validity('ma@lan@harvard.edu') == 'Invalid'


def test_special_characters_domain():
    """Test special characters in domain"""
    assert check_validity('malan@harvard..edu') == 'Invalid'
    assert check_validity('malan@har!vard.edu') == 'Invalid'
    assert check_validity('malan@harv,ard.edu') == 'Invalid'
    assert check_validity('ab@dominio_raro.com') == 'Invalid'
    assert check_validity('ab@-dominio.com') == 'Invalid'


def test_valid_emails():
    """Test valid emails"""
    assert check_validity('malan@harvard.edu') == 'Valid'
    assert check_validity('malan.malan@harvard.edu') == 'Valid'
    assert check_validity('malan@cs50.harvard.edu') == 'Valid'

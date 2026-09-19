from watch import parse


def test_protocol():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'


def test_no_www():
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_different_src():
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None
    assert parse('<iframe width="560" height="315" src="http://cs50.harvard.edu/python"></iframe>') == None


def test_multiple_arguments():
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'
    assert parse('<iframe width="560" height="315" src="http://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

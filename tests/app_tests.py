from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()


def test_app():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"waking up on the catwalk", rv.data)


def test_session():
    with web.session_transaction() as sess:
        sess['room_name'] = 'laser_weapon_armory'
    rv = web.get('/game', follow_redirects=True)
    assert_in(b"locked with a 3 digit", rv.data)


def test_session_next():
    with web.session_transaction() as sess:
        sess['room_name'] = 'laser_weapon_armory'
    rv = web.post('/game', data='action=012',
                  content_type='application/x-www-form-urlencoded', follow_redirects=True)
    assert_in(b"maintain a slow heart", rv.data)

    # rv = web.get('/hello', follow_redirects=True)
    # assert_equal(rv.status_code, 200)
    # assert_in(b"Fill Out This Form", rv.data)

    # data = {'name': 'Zed', 'greet': 'Hola'}
    # rv = web.post('/hello', follow_redirects=True, data=data)
    # assert_in(b"Zed", rv.data)
    # assert_in(b"Hola", rv.data)

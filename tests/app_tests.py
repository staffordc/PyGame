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


def test_session_next1():
    with web.session_transaction() as sess:
        sess['room_name'] = 'the_bridge'
    rv = web.post('/game', data='action=look up',
                  content_type='application/x-www-form-urlencoded', follow_redirects=True)
    assert_in(b"though... what was it?", rv.data)


def test_session_next2():
    with web.session_transaction() as sess:
        sess['room_name'] = 'escape_pod'
    rv = web.post('/game', data='action=control stick',
                  content_type='application/x-www-form-urlencoded', follow_redirects=True)
    assert_in(b"2 years outside of port", rv.data)


def test_session_next3():
    with web.session_transaction() as sess:
        sess['room_name'] = 'central_corridor'
    rv = web.post('/game', data='action=boot knife',
                  content_type='application/x-www-form-urlencoded', follow_redirects=True)
    assert_in(b"it is locked with a 3", rv.data)

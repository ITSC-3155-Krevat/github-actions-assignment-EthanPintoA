def test_get_all_cats(test_app):
    res = test_app.get('/cats')

    assert res.status_code == 200
    assert b'No CATS! Go make a CAT.' in res.data


def test_create_cat(test_app):
    res = test_app.post('/cats', data={
        'name': 'Piero',
        'breed': 'Orange',
        'numLegs': 4,
    }, follow_redirects=True)

    assert res.status_code == 200
    assert b'Piero' in res.data
    assert b'Orange' in res.data
    assert b'4' in res.data

def test_root_returns_message(client):
    res = client.get('/')
    assert res.status_code == 200
    assert 'message' in res.json()

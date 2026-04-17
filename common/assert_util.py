def assert_response(res, code=200):
    assert res.status_code == code
    json_data = res.json()
    assert json_data["code"] == 200
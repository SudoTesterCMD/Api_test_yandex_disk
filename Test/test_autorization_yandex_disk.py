from Base_App import API_disk


def test_connect(url, headers, user):
    query = API_disk()
    response = (query.get_query_json(url, headers))
    assert response["user"] == user


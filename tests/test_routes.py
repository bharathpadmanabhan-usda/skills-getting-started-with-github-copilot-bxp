def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_seeded_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()

    assert "Programming Class" in data
    assert "Chess Club" in data
    assert data["Programming Class"]["participants"] == [
        "emma@mergington.edu",
        "sophia@mergington.edu",
    ]

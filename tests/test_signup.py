def test_signup_success_adds_participant(client):
    email = "newstudent@mergington.edu"

    response = client.post("/activities/Programming Class/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Programming Class"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Programming Class"]["participants"]
    assert email in participants


def test_signup_fails_when_activity_not_found(client):
    response = client.post("/activities/Unknown Club/signup", params={"email": "a@mergington.edu"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_fails_when_already_signed_up(client):
    response = client.post(
        "/activities/Programming Class/signup",
        params={"email": "emma@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}


def test_signup_fails_when_activity_is_full(client):
    response = client.post("/activities/Chess Club/signup", params={"email": "extra@mergington.edu"})

    assert response.status_code == 400
    assert response.json() == {"detail": "Activity is full"}

def test_unregister_success_removes_participant(client):
    email = "emma@mergington.edu"

    response = client.delete(
        "/activities/Programming Class/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from Programming Class"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Programming Class"]["participants"]
    assert email not in participants


def test_unregister_fails_when_activity_not_found(client):
    response = client.delete(
        "/activities/Unknown Club/participants",
        params={"email": "a@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_fails_when_participant_not_found(client):
    response = client.delete(
        "/activities/Programming Class/participants",
        params={"email": "missing@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}

from unittest.mock import patch, MagicMock


@patch("controllers.user_controller.RepositoryFactory")
def test_user_not_found_returns_404(mock_factory, client):
    mock_repo = MagicMock()
    mock_repo.get_by_id.return_value = None
    mock_factory.get_repository.return_value = mock_repo
    response = client.get("/users/999")
    assert response.status_code == 404
    assert b"User not found" in response.data


@patch("controllers.user_controller.RepositoryFactory")
def test_repository_exception_handled(mock_factory, client):
    mock_repo = MagicMock()
    mock_repo.get_all.side_effect = Exception("Database failed")
    mock_factory.get_repository.return_value = mock_repo
    response = client.get("/users/")
    assert response.status_code == 500
    assert b"Internal Server Error" in response.data

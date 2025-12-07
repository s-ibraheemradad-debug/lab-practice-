from unittest.mock import patch, MagicMock
from models.user import User


@patch("controllers.user_controller.RepositoryFactory")
def test_user_list_route(mock_factory, client):
    mock_repo = MagicMock()
    mock_repo.get_all.return_value = [User(1, "Test", "t@t.com")]
    mock_factory.get_repository.return_value = mock_repo
    response = client.get("/users/")
    assert response.status_code == 200
    assert b"Test" in response.data

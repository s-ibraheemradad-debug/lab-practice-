from unittest.mock import patch
from repositories.user_repository import UserRepository


@patch("core.file_singleton.FileManager.read_csv")
def test_get_all_users_csv(mock_read):
    mock_read.return_value = [
        {"id": "1", "name": "Sara", "email": "s@s.com"}
    ]
    repo = UserRepository()
    users = repo.get_all()
    assert len(users) == 1
    assert users[0].name == "Sara"


@patch("core.file_singleton.FileManager.read_csv")
def test_get_by_id_csv(mock_read):
    mock_read.return_value = [
        {"id": "2", "name": "Bob", "email": "b@b.com"}
    ]
    repo = UserRepository()
    u = repo.get_by_id(2)
    assert u is not None
    assert u.email == "b@b.com"

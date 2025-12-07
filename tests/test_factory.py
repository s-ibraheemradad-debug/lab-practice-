import pytest
from repositories.repository_factory import RepositoryFactory
from repositories.user_repository import UserRepository


def test_factory_returns_user_repo():
    repo = RepositoryFactory.get_repository("user")
    assert isinstance(repo, UserRepository)


def test_factory_invalid_type():
    with pytest.raises(ValueError):
        RepositoryFactory.get_repository("unknown")

from lib.user_repository import UserRepository
from lib.user import User


def test_all(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result == [
        User(1, "tariqali87b@gmail.com", "tariq"),
        User(2, "yusuf@gmail.com", "yusuf")
    ]

def test_find(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.find(2)
    assert result == User(2, "yusuf@gmail.com", "yusuf")

def test_create(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = UserRepository(db_connection)
    user = User(None, "nadira@gmail.com", "nadira")
    repository.create(user) is None
    assert repository.all() == [
        User(1, "tariqali87b@gmail.com", "tariq"),
        User(2, "yusuf@gmail.com", "yusuf"),
        User(3, "nadira@gmail.com", "nadira")
    ]

def test_delete(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = UserRepository(db_connection)
    assert repository.delete(1) is None
    assert repository.all() == [
        User(2, "yusuf@gmail.com", "yusuf")

    ]



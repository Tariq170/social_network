from lib.post_repository import PostRepository
from lib.post import Post


def test_all(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Post(1, 'title one', 'content one', 1, 1),
        Post(2, 'title two', 'content two', 1, 2)
    ]


def test_find(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.find(2)
    assert result == Post(2, 'title two', 'content two', 1, 2)



def test_create(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = PostRepository(db_connection)
    post = Post(None, 'title three', 'content three', 1, 2)

    repository.create(post) is None
    assert repository.all() == [
        Post(1, 'title one', 'content one', 1, 1),
        Post(2, 'title two', 'content two', 1, 2),
        Post(3, 'title three', 'content three', 1, 2)
        
    ]



def test_delete(db_connection):
    db_connection.seed("seed/social_network.sql")
    repository = PostRepository(db_connection)
    assert repository.delete(1) is None
    assert repository.all() == [
        Post(2, 'title two', 'content two', 1, 2)

    ]



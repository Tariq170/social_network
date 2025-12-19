from lib.post import Post



def test_contrsucts():
    post = Post(1, "My Title", "My Content", 1, 1)
    assert post.id == 1
    assert post.title == "My Title"
    assert post.content == "My Content"
    assert post.views == 1
    assert post.user_id == 1


def test_equality():
    post_1 =Post(1, "My Title", "My Content", 1, 1)    
    post_2 =Post(1, "My Title", "My Content", 1, 1) 
    assert post_1 ==post_2

def test_formats():
    post = Post(1, "My Title", "My Content", 1, 1)
    assert str(post) == "Post(1, My Title, My Content 1, 1)"
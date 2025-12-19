from lib.user import User

#constrruct with email and username

def test_contrsucts():
    user = User(1, "My Email", "My Username")
    assert user.id == 1
    assert user.email == "My Email"
    assert user.username == "My Username"

def test_equality():
    user_1 = User(1, "My Username", "My Email")    
    user_2 = User(1, "My Username", "My Email") 
    assert user_1 == user_2

def test_formats():
    user = User(1, "My Username", "My Email")
    assert str(user) == "User(1, My Username, My Email)"
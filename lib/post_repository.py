
from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        return [
            Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])
            for row in rows
        ]    
    
    
    
    def find(self, user_id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s, [user_id]")

        row = rows[0]
        return Post(row["id"], row["title"], row["contents"], row["views"], row["user_id"])
    
    
    
    def create(self, post):
        self._connection.execute(
            "INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)",
            [post.title, post.content, post.views, post.user_id]
        )
        return None
    

    
    def delete(self, user_id):
        self._connection.execute(
            "DELETE FROM posts WHERE id = %s",
            [user_id]
        )

        return None
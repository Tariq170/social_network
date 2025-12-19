DROP TABLE IF EXISTS posts;

DROP TABLE IF EXISTS users;



CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT,
    username TEXT
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    views INT,
    -- The foreign key name is always {other_table_singular}_id
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
);

INSERT INTO users (email, username) VALUES ('tariqali87b@gmail.com', 'tariq');
INSERT INTO users (email, username) VALUES ('yusuf@gmail.com', 'yusuf');

INSERT INTO posts (title, content, views, user_id) VALUES ('title one', 'content one', 1, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('title two', 'content two', 1, 2);


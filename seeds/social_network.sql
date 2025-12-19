DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email text
    username text
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int
    -- The foreign key name is always {other_table_singular}_id
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (email, username) VALUES ('tariqali87b@gmail.com', 'tariq');
INSERT INTO users (email, username) VALUES ('yusuf@gmail.com', 'yusuf');

INSERT INTO posts (title, contents, views, user_id) VALUES ('title one', 'content one', 1, 1);
INSERT INTO posts (title, contents, views, user_id) VALUES ('title two', 'content two', 1, 2);


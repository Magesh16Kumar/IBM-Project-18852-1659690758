DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES (
    "jaeger_2601",
    "c51dcc4e0deaee00fa5af30e29b6e1acbf32fcb3cea8c4b5cdeaecece8e248df439b2da1b834cb67bbafd2fa07d02f49"
);
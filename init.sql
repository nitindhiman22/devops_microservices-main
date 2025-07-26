
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    info TEXT NOT NULL
);

INSERT INTO users (name, info) VALUES
('alice', 'Alice is a data scientist.'),
('bob', 'Bob is a backend developer.'),
('ram', 'Ram is a frontend engineer.')
ON CONFLICT (name) DO NOTHING;


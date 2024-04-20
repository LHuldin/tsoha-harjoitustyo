CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE visitors (
    id SERIAL PRIMARY KEY, 
    time TIMESTAMP
);
CREATE TABLE library (
    id SERIAL PRIMARY KEY,
    type TEXT,
    model TEXT,
    condition TEXT
);
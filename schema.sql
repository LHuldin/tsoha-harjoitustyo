CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE visitors (
    id SERIAL PRIMARY KEY, 
    time TIMESTAMP
);
CREATE TABLE hardware (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    type TEXT,
    model TEXT,
    condition TEXT,
    value INTEGER,
    public BOOLEAN,
    visible BOOLEAN
);
CREATE TABLE software (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    name TEXT,
    mediatype TEXT,
    model TEXT,
    condition TEXT,
    value INTEGER,
    public BOOLEAN,
    visible BOOLEAN
);
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    comment TEXT,
    user_id INTEGER REFERENCES users,
    t_stamp TIMESTAMP
);
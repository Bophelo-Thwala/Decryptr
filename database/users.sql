CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_credits INT DEFAULT 0,
);

INSERT INTO users (username, email, user_password, user_credits) VALUES (
    'john_doe', 'johndoe@gmail.com', 'hashed_password_123', 10
);
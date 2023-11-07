CREATE DATABASE "kentjordan";

CREATE TABLE users(
	id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	email VARCHAR(255),
	password TEXT,
	country VARCHAR(128),
	city VARCHAR(128),
	birth_day DATE
);

CREATE TABLE blogs(
	id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
	title TEXT NOT NULL,
	content TEXT,
	images TEXT[],
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP,
	user_id UUID NOT NULL,
	CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
);
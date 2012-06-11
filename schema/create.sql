CREATE SEQUENCE users_id_seq;

CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY DEFAULT NEXTVAL('users_id_seq'),
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    bio VARCHAR(120) NOT NULL DEFAULT 'No bio',
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);

CREATE SEQUENCE projects_id_seq;
CREATE TABLE projects (
    id INT NOT NULL PRIMARY KEY DEFAULT NEXTVAL('projects_id_seq'),
    name VARCHAR(120) NOT NULL,
    description TEXT,
    created_at TIMESTAMP,
    modified_at TIMESTAMP
);

CREATE TYPE role_enum AS ENUM ('ADMIN', 'MEMBER');

CREATE SEQUENCE user_project_rel_id_seq;
CREATE TABLE user_project_rel (
    id INT NOT NULL PRIMARY KEY DEFAULT NEXTVAL('user_project_rel_id_seq'),
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    role role_enum,
    created_at TIMESTAMP,
    modified_at TIMESTAMP,
    UNIQUE (user_id, project_id)
);

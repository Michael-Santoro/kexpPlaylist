CREATE TABLE IF NOT EXISTS hosts (
                id INT PRIMARY KEY,
                uri VARCHAR(255) UNIQUE NOT NULL,
                name VARCHAR(100) UNIQUE NOT NULL,
                image_uri VARCHAR(255),
                thumbnail_uri VARCHAR(255),
                is_active BOOL NOT NULL
            );
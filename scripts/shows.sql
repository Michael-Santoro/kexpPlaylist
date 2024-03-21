CREATE TABLE IF NOT EXISTS shows (
                id INT PRIMARY KEY,
                uri VARCHAR(255) UNIQUE NOT NULL,
                program INT NOT NULL,
                program_uri VARCHAR(255),
                hosts VARVCHAR(2550),
                program_name VARCHAR(255),
                program_tags VARCHAR(255),
                tagline TEXT,
                image_uri VARCHAR(255),
                start_time TIMESTAMP NOT NUll,
            );
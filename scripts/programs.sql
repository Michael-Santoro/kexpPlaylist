CREATE TABLE IF NOT EXISTS programs (
                id INT PRIMARY KEY,
                uri VARCHAR(255) UNIQUE NOT NULL,
                name VARCHAR(100) UNIQUE NOT NULL,
                description TEXT NOT NULL,
                tags VARCHAR(255),
                is_active BOOL NOT NULL
            );
CREATE TABLE IF NOT EXISTS plays (
                id INT PRIMARY KEY,
                uri VARCHAR(255) UNIQUE NOT NULL,
                airdate TIMESTAMP NOT NUll,
                show INT NOT NULL,
                song VARCHAR(255) NOT NULL,
                track_id VARCHAR(255) NOT NULL,
                recording_id VARCHAR(255) NOT NULL,
                artist VARCHAR(255) NOT NULL,
                album VARCHAR(255) NOT NULL,
                release_id VARCHAR(255),
                release_group_id VARCHAR(255),
                release_date VARCHAR(255),
                is_local BOOL,
                is_request BOOL,
                is_live BOOL,
                comment TEXT,
            );
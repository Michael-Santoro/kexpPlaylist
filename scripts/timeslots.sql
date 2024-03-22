CREATE TABLE IF NOT EXISTS timeslots (
                id INT PRIMARY KEY,
                uri VARCHAR(255) UNIQUE NOT NULL,
                program INT NOT NULL,
                program_uri VARCHAR(255),
                program_name VARCHAR(255),
                program_tags VARCHAR(255),
                weekday INT,
                start_date DATE,
                end_date TIME,
                start_time TIME,
                end_time TIME,
                duration TIME
            );
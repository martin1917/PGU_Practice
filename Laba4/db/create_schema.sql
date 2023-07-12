CREATE TABLE IF NOT EXISTS subject(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(128) NOT NULL,
    count_lectures INTEGER NOT NULL,
    count_practices INTEGER NOT NULL,
    there_is_coursework INTEGER NOT NULL DEFAULT 0 CHECK(there_is_coursework = 0 OR there_is_coursework = 1),
    there_is_selfwork INTEGER NOT NULL DEFAULT 0 CHECK(there_is_selfwork = 0 OR there_is_selfwork = 1)
);

CREATE TABLE IF NOT EXISTS teacher(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FIO NVARCHAR(128) NOT NULL,
    subject_id INTEGER NOT NULL,

    FOREIGN KEY (subject_id) REFERENCES subject (id) ON UPDATE CASCADE ON DELETE CASCADE
);
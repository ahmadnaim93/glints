CREATE TABLE Student(
    s_id VARCHAR(20),
    s_name VARCHAR(20) NOT NULL DEFAULT '',
    s_birth VARCHAR(20) NOT NULL DEFAULT '',
    s_sex VARCHAR(10) NOT NULL DEFAULT '',
    s_insert_dt timestamp NOT NULL,
    PRIMARY KEY(s_id)
);

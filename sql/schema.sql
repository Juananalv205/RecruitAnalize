CREATE TABLE IF NOT EXISTS `staging_candidates` (
    id int(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    application_date DATE,
    country VARCHAR(255),
    yoe INT,
    seniority VARCHAR(255),
    technology VARCHAR(255),
    code_challenge_score INT,
    technical_interview_score INT,
    Primary Key (id)
);


CREATE TABLE IF NOT EXISTS `candidates` (
    id int(11) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    application_date DATE,
    country VARCHAR(255),
    yoe INT,
    seniority VARCHAR(255),
    technology VARCHAR(255),
    code_challenge_score INT,
    technical_interview_score INT,
    Primary Key (id)
);
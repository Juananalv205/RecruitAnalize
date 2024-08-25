INSERT INTO Candidates (
    first_name, 
    last_name, 
    email, 
    application_date, 
    country, 
    yoe, 
    seniority, 
    technology, 
    code_challenge_score, 
    technical_interview_score
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
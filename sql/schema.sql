CREATE TABLE `Candidates` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `application_date` date NOT NULL,
  `country` int(100) NOT NULL,
  `yoe` int(11) NOT NULL,
  `seniority` varchar(100) NOT NULL,
  `technology` varchar(100) NOT NULL,
  `code_challenge_score` int(11) NOT NULL,
  `technical_interview_score` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

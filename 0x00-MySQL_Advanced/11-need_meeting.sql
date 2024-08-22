-- A script that creates a view named need_meeting that lists the names of students who have a score less than 80 and have not had a meeting in the last month.
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT names
FROM students
WHERE scores < 80
(last_meeting IS NULL
OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
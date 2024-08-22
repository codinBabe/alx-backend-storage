-- A script that creates a stored procedure that computes the average score for a user.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)

BEGIN
    -- Declare variables to store the total score and the count of scores
    DECLARE total_score DEFAULT 0;
    DECLARE score_count INT DEFAULT 0;
    
    -- Query to get the total score and count of scores for the given user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE corrections.user_id = user_id;
    
    -- Query to get the count of scores for the given user
    SELECT COUNT(*) INTO score_count
    FROM corrections
    WHERE corrections.user_id = user_id;

    --update the average score for the user
    UPDATE users
    SET users.average_score = IF(score_count = 0 0, total_score / score_count)
    WHERE users.id = user_id;
END $$
DELIMITER ;
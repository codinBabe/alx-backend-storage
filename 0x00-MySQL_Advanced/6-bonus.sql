-- A script that creates a stored procedure that adds a bonus to a user for a project.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
  BEGIN
    DECLARE project_id INT DEFAULT 0;
    DECLARE project_count INT DEFAULT 0;

    -- Check if the project exists, if not, create it
    SELECT COUNT(id) INTO project_count 
    FROM projects 
    WHERE name = project_name;
    IF project_count = 0 THEN
      INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Get the project ID
    SELECT id INTO project_id 
    FROM projects 
    WHERE name = project_name;
    
    -- Insert the new correction into the corrections table
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
  END $$
DELIMITER ;

-- A script that creates a trigger that sets the valid_email column to 0 if the email column is updated.
DROP TRIGGER IF EXISTS reset_email_valid;
DELIMITER $$
CREATE TRIGGER reset_email_valid
BEFORE UPDATE ON users
    FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = NEW.valid_email;
    END IF;
END $$
DELIMITER ;
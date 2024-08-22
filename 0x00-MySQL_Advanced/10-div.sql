-- A script that creates a function that safely divides two numbers.
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURN FLOAT DETERMINISTIC
BEGIN
DECLARE ret FLOAT DEFAULT 0;
    IF b <> 0 THEN
    SET ret = a / b;
    END IF;
    RETURN ret;
END $$
DELIMITER ;
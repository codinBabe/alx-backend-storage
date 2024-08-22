-- A script to create the store database for the given database schema
DROP TRIGGER IF EXISTS decrease_quantity;
DELIMITER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
    FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE id = NEW.item_id;
END $$
DELIMITER ;

-- A script that creates an index on the first character of the name column and the score column in the names table.
CREATE INDEX index_name_first_score ON names (name(1), score);
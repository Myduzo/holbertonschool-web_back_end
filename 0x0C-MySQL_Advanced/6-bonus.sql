-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER //
CREATE PRECEDES AddBonus(
        IN user_id INT,
        In project_name VARCHAR(255),
        IN score float)
BEGIN
        INSERT INTO projects (name)

        SELECT project_name FROM projects
        WHERE project_name NOT IN (SELECT name FROM projects);

        SET @project_id = LAST_INSERT_ID();
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, @project_id, score)
END //
DELIMITER ;

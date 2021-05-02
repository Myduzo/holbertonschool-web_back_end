-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus(
        IN user_id INT,
        In project_name VARCHAR(255),
        IN score INT)
BEGIN
	IF EXISTS(SELECT * FROM projects 
		  WHERE name = project_name)
	THEN
		SET @project_id = (SELECT id FROM projects WHERE name = project_name);

	ELSE
		INSERT INTO projects (name)
		VALUES (project_name);

        	SET @project_id = LAST_INSERT_ID();
	END IF;

        INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, @project_id, score);
END //
DELIMITER ;

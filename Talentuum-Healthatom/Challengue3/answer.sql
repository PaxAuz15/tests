CREATE TABLE IF NOT EXISTS `persons` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`id`)
)

INSERT INTO persons (id, nombre) VALUES (1,'Luis Auz'),(2,'Antonio García'),(3,'Mariuxi Casquete'),(4,'Brayan Cantos'),(5,'Brangy Castro'),(6,'Zully Cedeño'),(7,'Karla Palma'),(8,'Darwin Morocho'),(9,'Heidy Cedeño'),(10,'Yessica Moreira')


ALTER TABLE avistamientos
  ADD COLUMN id_person INT NOT NULL DEFAULT(1),
  ADD FOREIGN KEY fk_id_person(id_person) REFERENCES persons(id) ON DELETE RESTRICT ON UPDATE CASCADE;

UPDATE avistamientos SET id_person = FLOOR( 1 + RAND( ) *10 );

ALTER TABLE movimientos_recursos
  ADD COLUMN id_person INT NOT NULL DEFAULT(1),
  ADD FOREIGN KEY fk_id_person(id_person) REFERENCES persons(id) ON DELETE RESTRICT ON UPDATE CASCADE;

UPDATE movimientos_recursos SET id_person = FLOOR( 1 + RAND( ) *10 );

ALTER TABLE muertes
  ADD COLUMN id_person INT,
  ADD FOREIGN KEY fk_id_person(id_person) REFERENCES persons(id) ON DELETE RESTRICT ON UPDATE CASCADE;

UPDATE muertes SET id_person = FLOOR( 1 + RAND( ) *10 ) WHERE causa != "Desconocida" AND causa != "Accidente";


SELECT persons.nombre, SUM(muertes.id_person) as ejecuciones
FROM persons
JOIN muertes
ON persons.id = muertes.id_person
WHERE YEAR(muertes.fecha) = 2020
GROUP BY persons.id
ORDER BY ejecuciones DESC
LIMIT 1;


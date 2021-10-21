-- FIRST QUESTION
SELECT titanes.nombre,titanes.altura
FROM   titanes
       JOIN muertes
       ON titanes.id = muertes.id_titan
WHERE  muertes.causa = 'Batallón 1'
ORDER BY titanes.altura DESC
LIMIT 1;

-- SECOND QUESTION
SELECT titanes.id,titanes.nombre, titanes.altura,avistamientos.fecha 
FROM titanes
    LEFT JOIN muertes
    ON titanes.id = muertes.id_titan
    JOIN avistamientos
    ON titanes.id = avistamientos.id_titan
WHERE muertes.id_titan IS NULL
ORDER BY titanes.altura DESC;

-- THIRD QUESTION
SELECT *
FROM titanes
WHERE titanes.id
IN (
    SELECT avistamientos.id_titan
    FROM avistamientos
    GROUP BY avistamientos.id_titan
    HAVING COUNT(*)>1
    )

-- FOURTH QUESTION
SELECT recursos.nombre as recurso, SUM(movimientos_recursos.cantidad) as cantidad,recursos.unidad
FROM recursos
JOIN movimientos_recursos
ON movimientos_recursos.id_recurso = recursos.id
JOIN muertes
ON muertes.id = movimientos_recursos.id_muerte
JOIN titanes
ON titanes.id = muertes.id_titan
WHERE titanes.altura <= 5
GROUP BY recursos.id

-- FIFTH QUESTION
SELECT titanes.id,titanes.nombre
FROM titanes
JOIN muertes
ON muertes.id_titan = titanes.id
JOIN avistamientos
ON avistamientos.id_titan = titanes.id
WHERE avistamientos.fecha > muertes.fecha
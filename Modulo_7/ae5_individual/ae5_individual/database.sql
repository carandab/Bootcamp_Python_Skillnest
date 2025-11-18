-- Active: 1755651853873@@127.0.0.1@3306@m7_ae5_individual
CREATE DATABASE IF NOT EXISTS m7_ae5_individual;

USE m7_ae5_individual;



/* === Procedimientos Almacenados === */

/* Obtener todos los productos con precio mayor o igual al especificado */
DELIMITER //

CREATE PROCEDURE obtener_productos_por_precio(IN precio_minimo DECIMAL(5,2))
BEGIN
    SELECT * FROM registros_ORM_producto WHERE precio >= precio_minimo;
END //

DELIMITER ;


/* Obtener estadísticas generales de los productos */
DELIMITER //

CREATE PROCEDURE estadisticas_productos()
BEGIN
    SELECT 
        COUNT(*) as total_productos,
        SUM(CASE WHEN disponible = 1 THEN 1 ELSE 0 END) as total_disponibles,
        AVG(precio) as precio_promedio,
        MIN(precio) as precio_minimo,
        MAX(precio) as precio_maximo
    FROM registros_ORM_producto;
END //

DELIMITER ;

/* Actualizar precios con un porcentaje, opcionalmente solo disponibles */

DELIMITER //

CREATE PROCEDURE actualizar_precios(
    IN porcentaje DECIMAL(5,2),
    IN solo_disponibles BOOLEAN
)
BEGIN
    IF solo_disponibles THEN
        UPDATE registros_ORM_producto 
        SET precio = precio * (1 + porcentaje / 100)
        WHERE disponible = 1;
    ELSE
        UPDATE registros_ORM_producto 
        SET precio = precio * (1 + porcentaje / 100);
    END IF;
    
    SELECT ROW_COUNT() as filas_actualizadas;
END //

DELIMITER ;


/* Buscar productos por término en el nombre y precio máximo */

DELIMITER //

CREATE PROCEDURE buscar_productos(
    IN termino_busqueda VARCHAR(100),
    IN precio_max DECIMAL(5,2)
)
BEGIN
    SELECT * FROM registros_ORM_producto
    WHERE nombre LIKE CONCAT('%', termino_busqueda, '%')
    AND precio <= precio_max
    ORDER BY nombre;
END //

DELIMITER ;

/* Contar productos por su disponibilidad usando OUT parameters */
DELIMITER //

CREATE PROCEDURE contar_por_disponibilidad(
    OUT total INT,
    OUT disponibles INT,
    OUT no_disponibles INT
)
BEGIN
    SELECT COUNT(*) INTO total FROM registros_ORM_producto;
    SELECT COUNT(*) INTO disponibles FROM registros_ORM_producto WHERE disponible = 1;
    SELECT COUNT(*) INTO no_disponibles FROM registros_ORM_producto WHERE disponible = 0;
END //

DELIMITER ;


/* Obtener productos en un rango de precios especificado */

DELIMITER //

CREATE PROCEDURE productos_por_rango_precio(
    IN precio_min DECIMAL(5,2),
    IN precio_max DECIMAL(5,2)
)
BEGIN
    SELECT 
        id,
        nombre,
        precio,
        CASE 
            WHEN disponible = 1 THEN 'Disponible'
            ELSE 'No disponible'
        END as estado
    FROM registros_ORM_producto
    WHERE precio BETWEEN precio_min AND precio_max
    ORDER BY precio ASC;
END //

DELIMITER ;

/* Verificacion */

SELECT 
    ROUTINE_NAME as 'Procedimiento Creado',
    PARAM_LIST as 'Parámetros'
FROM information_schema.ROUTINES
WHERE ROUTINE_SCHEMA = 'm7_ae5_individual'
AND ROUTINE_TYPE = 'PROCEDURE'
ORDER BY ROUTINE_NAME;

SELECT 'Base de datos y procedimientos almacenados creados exitosamente' as 'Estado';
CREATE DATABASE IF NOT EXISTS ae3_individual;
USE ae3_individual;


-- Creacion de tablas
CREATE TABLE clientes (
  id_clientes INT     NOT NULL AUTO_INCREMENT,
  nombre      VARCHAR(100) NOT NULL,
  direccion   VARCHAR(100) NOT NULL,
  telefono    VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_clientes)
);

CREATE TABLE pedidos (
  id_pedidos  INT     NOT NULL AUTO_INCREMENT,
  id_clientes INT     NOT NULL,
  fecha       DATE    NOT NULL,
  total       DECIMAL NOT NULL,
  PRIMARY KEY (id_pedidos)
);

ALTER TABLE pedidos
  ADD CONSTRAINT FK_clientes_TO_pedidos
    FOREIGN KEY (id_clientes)
    REFERENCES clientes (id_clientes)



-- Datos
INSERT INTO clientes (nombre, direccion, telefono) VALUES

('Juan Pérez', 'Matucana 1500, Santiago', '955551234'),
('María García', 'Calle Prat 250, Valparaíso', '966665678'),
('Carlos Rodríguez', 'San Martín 890, Viña del Mar', '977779012'),
('Ana Torres', 'Manuel Rodríguez 400, Concepción', '988883456'),
('Pedro López', 'Avenida Balmaceda 1200, La Serena', '999997890');


INSERT INTO pedidos (id_clientes, fecha, total) VALUES

(1, '2025-08-25', 55.75),
(3, '2025-08-24', 120.50),
(1, '2025-08-23', 30.00),
(2, '2025-08-22', 85.25),
(5, '2025-08-21', 200.00),
(1, '2025-08-20', 45.00),
(4, '2025-08-19', 150.99),
(3, '2025-08-18', 75.80),
(2, '2025-08-17', 25.50),
(1, '2025-08-16', 90.00);


SELECT c.*, p.id_pedidos, p.fecha, p.total
FROM clientes AS c
INNER JOIN pedidos AS p ON c.id_clientes = p.id_clientes;

SELECT c.nombre, pedidos.*
FROM clientes AS c
LEFT JOIN pedidos ON c.id_clientes = pedidos.id_clientes
WHERE c.id_clientes = 1

SELECT c.nombre, COUNT(p.id_pedidos) AS cantidad_pedidos
FROM clientes AS c
LEFT JOIN pedidos AS p ON c.id_clientes = p.id_clientes
GROUP BY c.id_clientes
ORDER BY cantidad_pedidos DESC;

UPDATE clientes
SET direccion = 'Calle Prat 2500, Valparaíso' WHERE id_clientes = 2

DELETE FROM pedidos
WHERE id_clientes = 5;
DELETE FROM clientes
WHERE id_clientes = 5;

SELECT c.nombre, COUNT(p.id_pedidos) AS cantidad_pedidos
FROM clientes AS c
LEFT JOIN pedidos AS p ON c.id_clientes = p.id_clientes
GROUP BY c.id_clientes
ORDER BY cantidad_pedidos DESC
LIMIT 3;

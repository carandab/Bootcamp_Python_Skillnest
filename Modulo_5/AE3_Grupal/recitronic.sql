CREATE DATABASE IF NOT EXISTS recitronic;

USE recitronic;

-- TABLAS
CREATE TABLE clientes
(
  id_cliente INT     NOT NULL AUTO_INCREMENT,
  nombre     VARCHAR(100) NOT NULL,
  telefono   VARCHAR(20) NOT NULL,
  direccion  VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_cliente)
);

CREATE TABLE articulos
(
  id_articulo   INT     NOT NULL AUTO_INCREMENT,
  id_cliente    INT     NOT NULL,
  tipo_articulo VARCHAR(100) NOT NULL,
  estado        VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_articulo)
);

CREATE TABLE citas
(
  id_cita    INT      NOT NULL AUTO_INCREMENT,
  id_cliente INT      NOT NULL,
  fecha_hora DATETIME NOT NULL,
  PRIMARY KEY (id_cita)
);


CREATE TABLE pagos
(
  id_pago    INT      NOT NULL AUTO_INCREMENT,
  id_cliente INT      NOT NULL,
  monto      DECIMAL  NOT NULL,
  fecha_pago DATETIME NULL    ,
  PRIMARY KEY (id_pago)
);

ALTER TABLE articulos
  ADD CONSTRAINT FK_clientes_TO_articulos
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_cliente);

ALTER TABLE citas
  ADD CONSTRAINT FK_clientes_TO_citas
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_cliente);

ALTER TABLE pagos
  ADD CONSTRAINT FK_clientes_TO_pagos
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_cliente);

-- DATOS
INSERT INTO clientes (id_cliente, nombre, telefono, direccion) VALUES

(1, 'Juan Perez', '9-12345678', 'Calle Falsa 123'),
(2, 'Maria Gomez', '8-56781234', 'Avenida Siempre Viva 742'),
(3, 'Carlos Sanchez', '9-87654321', 'Boulevard de los Sueños Rotos 456'),
(4, 'Ana Martinez', '7-43218765', 'Calle Luna 789'),
(5, 'Luis Rodriguez', '6-34567890', 'Avenida del Sol 321'),
(6, 'Sofia Fernandez', '5-98765432', 'Calle Estrella 654'),
(7, 'Miguel Torres', '4-12349876', 'Avenida de la Paz 987'),
(8, 'Laura Ramirez', '3-56789012', 'Boulevard Central 159'),
(9, 'Diego Flores', '2-34561234', 'Calle Jardín 753'),
(10, 'Elena Morales', '1-67890123', 'Avenida Libertad 852'),
(11, 'Javier Jimenez', '9-23456789', 'Calle Primavera 951'),
(12, 'Isabel Castro', '8-34567890', 'Avenida Otoño 357'),
(13, 'Fernando Ruiz', '7-45678901', 'Boulevard Invierno 258'),
(14, 'Marta Ortiz', '6-56789012', 'Calle Verano 654'),
(15, 'Ricardo Vega', '5-67890123', 'Avenida Montaña 753'),
(16, 'Patricia Silva', '4-78901234', 'Calle Río 852'),
(17, 'Andrés Herrera', '3-89012345', 'Avenida Playa 951'),
(18, 'Gabriela Medina', '2-90123456', 'Boulevard Campo 159'),
(19, 'Santiago Rojas', '1-01234567', 'Calle Bosque 357'),
(20, 'Valentina Cruz', '9-12345670', 'Avenida Cielo 258');

-- ARTICULOS
INSERT INTO articulos (id_articulo, id_cliente, tipo_articulo, estado) VALUES

(1, 1, 'Laptop', 'En preparación'),
(2, 2, 'Smartphone', 'Reciclado'),
(3, 3, 'Tablet', 'Pendiente'),
(4, 4, 'Desktop', 'Reciclado'),
(5, 5, 'Smartwatch', 'En preparación'),
(6, 6, 'Laptop', 'Reciclado'),
(7, 7, 'Smartphone', 'Pendiente'),
(8, 8, 'Tablet', 'Reciclado'),
(9, 9, 'Desktop', 'En preparación'),
(10, 10, 'Smartwatch', 'Reciclado'),
(11, 11, 'Laptop', 'Pendiente'),
(12, 12, 'Smartphone', 'Reciclado'),
(13, 13, 'Tablet', 'En preparación'),
(14, 14, 'Desktop', 'Reciclado'),
(15, 15, 'Smartwatch', 'Pendiente'),
(16, 16, 'Laptop', 'Reciclado'),
(17, 17, 'Smartphone', 'En preparación'),
(18, 18, 'Tablet', 'Reciclado'),
(19, 19, 'Desktop', 'Pendiente'),
(20, 20, 'Smartwatch', 'Reciclado'),
(21, 1, 'Smartphone', 'En preparación'),
(22, 4, 'Tablet', 'Reciclado'),
(23, 3, 'Desktop', 'Pendiente'),
(24, 2, 'Smartwatch', 'Reciclado'),
(25, 5, 'Laptop', 'En preparación'),
(26, 6, 'Smartphone', 'Reciclado'),
(27, 1, 'Tablet', 'Reciclado'),
(28, 8, 'Desktop', 'Reciclado'),
(29, 7, 'Smartwatch', 'En preparación'),
(30, 10, 'Laptop', 'Reciclado');

-- CITAS
 INSERT INTO citas (id_cliente, fecha_hora) VALUES

(1, '2025-08-25 09:00:00'),
(2, '2025-08-25 10:30:00'),
(3, '2025-08-25 11:45:00'),
(4, '2025-08-26 14:00:00'),
(5, '2025-08-26 15:30:00'),
(6, '2025-08-26 16:45:00'),
(7, '2025-08-27 09:15:00'),
(8, '2025-08-27 10:00:00'),
(9, '2025-08-27 11:30:00'),
(10, '2025-08-28 13:00:00'),
(11, '2025-08-28 14:30:00'),
(12, '2025-08-28 15:45:00'),
(13, '2025-08-29 09:00:00'),
(14, '2025-08-29 10:30:00'),
(15, '2025-08-29 12:00:00'),
(16, '2025-08-29 14:00:00'),
(17, '2025-08-30 15:30:00'),
(18, '2025-08-30 16:00:00'),
(19, '2025-08-30 17:15:00'),
(20, '2025-08-30 18:00:00'),
(1, '2025-09-01 09:30:00'),
(1, '2025-09-02 11:00:00'),
(2, '2025-09-02 14:00:00'),
(3, '2025-09-03 10:00:00'),
(3, '2025-09-03 12:00:00'),
(4, '2025-09-04 15:00:00'),
(5, '2025-09-05 09:00:00'),
(6, '2025-09-05 10:00:00'),
(6, '2025-09-06 14:00:00'),
(7, '2025-09-06 15:00:00'),
(8, '2025-09-07 11:00:00'),
(9, '2025-09-07 12:30:00'),
(10, '2025-09-08 14:00:00'),
(11, '2025-09-08 16:00:00'),
(12, '2025-09-09 09:00:00'),
(13, '2025-09-09 10:00:00'),
(14, '2025-09-10 11:00:00'),
(15, '2025-09-10 12:30:00'),
(16, '2025-09-11 14:00:00'),
(17, '2025-09-12 10:00:00');

--PAGOS
INSERT INTO pagos (id_pago, id_cliente, monto, fecha_pago) VALUES

(1, 1, 100.00, '2025-08-26 10:00:00'),
(2, 2, 150.00, '2025-08-27 11:30:00'),
(3, 3, 200.00, '2025-08-28 14:15:00'),
(4, 4, 250.00, '2025-08-29 09:45:00'),
(5, 5, 300.00, '2025-08-30 16:20:00'),
(6, 6, 120.00, '2025-09-01 10:10:00'),
(7, 7, 180.00, '2025-09-02 13:50:00'),
(8, 8, 220.00, '2025-09-03 15:30:00'),
(9, 9, 270.00, '2025-09-04 11:25:00'),
(10, 10, 320.00, '2025-09-05 14:40:00'),
(11, 11, 130.00, '2025-09-06 09:55:00'),
(12, 12, 170.00, '2025-09-07 12:15:00'),
(13, 13, 210.00, '2025-09-08 16:05:00'),
(14, 14, 260.00, '2025-09-09 10:35:00'),
(15, 15, 310.00, '2025-09-10 13:45:00'),
(16, 16, 140.00, '2025-09-11 11:20:00'),
(17, 17, 190.00, '2025-09-12 15:55:00'),
(18, 18, 230.00, '2025-09-13 14:30:00'),
(19, 19, 280.00, '2025-09-14 10:50:00'),
(20, 20, 330.00, '2025-09-15 12:40:00'),
(21, 1, 110.00, '2025-09-16 09:30:00'),
(22, 2, 160.00, '2025-09-17 11:15:00'),
(23, 3, 210.00, '2025-09-18 13:55:00'),
(24, 4, 260.00, '2025-09-19 15:40:00'),
(25, 5, 310.00, '2025-09-20 10:05:00'),
(26, 6, 130.00, '2025-09-21 12:25:00'),
(27, 7, 180.00, '2025-09-22 14:50:00'),
(28, 8, 230.00, '2025-09-23 16:10:00'),
(29, 9, 280.00, '2025-09-24 11:35:00'),
(30, 10, 330.00, '2025-09-25 13:15:00');

-- UPDATE

UPDATE clientes SET telefono = '9-99999999' WHERE id_cliente = 1;
UPDATE articulos SET estado = 'Reparado' WHERE id_articulo = 1;
UPDATE pagos SET monto = 150.00 WHERE id_pago = 1;
UPDATE citas SET fecha_hora = '2025-08-26 09:00:00' WHERE id_cita = 1;
UPDATE clientes SET direccion = 'Calle Nueva 456' WHERE id_cliente = 2;
UPDATE articulos SET tipo_articulo = 'Smartphone' WHERE id_articulo = 2;
UPDATE pagos SET fecha_pago = '2025-08-28 10:00:00  ' WHERE id_pago = 2;
UPDATE citas SET fecha_hora = '2025-08-27 10:30:00' WHERE id_cita = 2;


-- DELETE 
DELETE FROM clientes WHERE id_cliente = 20;
DELETE FROM articulos WHERE id_articulo = 30;

-- TRANSACCIONES

START TRANSACTION ;

UPDATE 




-- Active: 1755731998654@@127.0.0.1@3306@libreria_db
CREATE DATABASE IF NOT EXISTS libreria_db;

USE libreria_db;

-- TABLAS
CREATE TABLE clientes
(
  id_cliente        INT          NOT NULL AUTO_INCREMENT,
  nombre_cliente    VARCHAR(100) NOT NULL,
  correo_cliente    VARCHAR(100) NOT NULL,
  telefono_cliente  VARCHAR(15)  NOT NULL,
  direccion_cliente VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_cliente)
);

CREATE TABLE detalles_pedido
(
  id_detalle     INT           NOT NULL AUTO_INCREMENT,
  id_pedido      INT           NOT NULL,
  id_libro       INT           NOT NULL,
  cantidad_libro INT           NOT NULL,
  precio_libro   DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id_detalle)
);

CREATE TABLE libros
(
  id_libro            INT           NOT NULL AUTO_INCREMENT,
  titulo_libro        VARCHAR(225)  NOT NULL,
  autor_libro         VARCHAR(100)  NOT NULL,
  precio_libro        DECIMAL(10,2) NOT NULL,
  cantidad_disponible INT           NOT NULL,
  categoria_libro     VARCHAR(50)   NOT NULL,
  PRIMARY KEY (id_libro)
);

CREATE TABLE pagos
(
  id_pago     INT           NOT NULL AUTO_INCREMENT,
  id_pedido   INT           NOT NULL,
  fecha_pago  DATE          NOT NULL,
  monto_pago  DECIMAL(10,2) NOT NULL,
  metodo_pago VARCHAR(50)   NOT NULL,
  PRIMARY KEY (id_pago)
);

CREATE TABLE pedidos
(
  id_pedido     INT         NOT NULL AUTO_INCREMENT,
  id_cliente    INT         NOT NULL,
  fecha_pedido  DATE        NOT NULL,
  total_pedido  DECIMAL(10,2)    NOT NULL,
  estado_pedido VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_pedido)
);

-- RESTRICCIONES

-- Restricciones clientes

ALTER TABLE clientes
ADD CONSTRAINT CHK_telefono_numeros_longitud
CHECK (LENGTH(telefono_cliente) = 10 AND telefono_cliente NOT LIKE '%[^0-9]%');

-- Alternativa que me dio Gemini, dice que es una herramienta mucho mas poderosa
/*ALTER TABLE clientes
ADD CONSTRAINT CHK_telefono_numeros_longitud
CHECK (telefono_cliente REGEXP '^[0-9]{10}$');
REGEXP es un operador que busca patrones en una cadena (Regular Expression)
^ indica que debe coincidir con el inicio de la cadena, [] conjunto de caracteres que se busca
{} cuantificador que indica la cantidad de veces que se debe repetir el conjunto ,  $ indica que debe coincidir con el final de la cadena*/

ALTER TABLE clientes
ADD CONSTRAINT UQ_correo_cliente UNIQUE (correo_cliente);

-- Restricciones libros

ALTER TABLE libros
ADD CONSTRAINT CHK_cantidad_positiva
CHECK (cantidad_disponible > 0);


-- Restricciones pedidos

ALTER TABLE pedidos
  ADD CONSTRAINT FK_clientes_TO_pedidos
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_cliente)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

ALTER TABLE pedidos
  ADD CONSTRAINT UQ_id_cliente UNIQUE (id_cliente);

-- Restricciones detalles_pedido

ALTER TABLE detalles_pedido
  ADD CONSTRAINT FK_pedidos_TO_detalles_pedido
    FOREIGN KEY (id_pedido)
    REFERENCES pedidos (id_pedido)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

ALTER TABLE detalles_pedido
  ADD CONSTRAINT FK_libros_TO_detalles_pedido
    FOREIGN KEY (id_libro)
    REFERENCES libros (id_libro)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

ALTER TABLE detalles_pedido
  ADD CONSTRAINT UQ_id_libro UNIQUE (id_libro);

-- Restricciones pagos

ALTER TABLE pagos
  ADD CONSTRAINT FK_pedidos_TO_pagos
    FOREIGN KEY (id_pedido)
    REFERENCES pedidos (id_pedido)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Modificaciones 

ALTER TABLE clientes
    MODIFY COLUMN telefono_cliente VARCHAR(20);

ALTER TABLE libros
    MODIFY COLUMN precio_libro DECIMAL(10,3);

ALTER TABLE pagos
    ADD COLUMN fecha_confirmacion DATE AFTER monto_pago;

-- Agregar Datos

INSERT INTO clientes (nombre_cliente, correo_cliente, telefono_cliente, direccion_cliente) VALUES
('Juan Pérez', 'juan.perez@email.com', '5512345678', 'Av. Siempre Viva 123'),
('María García', 'maria.garcia@email.com', '5523456789', 'Calle Falsa 456'),
('Carlos López', 'carlos.lopez@email.com', '5534567890', 'Blvd. de los Sueños 789'),
('Ana Martínez', 'ana.martinez@email.com', '5545678901', 'Paseo de la Luna 101'),
('Luis Torres', 'luis.torres@email.com', '5556789012', 'Vía Láctea 202'),
('Sofía Ramírez', 'sofia.ramirez@email.com', '5567890123', 'Avenida del Sol 303'),
('Pedro Sánchez', 'pedro.sanchez@email.com', '5578901234', 'Camino del Bosque 404'),
('Laura Gómez', 'laura.gomez@email.com', '5589012345', 'Plaza del Viento 505'),
('Diego Fernández', 'diego.fernandez@email.com', '5590123456', 'Río de la Paz 606'),
('Gabriela Díaz', 'gabriela.diaz@email.com', '5511223344', 'Cerro de la Esperanza 707'),
('Ricardo Milla', 'ricardo.milla@email.com', '5522334455', 'Volcán del Silencio 808'),
('Patricia Castro', 'patricia.castro@email.com', '5533445566', 'Lago de la Osa 909'),
('Jorge Vargas', 'jorge.vargas@email.com', '5544556677', 'Estrella Polar 110'),
('Verónica Herrera', 'veronica.herrera@email.com', '5555667788', 'Valle Escondido 220'),
('Arturo Morales', 'arturo.morales@email.com', '5566778899', 'Canto del Pájaro 330'),
('Cristina Ortiz', 'cristina.ortiz@email.com', '5577889900', 'Sendero de las Nubes 440'),
('Roberto Osorio', 'roberto.osorio@email.com', '5588990011', 'Luz de Luna 550'),
('Diana Nuñez', 'diana.nunez@email.com', '5599001122', 'Rocío del Mar 660'),
('Javier Guerrero', 'javier.guerrero@email.com', '5500112233', 'Sol Naciente 770'),
('Mónica Valdés', 'monica.valdes@email.com', '5511003322', 'Puesta del Sol 880');

INSERT INTO libros (titulo_libro, autor_libro, precio_libro, cantidad_disponible, categoria_libro) VALUES
('El Código Da Vinci', 'Dan Brown', '250.00', 100, 'Misterio'),
('Cien Años de Soledad', 'Gabriel García Márquez', '300.50', 50, 'Ficción'),
('1984', 'George Orwell', '150.75', 25, 'Ciencia Ficción'),
('Orgullo y Prejuicio', 'Jane Austen', '180.20', 75, 'Romance'),
('Don Quijote de la Mancha', 'Miguel de Cervantes', '450.00', 30, 'Clásico'),
('El Señor de los Anillos', 'J.R.R. Tolkien', '550.00', 40, 'Fantasía'),
('Crimen y Castigo', 'Fiódor Dostoievski', '210.00', 15, 'Drama'),
('Las Crónicas de Narnia', 'C.S. Lewis', '280.00', 60, 'Fantasía'),
('Rayuela', 'Julio Cortázar', '290.00', 35, 'Ficción'),
('Sapiens', 'Yuval Noah Harari', '320.00', 80, 'Historia');

INSERT INTO pedidos (id_cliente, fecha_pedido, total_pedido, estado_pedido) VALUES
(1, '2023-01-10', 250.00, 'Pendiente'),
(2, '2023-01-15', 300.50, 'Pendiente'),
(3, '2023-01-18', 150.75, 'Pendiente'),
(4, '2023-01-20', 180.20, 'Pendiente'),
(5, '2023-01-22', 450.00, 'Pendiente'),
(6, '2023-01-25', 550.00, 'Pendiente'),
(7, '2023-01-28', 210.00, 'Pendiente'),
(8, '2023-02-01', 280.00, 'Pendiente'),
(9, '2023-02-05', 290.00, 'Pendiente'),
(10, '2023-02-08', 320.00, 'Pendiente'),
(11, '2023-02-10', 250.00, 'Pendiente'),
(12, '2023-02-12', 300.50, 'Pendiente'),
(13, '2023-02-15', 150.75, 'Pendiente'),
(14, '2023-02-18', 180.20, 'Pendiente'),
(15, '2023-02-20', 450.00, 'Pendiente'),
(16, '2023-02-25', 550.00, 'Pendiente'),
(17, '2023-03-01', 210.00, 'Pendiente'),
(18, '2023-03-05', 280.00, 'Pendiente'),
(19, '2023-03-08', 290.00, 'Pendiente'),
(20, '2023-03-10', 320.00, 'Pendiente');

INSERT INTO detalles_pedido (id_pedido, id_libro, cantidad_libro, precio_libro) VALUES
(1, 1, 1, 250.00),
(2, 2, 1, 300.50),
(3, 3, 1, 150.75),
(4, 4, 1, 180.20),
(5, 5, 1, 450.00),
(6, 6, 1, 550.00),
(7, 7, 1, 210.00),
(8, 8, 1, 280.00),
(9, 9, 1, 290.00),
(10, 10, 1, 320.00);

INSERT INTO pagos (id_pedido, fecha_pago, monto_pago, metodo_pago) VALUES
(1, '2023-01-10', 250.00, 'Tarjeta'),
(2, '2023-01-15', 300.50, 'Efectivo'),
(3, '2023-01-18', 150.75, 'Tarjeta'),
(4, '2023-01-20', 180.20, 'Transferencia'),
(5, '2023-01-22', 450.00, 'Tarjeta'),
(6, '2023-01-25', 550.00, 'Efectivo'),
(7, '2023-01-28', 210.00, 'Tarjeta'),
(8, '2023-02-01', 280.00, 'Transferencia'),
(9, '2023-02-05', 290.00, 'Tarjeta'),
(10, '2023-02-08', 320.00, 'Efectivo'),
(11, '2023-02-10', 250.00, 'Transferencia'),
(12, '2023-02-12', 300.50, 'Tarjeta'),
(13, '2023-02-15', 150.75, 'Efectivo'),
(14, '2023-02-18', 180.20, 'Transferencia'),
(15, '2023-02-20', 450.00, 'Tarjeta'),
(16, '2023-02-25', 550.00, 'Efectivo'),
(17, '2023-03-01', 210.00, 'Transferencia'),
(18, '2023-03-05', 280.00, 'Tarjeta'),
(19, '2023-03-08', 290.00, 'Efectivo'),
(20, '2023-03-10', 320.00, 'Tarjeta');

UPDATE pagos
SET fecha_confirmacion = fecha_pago
WHERE fecha_confirmacion IS NULL;

UPDATE pedidos
SET estado_pedido = 'Entregado'
WHERE id_pedido IN (SELECT id_pedido FROM pagos);
-- Verificar que todos los libros estén entregados
START TRANSACTION;
DELETE FROM detalles_pedido 
WHERE id_pedido IN 
(SELECT id_pedido 
 FROM pedidos 
 WHERE estado_pedido = 'Entregado');

-- CONFIRMAR O DESHACER TRANSACCIÓN
COMMIT;
ROLLBACK;
-- Eliminar tabla
DROP TABLE pagos;

-- Truncar tabla
TRUNCATE TABLE pedidos;

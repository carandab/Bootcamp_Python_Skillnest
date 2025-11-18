CREATE DATABASE IF NOT EXISTS evaluacion_portafolioM5;

USE evaluacion_portafolioM5;

-- Tablas

CREATE TABLE clientes
(
  id_cliente INT     NOT NULL AUTO_INCREMENT,
  nombre     VARCHAR(50) NOT NULL,
  direccion  VARCHAR(100) NOT NULL,
  telefono   VARCHAR(14) NULL    ,
  correo     VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_cliente)
);

CREATE TABLE detalles_pedido
(
  id_detalle  INT NOT NULL AUTO_INCREMENT,
  id_producto INT NOT NULL,
  id_pedido   INT NOT NULL,
  cantidad    INT NOT NULL,
  PRIMARY KEY (id_detalle)
);

CREATE TABLE pedidos
(
  id_pedido  INT  NOT NULL AUTO_INCREMENT,
  id_cliente INT  NOT NULL,
  id_metodo  INT  NOT NULL,
  fecha      DATE NOT NULL,
  total      INT  NOT NULL,
  PRIMARY KEY (id_pedido)
);


CREATE TABLE productos
(
  id_producto INT     NOT NULL AUTO_INCREMENT,
  nombre      VARCHAR(50) NOT NULL,
  precio      INT     NOT NULL,
  PRIMARY KEY (id_producto)
);

CREATE TABLE metodos_pago
(
  id_metodo INT     NOT NULL AUTO_INCREMENT,
  nombre    VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_metodo)
);

-- Restricciones

ALTER TABLE clientes
  ADD CONSTRAINT UQ_correo UNIQUE (correo);
ALTER TABLE detalles_pedido
  ADD CONSTRAINT UQ_id_detalle UNIQUE (id_detalle);

ALTER TABLE pedidos
  ADD CONSTRAINT UQ_id_pedido UNIQUE (id_pedido);
  
ALTER TABLE productos
  ADD CONSTRAINT UQ_id_producto UNIQUE (id_producto);

ALTER TABLE metodos_pago
  ADD CONSTRAINT UQ_id_metodo UNIQUE (id_metodo);

ALTER TABLE metodos_pago
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

-- Relaciones

ALTER TABLE pedidos
  ADD CONSTRAINT FK_clientes_TO_pedidos
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_cliente);

ALTER TABLE detalles_pedido
  ADD CONSTRAINT FK_productos_TO_detalles_pedido
    FOREIGN KEY (id_producto)
    REFERENCES productos (id_producto);

ALTER TABLE detalles_pedido
  ADD CONSTRAINT FK_pedidos_TO_detalles_pedido
    FOREIGN KEY (id_pedido)
    REFERENCES pedidos (id_pedido);

ALTER TABLE pedidos
  ADD CONSTRAINT FK_metodos_pago_TO_pedidos
    FOREIGN KEY (id_metodo)
    REFERENCES metodos_pago (id_metodo);


-- Querys y Preguntas


/* -- 2. Utilizar Lenguaje Estructurado de Consultas (SQL) para la obtención de información que satisface los
requerimientos planteados a partir de un modelo de datos dado.
Desarrollar consultas SQL para obtener información específica de las tablas, utilizando cláusulas como
SELECT, WHERE, JOIN, GROUP BY, entre otras.
Ejemplo: Crear una consulta que obtenga todos los pedidos realizados por un cliente específico. */

SELECT p.id_pedido AS pedido_id, p.fecha, p.total
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
WHERE c.nombre = 'Laura Vidal Soto';

SELECT c.nombre, COUNT(p.id_pedido) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nombre;          


/* 3. Utilizar lenguaje de manipulación de datos (DML) para la modificación de los datos existentes en una base
de datos dando solución a un problema planteado.
Implementar consultas de inserción (INSERT), actualización (UPDATE) y eliminación (DELETE) para
modificar los datos dentro de las tablas.
Ejemplo: Crear una consulta que actualice la dirección de un cliente en la base de datos o elimine un
pedido que no fue procesado. */

-- Se actualiza la direccion y el telefono de un cliente
UPDATE clientes
SET
  direccion = 'Avenida del Desierto 500, Antofagasta',
  telefono = '977770000'
WHERE
  id_cliente = '8';

-- Se actualiza el precio de los productos
UPDATE productos
SET
  precio = ROUND(precio * 1.10) -- Redondeamos al entero más cercano
WHERE
  id_producto BETWEEN 1 AND 5;


-- Se eliminan los pedidos con un total menor a 10000
DELETE FROM pedidos
WHERE total < 10000;

-- Se añade un nuevo metodo de pago
INSERT INTO metodos_pago (nombre)
VALUES ('Transferencia Bancaria');

/* 4. Implementar estructuras de datos relacionales utilizando lenguaje de definición de datos (DDL) a partir de
un modelo de datos para la creación y mantención de las definiciones de los objetos de una base de
datos.
Utilizar el lenguaje DDL para crear, modificar y eliminar tablas, índices y otros objetos dentro de una
base de datos.
Ejemplo: Crear una tabla para almacenar información de empleados, con las columnas
correspondientes como nombre, salario y fecha de ingreso. */


-- Se crea una tabla fuera de las relaciones del modelo
CREATE TABLE empleados
(
  id_empleado   INT     NOT NULL AUTO_INCREMENT,
  nombre        VARCHAR(50) NOT NULL,
  salario       INT     NULL    ,
  fecha_ingreso DATE    NULL    ,
  PRIMARY KEY (id_empleado)
);

ALTER TABLE empleados
  ADD CONSTRAINT UQ_id_empleado UNIQUE (id_empleado);

ALTER TABLE empleados
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

-- Lenguaje DDL

ALTER TABLE empleados
ADD COLUMN departamento VARCHAR(50) NOT NULL DEFAULT 'Ventas';

ALTER TABLE empleados
MODIFY COLUMN salario DECIMAL(10, 2) NOT NULL;

ALTER TABLE empleados
DROP CONSTRAINT UQ_nombre;

-- Se elimina la tabla empleados porque no se necesita en este modelo
DROP TABLE empleados;




/* Insercion de datos */


INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES
('Juan Pérez Gómez', 'Av. Libertador 123, Santiago', '987654321', 'juan.perez@email.cl'),
('María Soto Díaz', 'Calle Los Robles 45B, Viña del Mar', '912345678', 'maria.soto@email.cl'),
('Carlos Riquelme Bravo', 'Pasaje Central 90, Concepción', '955554444', 'carlos.riquelme@email.cl'),
('Ana Torres Vega', 'El Golf 300, Las Condes', '966667777', 'ana.torres@email.cl'),
('Pedro Mena Castro', 'Arturo Prat 789, Temuco', '922221111', 'pedro.mena@email.cl'),
('Sofía Leal Rojas', 'Ruta 5 Sur Km 20, Talca', '933330000', 'sofia.leal@email.cl'),
('Andrés Núñez Vera', 'Manuel Montt 550, Providencia', '944449999', 'andres.nunez@email.cl'),
('Laura Vidal Soto', 'Los Carreras 101, Antofagasta', '977778888', 'laura.vidal@email.cl'),
('Jorge Flores Araya', 'Bernardo O''Higgins 200, Rancagua', '988886666', 'jorge.flores@email.cl'),
('Elena Tapia Mella', 'Sector Oriente, Chillán', '999991111', 'elena.tapia@email.cl'),
('Ricardo Peña Salas', 'Avenida Alemania 150, Valdivia', '911112222', 'ricardo.pena@email.cl'),
('Camila Bravo Rojas', 'Calle Nueva 400, Puerto Montt', '922223333', 'camila.bravo@email.cl'),
('Felipe Silva Lagos', 'Costanera Norte 50, Iquique', '933334444', 'felipe.silva@email.cl'),
('Valentina Paz Olivares', 'Las Acacias 60, La Serena', '944445555', 'valentina.paz@email.cl'),
('Daniel Orellana Moya', 'Diego Portales 70, Copiapó', '955556666', 'daniel.orellana@email.cl'),
('Javiera Reyes Soto', 'Los Pinos 80, San Bernardo', '966668888', 'javiera.reyes@email.cl'),
('Sebastián Muñoz Ruiz', 'El Bosque 90, Maipú', '977779999', 'sebastian.munoz@email.cl'),
('Isidora Guzmán Vega', 'Plaza Mayor 10, Puente Alto', '988880000', 'isidora.guzman@email.cl'),
('Gabriel Castro Ortiz', 'Camino del Sol 20, Quilpué', '999992222', 'gabriel.castro@email.cl'),
('Paz Herrera Morales', 'Viaducto 30, Talcahuano', '910103030', 'paz.herrera@email.cl'),
('Benjamín Soto Moya', 'El Arrayán 40, Colina', '920204040', 'benjamin.soto@email.cl'),
('Catalina Rojas Silva', 'Océano Pacífico 50, Valparaíso', '930305050', 'catalina.rojas@email.cl'),
('Diego Flores Leal', 'Cordillera 60, Los Andes', '940406060', 'diego.flores@email.cl'),
('Emilia Vidal Núñez', 'Valle Central 70, Curicó', '950507070', 'emilia.vidal@email.cl'),
('Matías Torres Bravo', 'Las Palmas 80, Linares', '960608080', 'matias.torres@email.cl'),
('Florencia Peña Salas', 'Río Claro 90, Osorno', '970709090', 'florencia.pena@email.cl'),
('Ignacio Bravo Castro', 'Volcán Osorno 100, Puerto Varas', '980801010', 'ignacio.bravo@email.cl'),
('Josefina Araya Flores', 'Desierto de Atacama 110, Calama', '990902020', 'josefina.araya@email.cl'),
('Manuel Mella Tapia', 'San Pedro 120, Arica', '900003000', 'manuel.mella@email.cl'),
('Rocío Vega Mena', 'Playa Blanca 130, Punta Arenas', '911114444', 'rocio.vega@email.cl'),
('Lucía Díaz Gómez', 'Avenida del Mar 140, Coquimbo', '922225555', 'lucia.diaz@email.cl'),
('Agustín Morales Núñez', 'Callejón Sur 150, Quillota', '933336666', 'agustin.morales@email.cl'),
('Fernanda Ortiz Soto', 'Ruta Larga 160, Melipilla', '944447777', 'fernanda.ortiz@email.cl'),
('Vicente Rojas Moya', 'Camino Real 170, Talagante', '955558888', 'vicente.rojas@email.cl'),
('Antonia Silva Leal', 'El Hualle 180, Buin', '966669999', 'antonia.silva@email.cl'),
('Tomás Lagos Vera', 'Los Alerces 190, Puente Alto', '977770000', 'tomas.lagos@email.cl'),
('Renata Castro Araya', 'Los Aromos 200, Ñuñoa', '988881111', 'renata.castro@email.cl'),
('Santiago Ortiz Tapia', 'Las Flores 210, La Florida', '999993333', 'santiago.ortiz@email.cl'),
('Andrea Mella Bravo', 'Los Volcanes 220, Maipú', '910104444', 'andrea.mella@email.cl'),
('Fabián Vega Flores', 'Santa Rosa 230, San Miguel', '920205555', 'fabian.vega@email.cl'),
('Martina Pérez Leal', 'Gran Avenida 240, El Bosque', '930306666', 'martina.perez@email.cl'),
('Joaquín Díaz Núñez', 'Pedro de Valdivia 250, Concepción', '940407777', 'joaquin.diaz@email.cl'),
('Gabriela Soto Peña', 'Orompello 260, Los Ángeles', '950508888', 'gabriela.soto@email.cl'),
('Cristóbal Torres Salas', 'Baquedano 270, Antofagasta', '960609999', 'cristobal.torres@email.cl'),
('Valeria Mena Bravo', 'Lautaro 280, Puerto Montt', '970700000', 'valeria.mena@email.cl'),
('Lucas Bravo Rojas', 'Brasil 290, Valparaíso', '980801111', 'lucas.bravo@email.cl'),
('Constanza Flores Castro', 'Victoria 300, Temuco', '990902222', 'constanza.flores@email.cl'),
('Esteban Núñez Mella', 'Alameda 310, Santiago', '900004444', 'esteban.nunez@email.cl'),
('Francisca Tapia Vega', 'Ejército 320, Chillán', '911115555', 'francisca.tapia@email.cl'),
('Héctor Leal Ortiz', 'Independencia 330, Talca', '922226666', 'hector.leal@email.cl'),
('Carolina Araya Soto', 'Oasis 340, Iquique', '933337777', 'carolina.araya@email.cl'),
('Gonzalo Moya Pérez', 'Costanera Sur 350, Valdivia', '944448888', 'gonzalo.moya@email.cl'),
('Denisse Vera Guzmán', 'Aconcagua 360, Los Andes', '955559999', 'denisse.vera@email.cl'),
('Álvaro Ruiz Flores', 'Central 370, San Bernardo', '966660000', 'alvaro.ruiz@email.cl'),
('Mariana Ortiz Silva', 'Oriente 380, Quilpué', '977771111', 'mariana.ortiz@email.cl'),
('Nicolás Bravo Vega', 'Poniente 390, Curicó', '988882222', 'nicolas.bravo@email.cl'),
('Julieta Castro Leal', 'Sur 400, Osorno', '999994444', 'julieta.castro@email.cl'),
('Felipe Mella Núñez', 'Norte 410, Calama', '910105555', 'felipe.mella@email.cl'),
('Patricia Salas Tapia', 'Playas 420, Arica', '920206666', 'patricia.salas@email.cl');


INSERT INTO productos (nombre, precio) VALUES
('Detergente Líquido concentrado 1.5L', 8990),
('Cloro Gel Desinfectante 2L', 3490),
('Limpiador Multiuso Lavanda 1L', 2190),
('Suavizante para Ropa Floral 3L', 5890),
('Jabón de Tocador en Barra x4', 1990),
('Papel Higiénico Doble Hoja x12', 6990),
('Toallas de Papel Cocina Rollo Gigante', 2490),
('Bolsas de Basura con Cierre 50L x20', 3990),
('Esponja de Acero Inoxidable x3', 1290),
('Desengrasante de Cocina Profesional 750ml', 4590),
('Ambientador Spray Cítrico', 2790),
('Limpiavidrios Anti-empañamiento 500ml', 3190),
('Alcohol Desnaturalizado 1L', 1590),
('Lavalozas Ultra Concentrado 500ml', 1890),
('Mopa de Microfibra con Mango Telescópico', 9990),
('Balde de Plástico con Escurridor 12L', 5490),
('Cepillo para Inodoro con Base', 4290),
('Pastillas Desodorantes para Baño x4', 1790),
('Cera para Pisos Autobrillo 1L', 6290),
('Removedor de Sarro y Hongos 500ml', 4990),
('Guantes de Goma para Limpieza Talla M', 2390),
('Paños de Microfibra Multiuso x5', 3690),
('Spray Anti-polvo Muebles Madera 300ml', 3890),
('Insecticida para Moscas y Mosquitos 400ml', 4190),
('Crema Limpiadora Abrillantadora 500g', 2990),
('Escoba de Interior Cerdas Suaves', 7490),
('Recogedor de Mano con Borde de Goma', 1190),
('Aromatizante de Telas 500ml', 3390),
('Desinfectante de Superficies Sin Cloro 1L', 3790),
('Limpia Hornos y Parrillas 500ml', 5190),
('Bicarbonato de Sodio Grado Limpieza 1Kg', 990),
('Vinagre Blanco de Limpieza 5L', 2590),
('Jabón Líquido para Manos Aloe Vera 500ml', 2090),
('Repuesto Mopa Plana Microfibra', 4690),
('Quitamanchas Ropa Color 500ml', 5590),
('Bloque Desodorante para Estanques de Agua', 1490),
('Vara de Incienso Aromática x20', 890),
('Filtros de Café Desechables x100', 1690),
('Máquina Afeitadora Desechable x5', 3090),
('Pañales Desechables Talla G x30', 12990);


INSERT INTO metodos_pago (nombre) VALUES
('Crédito'),
('Débito'),
('MercadoPago');


SET FOREIGN_KEY_CHECKS = 1; -- Si es que se añadieron las restricciones de llaves foráneas antes de esto, setear en 0 al agregar los datos de pedidos y detales_pedido. Al terminar setear en 1 y ejecutar.

-- Insertar 100 Pedidos (Distribución No Simétrica)
INSERT INTO pedidos (id_cliente, fecha, total, id_metodo)
VALUES -- Clientes con muchos pedidos (ID 1 al 10) - 5 a 10 pedidos cada uno.

    (1, '2025-10-01', 50000, 1),
    (1, '2025-10-15', 35000, 2),
    (1, '2025-11-05', 42000, 1),
    (2, '2025-10-02', 28000, 3),
    (2, '2025-10-20', 15000, 3),
    (2, '2025-11-10', 55000, 2),
    (3, '2025-10-03', 12000, 1),
    (3, '2025-11-01', 33000, 1),
    (4, '2025-10-04', 60000, 2),
    (4, '2025-10-25', 18000, 3),
    (4, '2025-11-15', 70000, 2),
    (4, '2025-12-01', 25000, 2),
    (5, '2025-10-05', 22000, 3),
    (5, '2025-11-02', 48000, 1),
    (5, '2025-11-20', 14000, 3),
    (6, '2025-10-06', 45000, 2),
    (6, '2025-10-28', 21000, 2),
    (6, '2025-12-10', 30000, 3),
    (6, '2025-12-25', 19000, 2),
    (7, '2025-10-07', 18000, 1),
    (7, '2025-11-03', 40000, 1),
    (7, '2025-12-05', 23000, 1),
    (8, '2025-10-08', 31000, 3),
    (8, '2025-11-04', 16000, 3),
    (8, '2025-12-15', 52000, 2),
    (8, '2025-12-20', 9000, 3),
    (9, '2025-10-09', 55000, 2),
    (9, '2025-11-11', 27000, 1),
    (9, '2025-12-02', 46000, 2),
    (9, '2026-01-01', 11000, 1),
    (10, '2025-10-10', 38000, 1),
    (10, '2025-11-12', 20000, 2),
    (10, '2025-12-03', 34000, 1),
    (10, '2026-01-05', 17000, 3),
    (10, '2026-01-15', 51000, 1),
-- Clientes con pedidos intermedios (ID 11 al 30) - 2 a 4 pedidos cada uno.
    (11, '2025-10-11', 25000, 2),
    (11, '2025-11-13', 15000, 2),
    (12, '2025-10-12', 32000, 3),
    (12, '2025-11-14', 10000, 3),
    (12, '2025-12-06', 40000, 3),
    (13, '2025-10-13', 19000, 1),
    (13, '2025-11-16', 29000, 1),
    (14, '2025-10-14', 44000, 2),
    (14, '2025-11-17', 12000, 3),
    (14, '2025-12-07', 22000, 2),
    (15, '2025-10-16', 27000, 3),
    (15, '2025-11-18', 36000, 1),
    (16, '2025-10-17', 13000, 1),
    (16, '2025-11-19', 41000, 2),
    (16, '2025-12-08', 26000, 1),
    (16, '2026-01-02', 17000, 2),
    (17, '2025-10-18', 33000, 2),
    (17, '2025-11-21', 18000, 2),
    (18, '2025-10-19', 47000, 3),
    (18, '2025-11-22', 24000, 3),
    (18, '2025-12-09', 39000, 3),
    (19, '2025-10-21', 16000, 1),
    (19, '2025-11-23', 30000, 1),
    (20, '2025-10-22', 49000, 2),
    (20, '2025-11-24', 11000, 3),
    (20, '2025-12-11', 35000, 2),
    (21, '2025-10-23', 21000, 3),
    (21, '2025-11-25', 43000, 3),
    (22, '2025-10-24', 37000, 1),
    (22, '2025-11-26', 14000, 2),
    (22, '2025-12-12', 28000, 1),
    (23, '2025-10-26', 15000, 2),
    (23, '2025-11-27', 48000, 1),
    (24, '2025-10-27', 30000, 3),
    (24, '2025-11-28', 19000, 3),
    (24, '2025-12-13', 44000, 3),
    (25, '2025-10-29', 23000, 1),
    (25, '2025-11-29', 38000, 2),
    (26, '2025-10-30', 46000, 2),
    (26, '2025-12-04', 16000, 1),
    (26, '2025-12-14', 31000, 2),
    (27, '2025-10-31', 17000, 3),
    (27, '2025-12-16', 49000, 3),
    (28, '2025-11-06', 34000, 1),
    (28, '2025-12-17', 20000, 1),
    (28, '2025-12-21', 15000, 2),
    (29, '2025-11-07', 28000, 2),
    (29, '2025-12-18', 42000, 3),
    (30, '2025-11-08', 40000, 3),
    (30, '2025-12-19', 13000, 1),
    (30, '2025-12-22', 50000, 2),
-- Clientes con 1 solo pedido (ID 31 al 60) - 1 pedido cada uno.
    (31, '2025-11-09', 25000, 1),
    (32, '2025-11-10', 12000, 2),
    (33, '2025-11-20', 33000, 3),
    (34, '2025-12-01', 18000, 1),
    (35, '2025-12-02', 47000, 2),
    (36, '2025-12-03', 14000, 3),
    (37, '2025-12-04', 29000, 1),
    (38, '2025-12-05', 41000, 2),
    (39, '2025-12-06', 22000, 3),
    (40, '2025-12-07', 36000, 1),
    (41, '2025-12-08', 19000, 2),
    (42, '2025-12-09', 45000, 3),
    (43, '2025-12-10', 11000, 1),
    (44, '2025-12-11', 52000, 2),
    (45, '2025-12-12', 24000, 3),
    (46, '2025-12-13', 38000, 1),
    (47, '2025-12-14', 16000, 2),
    (48, '2025-12-15', 30000, 3),
    (49, '2025-12-16', 43000, 1),
    (50, '2025-12-17', 20000, 2),
    (51, '2025-12-18', 35000, 3),
    (52, '2025-12-19', 17000, 1),
    (53, '2025-12-20', 40000, 2),
    (54, '2025-12-21', 23000, 3),
    (55, '2025-12-22', 39000, 1),
    (56, '2025-12-23', 15000, 2),
    (57, '2025-12-24', 48000, 3),
    (58, '2025-12-25', 21000, 1),
    (59, '2025-12-26', 32000, 2),
    (60, '2025-12-27', 10000, 3),
    (1, '2026-01-20', 40000, 2),
    (2, '2026-01-25', 25000, 3),
    (3, '2026-01-30', 15000, 1),
    (4, '2026-02-05', 55000, 2),
    (5, '2026-02-10', 30000, 3),
    (6, '2026-02-15', 18000, 2),
    (7, '2026-02-20', 45000, 1),
    (8, '2026-02-25', 22000, 3),
    (9, '2026-03-01', 37000, 2),
    (10, '2026-03-05', 14000, 1),
    (11, '2026-03-10', 41000, 2),
    (12, '2026-03-15', 26000, 3),
    (13, '2026-03-20', 33000, 1),
    (14, '2026-03-25', 19000, 2),
    (15, '2026-03-30', 46000, 3),
    (16, '2026-04-05', 28000, 1),
    (17, '2026-04-10', 35000, 2),
    (18, '2026-04-15', 12000, 3),
    (19, '2026-04-20', 50000, 1),
    (20, '2026-04-25', 27000, 2),
    (21, '2026-04-30', 34000, 3),
    (22, '2026-05-05', 16000, 1),
    (23, '2026-05-10', 49000, 2),
    (24, '2026-05-15', 23000, 3),
    (25, '2026-05-20', 37000, 1),
    (26, '2026-05-25', 18000, 2),
    (27, '2026-05-30', 42000, 3);

-- Insertar Detalles de Pedido (Más de 100 registros para poblar los 100 pedidos)

INSERT INTO detalles_pedido (id_producto, id_pedido, cantidad)
VALUES -- Pedidos 1 al 10: Multi-producto

    (1, 1, 3),
    (12, 1, 2),
    (25, 1, 1),
    (5, 2, 5),
    (15, 2, 1),
    (30, 3, 1),
    (2, 3, 2),
    (18, 4, 10),
    (1, 4, 1),
    (3, 5, 2),
    (16, 5, 1),
    (22, 6, 4),
    (10, 6, 2),
    (20, 7, 1),
    (35, 7, 2),
    (4, 8, 3),
    (6, 9, 2),
    (11, 9, 4),
    (13, 10, 5),
    (32, 10, 1),
-- Pedidos 11 al 30: Variación de productos
    (8, 11, 3),
    (28, 11, 1),
    (17, 12, 1),
    (24, 12, 2),
    (36, 13, 2),
    (37, 14, 1),
    (2, 14, 4),
    (29, 15, 2),
    (39, 15, 1),
    (14, 16, 5),
    (1, 16, 2),
    (7, 17, 3),
    (33, 17, 2),
    (19, 18, 1),
    (40, 18, 1),
    (21, 19, 2),
    (34, 19, 1),
    (9, 20, 4),
    (10, 20, 1),
    (3, 21, 5),
    (12, 21, 2),
    (27, 22, 1),
    (15, 22, 2),
    (23, 23, 3),
    (18, 24, 2),
    (31, 24, 5),
    (16, 25, 1),
    (4, 25, 3),
    (5, 26, 4),
    (25, 26, 1),
    (6, 27, 2),
    (13, 27, 3),
    (22, 28, 1),
    (30, 28, 2),
    (20, 29, 3),
    (29, 30, 1),
    (8, 30, 2),
-- Pedidos 31 al 60: Principalmente 1-2 productos
    (1, 31, 2),
    (15, 32, 1),
    (3, 33, 3),
    (18, 34, 1),
    (2, 35, 5),
    (12, 36, 1),
    (34, 37, 2),
    (5, 38, 4),
    (25, 39, 1),
    (1, 40, 3),
    (10, 41, 1),
    (20, 42, 2),
    (13, 43, 1),
    (40, 44, 4),
    (22, 45, 2),
    (16, 46, 3),
    (14, 47, 1),
    (3, 48, 5),
    (2, 49, 3),
    (18, 50, 1),
    (25, 51, 2),
    (1, 52, 1),
    (15, 53, 4),
    (3, 54, 2),
    (12, 55, 3),
    (40, 56, 1),
    (5, 57, 5),
    (10, 58, 2),
    (20, 59, 3),
    (13, 60, 1),
-- Relleno para llegar a 100 pedidos y más detalles
    (2, 61, 4),
    (12, 62, 2),
    (35, 63, 1),
    (1, 64, 5),
    (5, 65, 3),
    (10, 66, 1),
    (20, 67, 2),
    (3, 68, 4),
    (12, 69, 1),
    (2, 70, 3),
    (1, 71, 2),
    (15, 72, 1),
    (3, 73, 3),
    (18, 74, 1),
    (2, 75, 5),
    (12, 76, 1),
    (34, 77, 2),
    (5, 78, 4),
    (25, 79, 1),
    (1, 80, 3),
    (10, 81, 1),
    (20, 82, 2),
    (13, 83, 1),
    (40, 84, 4),
    (22, 85, 2),
    (16, 86, 3),
    (14, 87, 1),
    (3, 88, 5),
    (2, 89, 3),
    (18, 90, 1),
    (25, 91, 2),
    (1, 92, 1),
    (15, 93, 4),
    (3, 94, 2),
    (12, 95, 3),
    (40, 96, 1),
    (5, 97, 5),
    (10, 98, 2),
    (20, 99, 3),
    (13, 100, 1),
    (4, 1, 1),
    (6, 2, 1),
    (7, 3, 1),
    (8, 4, 1),
    (9, 5, 1),
    (10, 6, 1),
    (11, 7, 1),
    (12, 8, 1),
    (13, 9, 1),
    (14, 10, 1),
    (15, 1, 1),
    (16, 2, 1),
    (17, 3, 1),
    (18, 4, 1),
    (19, 5, 1),
    (20, 6, 1),
    (21, 7, 1),
    (22, 8, 1),
    (23, 9, 1),
    (24, 10, 1),
    (25, 11, 1),
    (26, 12, 1),
    (27, 13, 1),
    (28, 14, 1),
    (29, 15, 1),
    (30, 16, 1),
    (31, 17, 1),
    (32, 18, 1),
    (33, 19, 1),
    (34, 20, 1),
    (35, 21, 1),
    (36, 22, 1),
    (37, 23, 1),
    (38, 24, 1),
    (39, 25, 1),
    (40, 26, 1),
    (1, 27, 1),
    (2, 28, 1),
    (3, 29, 1),
    (4, 30, 1);


CREATE DATABASE IF NOT EXISTS evaluacion_modulo_db;

GO

USE evaluacion_modulo_db;

/* ========== Tablas ========== */

CREATE TABLE productos
(
  id_producto INT     NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombre      VARCHAR(50) NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  precio      INT     NOT NULL,
  cantidad    INT     NOT NULL
);


CREATE TABLE proveedores
(
  id_proveedor INT     NOT NULL PRIMARY KEY  AUTO_INCREMENT,
  nombre       VARCHAR(50) NOT NULL,
  direccion    VARCHAR(50) NOT NULL,
  telefono     VARCHAR(15) NOT NULL,
  email        VARCHAR(50) NOT NULL
);

CREATE TABLE transacciones
(
  id_transaccion INT     NOT NULL PRIMARY KEY AUTO_INCREMENT,
  tipo           VARCHAR(50) NOT NULL,
  fecha          DATE    NOT NULL,
  cantidad       INT     NOT NULL,
  id_producto    INT     NOT NULL,
  id_proveedor   INT     NOT NULL
);

/* ========== Restricciones ========== */

ALTER TABLE productos
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

ALTER TABLE proveedores
  ADD CONSTRAINT UQ_nombre UNIQUE (nombre);

ALTER TABLE proveedores
  ADD CONSTRAINT UQ_telefono UNIQUE (telefono);

ALTER TABLE proveedores
  ADD CONSTRAINT UQ_email UNIQUE (email);

ALTER TABLE transacciones
  ADD CONSTRAINT FK_productos_TO_transacciones
    FOREIGN KEY (id_producto)
    REFERENCES productos (id_producto);

ALTER TABLE transacciones
  ADD CONSTRAINT FK_proveedores_TO_transacciones
    FOREIGN KEY (id_proveedor)
    REFERENCES proveedores (id_proveedor);



/* ========== Querys ==========*/


-- Consultas Básicas 


-- 1.- Recupera todos los productos disponibles en el inventario 
SELECT * FROM productos;
-- /* 2.- Recupera todos los proveedores que suministran productos específicos
SELECT DISTINCT p.*
FROM proveedores p
INNER JOIN transacciones t ON p.id_proveedor = t.id_proveedor
WHERE t.id_producto = 1;

-- 3.- Consulta las transacciones realizadas en una fecha específica
SELECT * FROM transacciones
WHERE fecha BETWEEN '2025-01-01' AND '2025-01-31'
ORDER BY fecha ASC;

/* 4.- Realiza consultas de selección con funciones de agrupación, como COUNT() y SUM(), para
calcular el número total de productos vendidos o el valor total de las compras. */

SELECT COUNT(*) AS total_productos_vendidos
FROM transacciones
WHERE tipo = 'venta';

SELECT SUM(t.cantidad * p.precio) AS total_compras
FROM productos p
INNER JOIN transacciones t ON p.id_producto = t.id_producto
WHERE t.tipo = 'compra';


-- Consultas Complejas

-- 1.- Realiza una consulta que recupere el total de ventas de un producto durante el mes anterior.
SELECT 
    SUM(t.cantidad) AS total_ventas_julio,
    SUM(t.cantidad * p.precio) AS precio_total_julio
FROM transacciones t
INNER JOIN productos p ON t.id_producto = p.id_producto
WHERE t.tipo = 'venta'
  AND MONTH(t.fecha) = 7
  AND YEAR(t.fecha) = 2025
  AND p.id_producto = 49;

/* 2.- Implementa una consulta con subconsultas (subqueries) para obtener productos que no se han
vendido durante un período determinado. */


SELECT p.*
FROM productos p
WHERE p.id_producto NOT IN (
    SELECT DISTINCT t.id_producto
    FROM transacciones t
    WHERE t.tipo = 'venta'
      AND t.fecha BETWEEN '2025-04-01' AND '2025-07-31'
  );




/* ========== Manipulación de Datos ========== */



-- Insertar Datos

-- INSERCIÓN DE PROVEEDORES (20 registros)

INSERT INTO proveedores (nombre, direccion, telefono, email) VALUES
('TechSupply SpA', 'Av. Libertador 1234, Santiago', '+56912345001', 'contacto@techsupply.cl'),
('Distribuidora Global', 'Calle Comercio 567, Valparaíso', '+56912345002', 'ventas@distglobal.cl'),
('Importadora del Sur', 'Av. España 890, Concepción', '+56912345003', 'info@importsur.cl'),
('Mayorista Central', 'Paseo Bulnes 234, Santiago', '+56912345004', 'compras@mayorista.cl'),
('ElectroMax Ltda', 'Los Carrera 456, Viña del Mar', '+56912345005', 'electromax@email.cl'),
('Suministros Industriales', 'Av. Grecia 789, Antofagasta', '+56912345006', 'ventas@sumindustrial.cl'),
('Comercial Pacífico', 'Errázuriz 123, Valparaíso', '+56912345007', 'contacto@compacífico.cl'),
('Ferretería Nacional', 'Manuel Montt 567, Temuco', '+56912345008', 'ferreteria@nacional.cl'),
('Tecnología Avanzada', 'Apoquindo 2345, Las Condes', '+56912345009', 'tech@avanzada.cl'),
('Distribuidora Norte', 'Baquedano 678, Iquique', '+56912345010', 'norte@distribuye.cl'),
('ProveMax Chile', 'Santa Rosa 901, La Serena', '+56912345011', 'provemax@chile.cl'),
('Importaciones Rápidas', 'Av. Brasil 234, Valparaíso', '+56912345012', 'rapidas@import.cl'),
('SuministroTec', 'Beauchef 567, Santiago', '+56912345013', 'info@suministrotec.cl'),
('Comercial del Maule', 'Av. San Miguel 890, Talca', '+56912345014', 'maule@comercial.cl'),
('Distribuidora Express', 'Pedro de Valdivia 123, Providencia', '+56912345015', 'express@distrib.cl'),
('Megastock Chile', 'Av. Kennedy 4567, Vitacura', '+56912345016', 'info@megastock.cl'),
('Proveedor Premium', 'Isidora Goyenechea 890, Las Condes', '+56912345017', 'premium@proveedor.cl'),
('Suministros del Bio Bio', 'Colo Colo 234, Concepción', '+56912345018', 'biobio@suministros.cl'),
('TechWorld Importaciones', 'Av. Vicuña Mackenna 567, Santiago', '+56912345019', 'techworld@import.cl'),
('Distribuidora Universal', 'O Higgins 789, Rancagua', '+56912345020', 'universal@distrib.cl');


-- INSERCIÓN DE PRODUCTOS (50 registros) 

INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES
('Laptop HP Pavilion', 'Laptop 15.6 pulgadas, 8GB RAM, 256GB SSD', 549990, 15),
('Mouse Inalámbrico Logitech', 'Mouse ergonómico con batería recargable', 19990, 45),
('Teclado Mecánico Redragon', 'Teclado RGB retroiluminado', 39990, 30),
('Monitor Samsung 24"', 'Monitor Full HD, panel IPS', 129990, 20),
('Disco Duro Externo 1TB', 'WD Elements portátil USB 3.0', 54990, 35),
('Auriculares Sony WH-1000XM4', 'Cancelación de ruido activa', 299990, 12),
('Webcam Logitech C920', 'Full HD 1080p con micrófono', 69990, 25),
('Impresora HP DeskJet', 'Multifuncional con WiFi', 89990, 18),
('Cable HDMI 2.0', 'Cable 2 metros alta velocidad', 8990, 100),
('Hub USB-C 7 puertos', 'Adaptador multipuerto con HDMI', 34990, 40),
('Memoria RAM DDR4 16GB', 'Crucial 3200MHz', 49990, 28),
('SSD Kingston 500GB', 'NVMe M.2 alta velocidad', 59990, 22),
('Mousepad Gaming XXL', 'Base antideslizante 90x40cm', 14990, 60),
('Silla Gamer Ergonómica', 'Reclinable con soporte lumbar', 189990, 8),
('Escritorio Esquinero', 'MDF 120x60cm con estante', 79990, 10),
('Router WiFi 6 TP-Link', 'Doble banda AC1200', 44990, 15),
('Switch Ethernet 8 puertos', 'Gigabit no administrable', 29990, 20),
('Fuente Poder 650W', 'Certificación 80 Plus Bronze', 54990, 16),
('Tarjeta Gráfica GTX 1650', 'NVIDIA 4GB GDDR6', 249990, 6),
('Procesador Intel i5', '11va generación 6 núcleos', 189990, 10),
('Placa Madre ASUS', 'Socket LGA1200 ATX', 129990, 12),
('Gabinete PC RGB', 'Ventana templada con 3 ventiladores', 69990, 14),
('Cooler CPU Líquido', 'Sistema refrigeración 240mm', 89990, 9),
('Pasta Térmica Arctic', 'Tubo 4 gramos alta conductividad', 6990, 80),
('Kit Limpieza Electrónica', 'Spray y paños microfibra', 12990, 50),
('UPS 1000VA', 'Respaldo energía 600W', 119990, 11),
('Micrófono USB Fifine', 'Condensador para streaming', 39990, 18),
('Luz LED Ring Light', 'Iluminación para video 12 pulgadas', 34990, 22),
('Soporte Monitor Brazo', 'Articulado hasta 27 pulgadas', 44990, 17),
('Regleta Protección 8 Salidas', 'Protector sobretensión 2500W', 19990, 45),
('Adaptador WiFi USB', 'AC1200 doble banda antena', 16990, 38),
('Tarjeta Sonido Externa', 'USB DAC audio 7.1', 39990, 15),
('Cámara IP Seguridad', 'WiFi 2MP visión nocturna', 49990, 20),
('Sistema Audio 2.1', 'Altavoces con subwoofer 80W', 79990, 13),
('Micrófono Solapa Inalámbrico', 'Para presentaciones 2.4GHz', 29990, 25),
('Maletín Notebook 15.6"', 'Acolchado con compartimentos', 24990, 32),
('Soporte Laptop Ajustable', 'Aluminio elevado ergonómico', 19990, 28),
('Ventilador USB Portátil', 'Silencioso 2 velocidades', 9990, 55),
('Organizador Cables', 'Kit 20 piezas velcro clips', 7990, 70),
('Batería Externa 20000mAh', 'Carga rápida 2 puertos USB', 29990, 26),
('Lector Tarjetas SD/MicroSD', 'USB 3.0 alta velocidad', 8990, 42),
('Funda Tablet 10"', 'Protección con soporte', 14990, 35),
('Stylus Pen Capacitivo', 'Lápiz táctil universal', 12990, 40),
('Capturadora Video HDMI', 'USB 3.0 para streaming', 79990, 10),
('Kit Destornilladores Precisión', '24 piezas magnéticos', 16990, 48),
('Multímetro Digital', 'Medidor voltaje corriente resistencia', 24990, 19),
('Soldador Electrónico 60W', 'Temperatura ajustable con base', 34990, 14),
('Película Protectora Notebook', 'Anti reflejo 15.6 pulgadas', 11990, 30),
('Base Refrigerante Notebook', '5 ventiladores LED ajustables', 24990, 24),
('Candado Seguridad Kensington', 'Cable reforzado con llave', 18990, 27);


-- INSERCIÓN DE TRANSACCIONES (100 registros)

INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor) VALUES
('compra', '2024-01-15', 10, 1, 1),
('compra', '2024-01-18', 50, 2, 2),
('compra', '2024-01-20', 30, 3, 3),
('venta', '2024-01-25', 2, 1, 1),
('venta', '2024-02-01', 5, 2, 2),
('compra', '2024-02-05', 25, 4, 1),
('compra', '2024-02-10', 40, 5, 4),
('venta', '2024-02-14', 3, 4, 1),
('venta', '2024-02-20', 5, 5, 4),
('compra', '2024-02-25', 15, 6, 5),
('venta', '2024-03-01', 1, 6, 5),
('compra', '2024-03-05', 30, 7, 6),
('venta', '2024-03-10', 5, 7, 6),
('compra', '2024-03-15', 20, 8, 7),
('venta', '2024-03-18', 2, 8, 7),
('compra', '2024-03-22', 100, 9, 2),
('venta', '2024-03-25', 10, 2, 2),
('venta', '2024-04-02', 15, 9, 2),
('compra', '2024-04-08', 50, 10, 8),
('venta', '2024-04-12', 10, 10, 8),
('compra', '2024-04-15', 30, 11, 9),
('venta', '2024-04-20', 2, 11, 9),
('compra', '2024-04-25', 25, 12, 10),
('venta', '2024-05-01', 3, 12, 10),
('compra', '2024-05-05', 60, 13, 2),
('venta', '2024-05-10', 8, 13, 2),
('venta', '2024-05-15', 12, 13, 2),
('compra', '2024-05-20', 10, 14, 11),
('venta', '2024-05-25', 2, 14, 11),
('compra', '2024-06-01', 12, 15, 12),
('venta', '2024-06-05', 2, 15, 12),
('compra', '2024-06-10', 20, 16, 13),
('venta', '2024-06-15', 5, 16, 13),
('compra', '2024-06-20', 25, 17, 14),
('venta', '2024-06-25', 5, 17, 14),
('compra', '2024-07-01', 18, 18, 15),
('venta', '2024-07-05', 2, 18, 15),
('compra', '2024-07-10', 8, 19, 16),
('venta', '2024-07-15', 2, 19, 16),
('compra', '2024-07-20', 12, 20, 17),
('venta', '2024-07-25', 2, 20, 17),
('compra', '2024-08-01', 15, 21, 18),
('venta', '2024-08-05', 3, 21, 18),
('compra', '2024-08-10', 16, 22, 19),
('venta', '2024-08-15', 2, 22, 19),
('compra', '2024-08-20', 10, 23, 20),
('venta', '2024-08-25', 1, 23, 20),
('compra', '2024-09-01', 80, 24, 2),
('venta', '2024-09-05', 15, 24, 2),
('venta', '2024-09-10', 20, 24, 2),
('compra', '2025-01-05', 50, 25, 3),
('venta', '2025-01-08', 8, 25, 3),
('compra', '2025-01-12', 15, 26, 4),
('venta', '2025-01-15', 4, 26, 4),
('compra', '2025-01-18', 20, 27, 5),
('venta', '2025-01-22', 2, 27, 5),
('compra', '2025-01-25', 25, 28, 6),
('venta', '2025-01-28', 3, 28, 6),
('compra', '2025-02-01', 20, 29, 7),
('venta', '2025-02-05', 3, 29, 7),
('compra', '2025-02-08', 50, 30, 8),
('venta', '2025-02-12', 5, 30, 8),
('compra', '2025-02-15', 40, 31, 9),
('venta', '2025-02-18', 2, 31, 9),
('compra', '2025-02-22', 18, 32, 10),
('venta', '2025-02-25', 3, 32, 10),
('compra', '2025-03-01', 22, 33, 11),
('venta', '2025-03-05', 2, 33, 11),
('compra', '2025-03-08', 15, 34, 12),
('venta', '2025-03-12', 2, 34, 12),
('compra', '2025-03-15', 28, 35, 13),
('venta', '2025-03-18', 3, 35, 13),
('compra', '2025-03-22', 35, 36, 14),
('venta', '2025-03-25', 3, 36, 14),
('compra', '2025-04-01', 30, 37, 15),
('venta', '2025-04-05', 2, 37, 15),
('compra', '2025-04-08', 60, 38, 2),
('venta', '2025-04-12', 5, 38, 2),
('compra', '2025-04-15', 75, 39, 3),
('venta', '2025-04-18', 5, 39, 3),
('compra', '2025-04-22', 30, 40, 16),
('venta', '2025-04-25', 4, 40, 16),
('compra', '2025-05-01', 45, 41, 17),
('venta', '2025-05-05', 3, 41, 17),
('compra', '2025-05-08', 38, 42, 18),
('venta', '2025-05-12', 3, 42, 18),
('compra', '2025-05-15', 45, 43, 19),
('venta', '2025-05-18', 5, 43, 19),
('compra', '2025-05-22', 12, 44, 20),
('venta', '2025-05-25', 2, 44, 20),
('compra', '2025-06-01', 50, 45, 1),
('venta', '2025-06-05', 2, 45, 1),
('compra', '2025-06-08', 20, 46, 2),
('venta', '2025-06-12', 1, 46, 2),
('compra', '2025-06-15', 16, 47, 3),
('venta', '2025-06-18', 2, 47, 3),
('compra', '2025-06-22', 32, 48, 4),
('venta', '2025-06-25', 2, 48, 4),
('compra', '2025-07-01', 26, 49, 5),
('venta', '2025-07-05', 2, 49, 5),
('compra', '2025-07-08', 28, 50, 6);


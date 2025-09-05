CREATE DATABASE IF NOT EXISTS m5_ae2_grupaldb;
USE m5_ae2_grupaldb;


-- TABLAS
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY ,
    nombre VARCHAR(100),
    telefono VARCHAR(15),
    email VARCHAR(100),
    direccion VARCHAR(100)
);

CREATE TABLE Vehiculos (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    año INT,
    precio_dia DECIMAL(10,2) 
);


CREATE TABLE Alquileres (
    id_alquiler INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_vehiculo INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculos(id_vehiculo)
);


CREATE TABLE PAGOS (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_alquiler INT,
    monto DECIMAL(10,2),
    fecha_pago DATE,
    FOREIGN KEY (id_alquiler) REFERENCES Alquileres(id_alquiler)
)

-- Datos

INSERT INTO Clientes VALUES
(1, 'Juan Pérez', '555-1234' , 'juan@mail.com', 'Calle 123'),
(2, 'Laura Gómez ', '555-5678' , 'laura@mail.com', 'Calle 456'),
(3, 'Carlos Sánchez', '555-9101' , 'carlos@mail.com', 'Calle 789');

INSERT INTO Vehiculos VALUES
(1, 'Toyota', 'Corolla', '2020', 30.00),
(2, 'Honda', 'Civic', '2019', 28.00),
(3, 'Ford', 'Focus ', '2021', 35.00);

INSERT INTO Alquileres VALUES
(1, 1, 2, '2025-03-10', '2025-03-15'),
(2, 2, 1, '2025-03-12', '2025-03-16'),
(3, 3, 3, '2025-03-20', '2025-03-22');


-- Se actualiza datos para poder mostrar Query 7
UPDATE Alquileres
SET id_vehiculo = 1
WHERE id_alquiler IN (1, 2, 3);


INSERT INTO Pagos VALUES
(1, 1, 150.00, '2025-03-10'),
(2, 2, 112.00, '2025-03-12'),
(3, 3, 70.00, '2025-03-20');


-- Datos nuevos para realizar las Query
INSERT INTO Clientes VALUES
(4, 'Javier Mendoza', '555-9235' , 'javier@mail.com', 'Calle 251');

INSERT INTO Clientes VALUES 
(5, 'María Rodríguez', '555-3456', 'maria@mail.com', 'Calle 321'),
(6, 'Pedro Martínez', '555-7890', 'pedro@mail.com', 'Calle 654'),
(7, 'Ana López', '555-2468', 'ana@mail.com', 'Calle 987'),
(8, 'Diego Fernández', '555-1357', 'diego@mail.com', 'Calle 159'),
(9, 'Carmen Torres', '555-8024', 'carmen@mail.com', 'Calle 753'),
(10, 'Roberto Silva', '555-4681', 'roberto@mail.com', 'Calle 842');

INSERT INTO Alquileres VALUES
(4, 4, 2, '2025-08-20', '2025-08-26');
INSERT INTO Alquileres VALUES
(5, 3, 1, '2025-07-05', '2025-07-10'),
(6, 1, 3, '2025-07-12', '2025-07-15'),
(7, 7, 2, '2025-07-18', '2025-07-22'),
(8, 2, 1, '2025-07-25', '2025-07-30'),
(9, 9, 3, '2025-08-02', '2025-08-06'),
(10, 5, 2, '2025-08-08', '2025-08-12'),
(11, 1, 1, '2025-08-15', '2025-08-18'),
(12, 8, 3, '2025-08-22', '2025-08-25'),
(13, 4, 2, '2025-09-01', '2025-09-05'),
(14, 6, 1, '2025-09-08', '2025-09-14'),
(15, 10, 3, '2025-09-16', '2025-09-20'),
(16, 3, 2, '2025-09-23', '2025-09-28'),
(17, 7, 1, '2025-10-02', '2025-10-06'),
(18, 2, 3, '2025-10-10', '2025-10-13'),
(19, 9, 2, '2025-10-15', '2025-10-19'),
(20, 5, 1, '2025-10-22', '2025-10-26');

INSERT INTO Pagos VALUES
(5, 5, 210.00, '2025-04-12'),
(6, 6, 105.00, '2025-04-18'),
(7, 7, 168.00, '2025-05-07'),
(8, 8, 120.00, '2025-05-14'),
(9, 9, 245.00, '2025-06-09'),
(10, 10, 140.00, '2025-06-20'),
(11, 11, 150.00, '2025-07-10');

-- Consultas

-- Consulta 1: Mostrar el nombre, telefono y email de todos los clientes que tienen un alquiler activo
-- (es decir, cuya fecha actual esté dentro del rango entre fecha_inicio y fecha_fin).

SELECT nombre, telefono, email FROM Clientes
WHERE id_cliente IN (
    SELECT id_cliente FROM Alquileres
    WHERE fecha_inicio <= CURDATE() AND fecha_fin >= CURDATE()
);

-- Consulta 2: Mostrar los vehículos que se alquilaron en el mes de marzo de 2025.
-- Debe mostrar el modelo, marca, y precio_dia de esos vehículos.

SELECT modelo, marca, precio_dia FROM Vehiculos
WHERE id_vehiculo IN (
    SELECT id_vehiculo FROM Alquileres
    WHERE MONTH(fecha_inicio) = 3 AND YEAR(fecha_inicio) = 2025
);


-- Consulta 3: Calcular el precio total del alquiler para cada cliente, considerando el número de días que alquiló el vehículo
-- (el precio por día de cada vehículo multiplicado por la cantidad de días de alquiler).

SELECT  Alquileres.id_alquiler, Alquileres.id_vehiculo, SUM(Vehiculos.precio_dia * DATEDIFF(Alquileres.fecha_fin, Alquileres.fecha_inicio)) AS precio_total
FROM Alquileres
INNER JOIN Vehiculos ON Alquileres.id_vehiculo = Vehiculos.id_vehiculo
GROUP BY Alquileres.id_alquiler, Alquileres.id_vehiculo

-- Consulta 4: Encontrar los clientes que no han realizado ningún pago (no tienen registros en la tabla Pagos).
-- Muestra su nombre y email.

SELECT Clientes.nombre, Clientes.email FROM Clientes
JOIN Alquileres ON Clientes.id_cliente = Alquileres.id_cliente
LEFT JOIN Pagos ON Alquileres.id_alquiler = Pagos.id_alquiler
WHERE Pagos.id_alquiler IS NULL;

-- Consulta 5: Calcular el promedio de los pagos realizados por cada cliente.
-- Muestra el nombre del cliente y el promedio de pago.

SELECT Clientes.nombre, AVG(Pagos.monto) AS promedio_pago
FROM Clientes
JOIN Alquileres ON Clientes.id_cliente = Alquileres.id_cliente
JOIN Pagos ON Alquileres.id_alquiler = Pagos.id_alquiler
GROUP BY Clientes.id_cliente


-- Consulta 6: Mostrar los vehículos que están disponibles para alquilar en una fecha específica
-- (por ejemplo, 2025-03-18). Debe mostrar el modelo, marca y precio_dia. Si el vehículo está ocupado, no se debe incluir.

SELECT * FROM Vehiculos
WHERE id_vehiculo NOT IN (
    SELECT id_vehiculo FROM Alquileres
    WHERE fecha_inicio <= '2025-08-24' AND fecha_fin >= '2025-08-25'
);


-- Consulta 7: Encontrar la marca y el modelo de los vehículos que se alquilaron más de una vez en el mes de marzo de 2025.

SELECT marca, modelo FROM Vehiculos
WHERE id_vehiculo IN (
    SELECT id_vehiculo FROM Alquileres
    WHERE MONTH(fecha_inicio) = 3 AND YEAR(fecha_inicio) = 2025
    GROUP BY id_vehiculo
    HAVING COUNT(*) > 1
)


-- Consulta 8: Mostrar el total de monto pagado por cada cliente.
-- Debe mostrar el nombre del cliente y la cantidad total de pagos realizados (suma del monto de los pagos).

SELECT Clientes.nombre, SUM(Pagos.monto) AS total_pagado
FROM Clientes
JOIN Alquileres ON Clientes.id_cliente = Alquileres.id_cliente
JOIN Pagos ON Alquileres.id_alquiler = Pagos.id_alquiler
GROUP BY Clientes.id_cliente


-- Consulta 9: Mostrar los clientes que alquilaron el vehículo Ford Focus (con id_vehiculo = 3).
-- Debe mostrar el nombre del cliente y la fecha del alquiler.

SELECT Clientes.nombre, Alquileres.fecha_inicio
FROM Clientes
JOIN Alquileres ON Clientes.id_cliente = Alquileres.id_cliente
WHERE Alquileres.id_vehiculo = 3


-- Consulta 10: Realizar una consulta que muestre el nombre del cliente y el total de días alquilados de cada cliente, ordenado de mayor a menor total de días.
-- El total de días es calculado como la diferencia entre fecha_inicio y fecha_fin.

SELECT nombre FROM Clientes
JOIN Alquileres ON Clientes.id_cliente = Alquileres.id_cliente
ORDER BY DATEDIFF(Alquileres.fecha_fin, Alquileres.fecha_inicio) DESC

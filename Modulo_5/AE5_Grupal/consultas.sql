drop database if exists M5_AE5_Grupal;

CREATE DATABASE M5_AE5_Grupal;

USE M5_AE5_Grupal;

CREATE TABLE articulos
(
  id_articulos INT          NOT NULL AUTO_INCREMENT,
  descripcion  VARCHAR(100) NOT NULL,
  tipo         VARCHAR(100) NOT NULL,
  cantidad     INT          NOT NULL,
  precio       INT          NOT NULL,
  PRIMARY KEY (id_articulos)
);

ALTER TABLE articulos
  ADD CONSTRAINT UQ_id_articulos UNIQUE (id_articulos);

CREATE TABLE clientes
(
  id_cliente INT          NOT NULL AUTO_INCREMENT,
  nombre     VARCHAR(100) NOT NULL,
  apellido   VARCHAR(100) NOT NULL,
  direccion  VARCHAR(100) NOT NULL,
  telefono   VARCHAR(15)  NOT NULL,
  correo     VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_cliente)
);

ALTER TABLE clientes
  ADD CONSTRAINT UQ_id_cliente UNIQUE (id_cliente);

ALTER TABLE clientes
  ADD CONSTRAINT UQ_telefono UNIQUE (telefono);

ALTER TABLE clientes
  ADD CONSTRAINT UQ_correo UNIQUE (correo);

CREATE TABLE pedido
(
  id_pedido    INT NOT NULL AUTO_INCREMENT,
  id_cliente   INT NOT NULL,
  id_articulos INT NOT NULL,
  precio_total INT NOT NULL,
  PRIMARY KEY (id_pedido)
);

CREATE TABLE solicitudes
(
  id_solicitud    INT      NOT NULL AUTO_INCREMENT,
  id_pedido       INT      NOT NULL,
  id_vehiculo     INT      NOT NULL,
  fecha_solicitud DATETIME NOT NULL,
  fecha_retiro    DATETIME NULL    ,
  PRIMARY KEY (id_solicitud)
);

ALTER TABLE solicitudes
  ADD CONSTRAINT UQ_id_solicitud UNIQUE (id_solicitud);

CREATE TABLE vehiculo
(
  id_vehiculo INT          NOT NULL AUTO_INCREMENT,
  modelo      VARCHAR      NOT NULL,
  patente     VARCHAR      NOT NULL,
  capacidad   DECIMAL(8,2) NOT NULL,
  disponible  BOOLEAN      NOT NULL,
  PRIMARY KEY (id_vehiculo)
);

ALTER TABLE vehiculo
  ADD CONSTRAINT UQ_patente UNIQUE (patente);

ALTER TABLE pedido
  ADD CONSTRAINT FK_clientes_TO_pedido
    FOREIGN KEY (id_cliente)
    REFERENCES clientes (id_cliente);

ALTER TABLE pedido
  ADD CONSTRAINT FK_articulos_TO_pedido
    FOREIGN KEY (id_articulos)
    REFERENCES articulos (id_articulos);

ALTER TABLE solicitudes
  ADD CONSTRAINT FK_vehiculo_TO_solicitudes
    FOREIGN KEY (id_vehiculo)
    REFERENCES vehiculo (id_vehiculo);

ALTER TABLE solicitudes
  ADD CONSTRAINT FK_pedido_TO_solicitudes
    FOREIGN KEY (id_pedido)
    REFERENCES pedido (id_pedido);


CREATE SCHEMA `cupabuger_v2` ;



-- Crear la tabla Roles
CREATE TABLE Cargo (
    ID_Cargo INT PRIMARY KEY,
    Rango VARCHAR(50) NOT NULL Unique
);

-- Crear la tabla Empleados
CREATE TABLE Empleados (
    ID_Empleado INT UNIQUE PRIMARY KEY NOT NULL,
    Nombre VARCHAR(45) NOT NULL,
    Apellido VARCHAR(45) NOT NULL,
    Teléfono VARCHAR(20) NOT NULL,
    Fecha_Contratación TIMESTAMP NOT NULL,
    ID_Cargo INT NOT NULL,
    Usuario varchar(50) NOT NULL,
    Contraseña varchar(255) NOT NULL,
    FOREIGN KEY (ID_Cargo) REFERENCES Cargo(ID_Cargo)
);

-- Crear la tabla Clientes
CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY NOT NULL UNIQUE,
    Nombre VARCHAR(45) NOT NULL,
    Apellido VARCHAR(45) NOT NULL,
    Dirección_Entrega VARCHAR(100) NOT NULL,
    Teléfono VARCHAR(10) NOT NULL,
    Fecha_de_Registro TIMESTAMP NOT NULL,
    Tipo_de_Cliente VARCHAR(10) NOT NULL
);

-- Crear la tabla Productos
CREATE TABLE Productos (
    ID_Producto INT PRIMARY KEY UNIQUE,
    Nombre_Producto VARCHAR(50) NOT NULL,
    Descripción VARCHAR(100) NOT NULL,
    Precio INT NOT NULL,
    Categoría VARCHAR(50) NOT NULL,
    Estado VARCHAR(20) NOT NULL DEFAULT "Disponible"
);

-- Crear la tabla Inventario
CREATE TABLE Inventario (
    inventarioID INT PRIMARY KEY NOT NULL,
    cantidad_disponible INT NOT NULL,
    FOREIGN KEY (inventarioID) REFERENCES Productos(ID_Producto)
);



-- Crear la tabla Pedidos
CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Tipo_pedido VARCHAR(20) NOT NULL,
    DetallePedido VARCHAR(200) NOT NULL,
    Fecha_Hora_Orden TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Dirección_Entrega VARCHAR(100) NOT NULL,
    Total INT NOT NULL,
    Estado_Orden VARCHAR(50) NOT NULL DEFAULT "Preparando",
    Método_Pago VARCHAR(20) NOT NULL DEFAULT "Efectivo"
);


-- Crear la tabla Pedido Cocina
CREATE TABLE Pedido_Cocina (
    ID_Pedido_Cocina INT AUTO_INCREMENT PRIMARY KEY NOT NULL
);


-- Crear la tabla control monetario
CREATE TABLE Control_Monetario (
    Fecha_Dia TIMESTAMP NOT NULL,
    Monto INT NOT NULL,
    Descripción VARCHAR(200) NOT NULL,
    Ingresos_Diarios INT NOT NULL,
    FOREIGN KEY (Fecha_Dia) REFERENCES Pedidos(PedidoID)
);





-- :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

-- RELACIONES-- Tabla clientes se relaciona con tabla Pedidos
ALTER TABLE Pedidos ADD CONSTRAINT FK_Pedidos_Clientes FOREIGN KEY (PedidoID) REFERENCES Clientes (ID_Cliente);

-- Tabla Productos se relaciona con tabla Pedidos
ALTER TABLE Pedidos ADD CONSTRAINT FK_Pedidos_Productos FOREIGN KEY (PedidoID) REFERENCES Productos (ID_Producto);

-- Tabla Productos se relaciona con tabla Inventario
ALTER TABLE Inventario ADD CONSTRAINT FK_Inventario_Productos FOREIGN KEY (inventarioID) REFERENCES Productos (ID_Producto);

-- -- Tabla Control_Monetario se relaciona con tabla Pedidos
-- ALTER TABLE Control_Monetario-- ADD CONSTRAINT FK_Control_Monetario_Pedidos-- FOREIGN KEY (ID_Pedido) REFERENCES Pedidos (ID_Pedido);

-- Tabla Pedidos se relaciona con tabla Pedido_Cocina
ALTER TABLE Pedido_CocinaADD CONSTRAINT FK_Pedido_Cocina_PedidosFOREIGN KEY (ID_Pedido_Cocina) REFERENCES Pedidos (PedidoID);

-- Tabla empleados se relaciona con tabla Pedidos
ALTER TABLE PedidosADD CONSTRAINT FK_Pedidos_EmpleadosFOREIGN KEY (PedidoID) REFERENCES Empleados (ID_Empleado);

-- -- Tabla Cargo se relaciona con tabla Empleados
-- ALTER TABLE Empleados-- ADD CONSTRAINT FK_Empleados_Cargo-- FOREIGN KEY (ID_Cargo) REFERENCES Cargo (ID_Cargo);

-- Tabla empleados se relaciona con tabla pedido_cocina
ALTER TABLE Pedido_CocinaADD CONSTRAINT FK_Pedido_Cocina_EmpleadosFOREIGN KEY (ID_Pedido_Cocina) REFERENCES Empleados (ID_Empleado);
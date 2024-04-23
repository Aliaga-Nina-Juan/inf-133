import sqlite3

conn = sqlite3.connect("personal.db")

#CREACION DE TABLAS 

try:
    conn.execute(
        """
        CREATE TABLE CARGOS
        (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            nivel TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARGOS ya ha sido creada")

try:
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL    
        ); 
        """
    )
except sqlite3.OperationalError:
    print("La tabla DEPARTAMENTOS ya ha sido creada")
    
try:    
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (
            id INTEGER PRIMARY KEY,
            nombres TEXT NOT NULL,
            apellido_paterno TEXT NOT NULL,
            apellido_materno TEXT NOT NULL,
            fecha_contratacion DATE NOT NULL,
            departamento_id INTEGER NOT NULL,
            cargo_id INTEGER NOT NULL,
            FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
            FOREIGN KEY (cargo_id) REFERENCES CARGOS(id)
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla EMPLEADOS ya ha sido creada")
    
try:
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (
            id INTEGER PRIMARY KEY,
            salario REAL NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_fin DATE NOT NULL,
            fecha_creacion TEXT NOT NULL,
            empleado_id INTEGER NOT NULL,
            FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id)
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla SALARIOS ya ha sido creada")

#Añadiendo DEPARTAMENTOS
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre,fecha_creacion)
    VALUES('Ventas','10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre,fecha_creacion)
    VALUES('Marketing','11-04-2020')
    """
)

#Añadiendo CARGOS
conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
    VALUES('Gerente de ventas','Senior','10-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
    VALUES('Analista de Marketing','Junior','11-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion)
    VALUES('Representante de Ventas','Junior','12-04-2020')
    """
)

#Insertanto nuevos EMPLEADOS

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,departamento_id,cargo_id)
    VALUES('Juan','Gonzales','Perez','15-05-2023',1,1)
    """
)
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,departamento_id,cargo_id)
    VALUES('Maria','Lopez','Martines','20-06-2023',2,2)
    """
)

#Insertar SALARIOS
conn.execute(
    """
    INSERT INTO SALARIOS(salario,fecha_inicio,fecha_fin,fecha_creacion,empleado_id)
    VALUES(3000,'2024-04-01','30-04-2025','30-01-2021',1)
    """
)
conn.execute(
    """
    INSERT INTO SALARIOS(salario,fecha_inicio,fecha_fin,fecha_creacion,empleado_id)
    VALUES(3500,'01-07-2023','30-04-2024','30-01-2021',2)
    """
)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres , SALARIOS.salario
    FROM  EMPLEADOS
    JOIN SALARIOS  ON EMPLEADOS.id == SALARIOS.empleado_id
    """
)
for row in cursor:
    print(row)


print("Nombres, nombre del departamento, nombre del cargo ")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres ,DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM  EMPLEADOS
    JOIN SALARIOS  ON EMPLEADOS.id == SALARIOS.empleado_id
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id == DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id == CARGOS.id
    """
)

for row in cursor:
    print(row)
    
print("nombres , nombre_departamento, nombre_cargo, salario")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario
    FROM EMPLEADOS
    JOIN SALARIOS ON EMPLEADOS.id == SALARIOS.empleado_id
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id == DEPARTAMENTOS.id 
    JOIN CARGOS ON EMPLEADOS.cargo_id == CARGOS.id
    """
)
for row in cursor:
    print(row)


#CAMBIANDO CARGO DE MARIA
conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = 3
    WHERE id = 2
    """
)

print("\nnombres , nombre_departamento, nombre_cargo, salario")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario
    FROM EMPLEADOS
    JOIN SALARIOS ON EMPLEADOS.id == SALARIOS.empleado_id
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id == DEPARTAMENTOS.id 
    JOIN CARGOS ON EMPLEADOS.cargo_id == CARGOS.id
    """
)
for row in cursor:
    print(row)
#CAMBIO DE SALARIO A MARIA
conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)
print("\nnombres , nombre_departamento, nombre_cargo, salario")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario
    FROM EMPLEADOS
    JOIN SALARIOS ON EMPLEADOS.id == SALARIOS.empleado_id
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id == DEPARTAMENTOS.id 
    JOIN CARGOS ON EMPLEADOS.cargo_id == CARGOS.id
    """
)
for row in cursor:
    print(row)

conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)
conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)

print("\nnombres , nombre_departamento, nombre_cargo, salario")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario
    FROM EMPLEADOS
    JOIN SALARIOS ON EMPLEADOS.id == SALARIOS.empleado_id
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id == DEPARTAMENTOS.id 
    JOIN CARGOS ON EMPLEADOS.cargo_id == CARGOS.id
    """
)
for row in cursor:
    print(row)

#Adicionar nuevo empleado
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres,apellido_paterno,apellido_materno,fecha_contratacion,departamento_id,cargo_id)
    VALUES('Carlos','Sanches','Rodriguez','09-04-2024',1,3)
    """
)
#Adicionar salario
conn.execute(
    """
    INSERT INTO SALARIOS(salario,fecha_inicio,fecha_fin,fecha_creacion,empleado_id)
    VALUES(3500,'05-05-2023','05-12-2024','04-12-2025',2)
    """
)


print("Los empleados finales son:")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres,DEPARTAMENTOS.nombre,CARGOS.nombre,SALARIOS.salario
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id == DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id == CARGOS.id
    JOIN SALARIOS ON EMPLEADOS.id == SALARIOS.empleado_id
    """
)
for row in cursor:
    print(row)

conn.commit()

conn.close()
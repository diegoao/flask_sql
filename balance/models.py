from datetime import date
import sqlite3


"""
SELECT ID, FECHA,  CONCEPTO, TIPO, CANTIDAD FROM movimientos
"""


class DBManager:
    """
    Clase para interactuar con la base de datos SQlite
    """

    def __init__(self, ruta):
        self.ruta = ruta

    def conectar(self):
        # 1. Conectar a la nase de datos
        conexion = sqlite3.connect(self.ruta)
        # 2. Abrir cursor
        cursor = conexion.cursor()
        return conexion, cursor

    def desconectar(self, conexion):
        conexion.close()

    def consultaSQL(self, consulta):

        # 1. Conectar a la nase de datos
        conexion = sqlite3.connect(self.ruta)

        # 2. Abrir cursor
        cursor = conexion.cursor()

        # 3. Ejecutar la consulta
        cursor.execute(consulta)

        # 4. Tratar los datos
        # 4.1 Obtener los datos
        datos = cursor.fetchall()  # le decimos que recoja todos los datos en una lista

        # 4.2 Los guardo localmente
        self.registros = []
        nombres_columna = []
        for columna in cursor.description:  # nos da info sobre cada columna que nos ha devuelto
            nombres_columna.append(columna[0])  # nombres de la columna

        for dato in datos:  # recorremos las tuplas que nos ha dado el cursor
            movimiento = {}  # generamos diccionario vacío
            indice = 0
            for nombre in nombres_columna:  # recorremos los nombres de columna
                movimiento[nombre] = dato[indice]
                indice += 1
            self.registros.append(movimiento)

        # 5. Cerrar la conexión
        conexion.close()  # cerramos la conexión es muy importante

        # 6. Devolver los resultados

        return self.registros

    def borrar(self, id):
        """
        DELETE FROM movimientos WHERE id = ?
        """
        sql = 'DELETE FROM movimientos WHERE id=?'
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()

        resultado = False
        try:
            # se añade coma para que lo detecte como tupla
            cursor.execute(sql, (id,))
            conexion.commit()  # se hace para guardar la ultima operacion
            resultado = True
        except:
            conexion.rollback()  # dejamos todo como estaba antes de hacer el execute si hay error

        conexion.close()

        return resultado

    def obtenerMovimiento(self, id):
        consulta = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos WHERE id=?'

        conexion, cursor = self.conectar()
        cursor = conexion.cursor()
        #  Le pasamos el parámetro que queremos en la consulta
        cursor.execute(consulta, (id,))
        datos = cursor.fetchone()  # Cogemos solo un elemento si queremos todos fetchall
        resultado = None
        if datos:
            nombres_columna = []
            for columna in cursor.description:  # nos da info sobre cada columna que nos ha devuelto
                nombres_columna.append(columna[0])  # nombres de la columna
                movimiento = {}  # generamos diccionario vacío
            indice = 0
            for nombre in nombres_columna:  # recorremos los nombres de columna
                movimiento[nombre] = datos[indice]
                indice += 1
            movimiento['fecha'] = date.fromisoformat(movimiento['fecha'])
            resultado = movimiento
        self.desconectar(conexion)
        return resultado

    # se hace generica para sustituir el borrar
    def consultaConParametros(self, consulta, params):
        conexion, cursor = self.conectar()

        resultado = False
        try:
            cursor.execute(consulta, params)
            conexion.commit
            resultado = True
        except Exception as ex:
            print(ex)
            conexion.rollback()  # Volver atrás si hay un error
        self.desconectar(conexion)
        return resultado

    def guardar(self):

        # consulta = 'INSERT INTO movimientos (fecha,concepto,tipo,cantidad) VALUES (2023-10-07,Hamburguesa,,24)'
        conexion, cursor = self.conectar()
        cursor = conexion.cursor()
        #  Le pasamos el parámetro que queremos en la consulta
        # cursor.execute(consulta)

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

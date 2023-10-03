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
        self.movimientos = []
        nombres_columna = []
        for columna in cursor.description:  # nos da info sobre cada columna que nos ha devuelto
            nombres_columna.append(columna[0])  # nombres de la columna

        for dato in datos:  # recorremos las tuplas que nos ha dado el cursor
            movimiento = {}  # generamos diccionario vacío
            indice = 0
            for nombre in nombres_columna:  # recorremos los nombres de columna
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        # 5. Cerrar la conexión
        conexion.close()  # cerramos la conexión es muy importante

        # 6. Devolver los resultados

        return nombres_columna

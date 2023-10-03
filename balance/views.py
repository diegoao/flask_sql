
from flask import render_template
from . import app, RUTA
from .models import DBManager


@app.route('/')
def home():
    db = DBManager(RUTA)
    sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
    movimientos = db.consultaSQL(sql)
    return render_template('inicio.html', movs=movimientos)

# - Función borrar
# - Operar con la BD
# - Botón de borrado en cada movimiento
# - Plantilla con el resultado


# le decimos que nos viene un parametro id  se lo pasamos a la plantilla
@app.route('/borrar/<int:id>')
def eliminar(id):
    db = DBManager(RUTA)
    ha_ido_bien = db.borrar(id)
    return render_template('borrado.html', resultado=ha_ido_bien)

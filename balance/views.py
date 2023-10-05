

from flask import render_template, request

from . import RUTA, app
from .forms import MovimientoForm
from .models import DBManager


@app.route('/')
def home():
    db = DBManager(RUTA)
    sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
    movimientos = db.consultaSQL(sql)
    return render_template('inicio.html', movs=movimientos)


# - Función borrar  -- DONE
# - Operar con la BD -- DONE
# - Botón de borrado en cada movimiento -- DONE
# - Plantilla con el resultado -- DONE

@app.route('/borrar/<int:id>')
def eliminar(id):
    db = DBManager(RUTA)
    ha_ido_bien = db.borrar(id)
    return render_template('borrado.html', resultado=ha_ido_bien)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def actualizar(id):
    if request.method == 'GET':
        # TODO: obtener el movimiento que se va a editar por su ID
        # SELECT id, fecha, concepto, tipo, cantidad FROM movimientos WHERE id=?
        # TODO: acceder aquí por un enlace en la lista de movimientos
        # (al lado del botón eliminar)
        # db = DBManager(RUTA)
        # ---------------------------------------------------------------------
        # sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos WHERE id=?'
        # sql = f'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos WHERE id={id}'
        # datos = db.consultaSQL(sql)
        # datos = datos[0]
        # datos['fecha'] = date.fromisoformat(datos['fecha'])
        # movimiento = datos
        # Mi metodo tiene problema de seguridad, pueden meter por el id comando de borrar
        # ----------------------------------------------------------------------
        db = DBManager(RUTA)
        movimiento = db.obtenerMovimiento(id)
        formulario = MovimientoForm(data=movimiento)
        return render_template('form_movimiento.html', form=formulario, id=id)
    if request.method == 'POST':
        form = MovimientoForm(datra=request.form)
        if form.validate():
            return "Guardar el movimiento"
        else:
            return "Los datos no son correctos.(Volver al formulario)"
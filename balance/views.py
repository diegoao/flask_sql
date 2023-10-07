from datetime import date

from flask import flash, redirect, render_template, request, url_for

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
    # TODO: en lugar de pintar el mensaje con su propia plantillam usar un mensaje flash  y volver al listado
    # TODO: un poco más dificil? pedir confirmación antes de eliminar un movimiento:
    # - Incluir un texto con la pregunta
    # - Incluir un botón aceptar que hace la eliminación y vuelve al listado(con mensaje flash)
    # - Incluir un botón cancelar que vuelve al inicio sin eliminar el movimiento
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
            db = DBManager(RUTA)
            consulta = 'UPDATE movimientos SET fecha=?, concepto=?, tipo=?, cantidad=? WHERE id=?'
            parametros = (
                form.fecha.data,
                form.concepto.data,
                form.tipo.data,
                float(form.cantidad.data),
                form.id.data
            )
            resultado = db.consultaConParametros(consulta, parametros)
            if resultado:
                flash('El movimiento se ha actualizado correctamente',
                      category="exito")
                return redirect(url_for('home'))
            return "Guardar el movimiento"
        else:
            # TODO: pintar los mensajes de error junto al campo que lo provoca
            errores = []
            for key in form.errors:
                errores.append((key, form.errors[key]))
            return render_template('form_movimiento.html', form=formulario, id=id, errors=errores)


@app.route('/nuevo')
def crear_movimiento():
    # TODO: reutilizar el formulario para crear movimientos nuevo coger el post y el get
    consulta = 'INSERT INTO movimientos (fecha, concepto, tipo, cantidad) VALUES(?,?,?,?)'
    pass

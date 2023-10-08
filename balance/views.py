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
    # TODO: en lugar de pintar en mensaje con su propia plantilla, usar un mensaje flash y volver al listado
    # TODO: un poco más difícil? pedir confirmación antes de eliminar un movimiento:
    #   - Incluir un texto con la pregunta
    #   - Incluir un botón aceptar que hace la eliminación y vuelve al listado (con mensaje flash)
    #   - Incluir un botón cancelar que vuelve al inicio SIN eliminar el movimiento
    return render_template('borrado.html', resultado=ha_ido_bien)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def actualizar(id):
    if request.method == 'GET':
        db = DBManager(RUTA)
        movimiento = db.obtenerMovimiento(id)
        formulario = MovimientoForm(data=movimiento)
        return render_template('form_movimiento.html', form=formulario, id=id)

    if request.method == 'POST':
        form = MovimientoForm(data=request.form)
        if form.validate():
            db = DBManager(RUTA)
            consulta = 'UPDATE movimientos SET fecha=?, concepto=?, tipo=?, cantidad=? WHERE id=? '
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
            return "El movimiento no se ha podido guardar en la base de datos"
        else:
            # TODO: pintar los mensajes de error junto al campo que lo provoca  -> ok
            errores = []
            codigoError = {}
            for key in form.errors:
                errores.append((key, form.errors[key]))
                mens = form.errors[key]
                codigoError[key] = mens[0]

            return render_template('form_movimiento.html', form=form, id=id, errors=errores, coderror=codigoError)


# @app.route('/editar/<str:fecha><str:concepto><str:tipo><float:cantidad>', methods=['GET', 'POST'])
# def crear_movimiento(fecha, concepto, tipo, cantidad):
#     # TODO: reutilizar el formulario para crear movimientos nuevos
#     consulta = 'INSERT INTO movimientos (fecha,concepto,tipo,cantidad) VALUES (?,?,?,?)'
#     pass
@app.route('/nuevo')
def crear_movimiento():
    form = MovimientoForm(data=request.form)
    db = DBManager(RUTA)
    sql = 'SELECT id, fecha, concepto, tipo, cantidad FROM movimientos'
    return render_template('nuevo.html', form=form)

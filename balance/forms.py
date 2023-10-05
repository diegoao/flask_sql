from flask_wtf import FlaskForm
from wtforms import (DateField, DecimalField, HiddenField, RadioField,
                     StringField, SubmitField)
from wtforms.validators import DataRequired, NumberRange


class MovimientoForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha', validators=[
                      DataRequired(message='Debes indicar una fecha')])
    concepto = StringField('Concepto', validators=[DataRequired(
        message='No has especificado un concepto')])
    tipo = RadioField(
        choices=[('I', 'Ingreso'), ('G', 'Gasto')], validators=[DataRequired(message='Debes especificar si es un ingreso o un gasto')])
    cantidad = DecimalField('Cantidad', places=2, validators=[
                            DataRequired(message='No puede haber un movimiento sin cantidad'), NumberRange(min=0.1, message='No se permiten cantidades inferiores a diez centimos ')])

    submit = SubmitField('Guardar')

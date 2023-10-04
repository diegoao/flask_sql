from flask_wtf import FlaskForm
from wtforms import (DateField, DecimalField, HiddenField, RadioField,
                     StringField, SubmitField)


class MovimientoForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha')
    concepto = StringField('Concepto')
    tipo = RadioField(choices=[('I', 'Ingreso'), ('G', 'Gasto')])
    cantidad = DecimalField('Cantidad', places=2)

    submit = SubmitField('Guardar')

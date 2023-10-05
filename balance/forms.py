from flask_wtf import FlaskForm
from wtforms import (DateField, DecimalField, HiddenField, RadioField,
                     StringField, SubmitField)
from wtforms.validators import DataRequired


class MovimientoForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha', validators=[DataRequired()])
    concepto = StringField('Concepto', validators=[DataRequired()])
    tipo = RadioField(
        choices=[('I', 'Ingreso'), ('G', 'Gasto')], validators=[DataRequired()])
    cantidad = DecimalField('Cantidad', places=2, validators=[DataRequired()])

    submit = SubmitField('Guardar')

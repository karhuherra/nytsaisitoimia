from flask_wtf import FlaskForm
from wtforms import StringField, validators, DecimalField

class TyoaikaForm(FlaskForm):
    tyoaika = DecimalField("tyoaika", [validators.NumberRange(min=1)])
 
    class Meta:
        csrf = False


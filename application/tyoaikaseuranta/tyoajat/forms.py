from flask_wtf import FlaskForm
from wtforms import StringField, validators, DecimalField, IntegerField

class TyoaikaForm(FlaskForm):
    tyoaika = DecimalField("tyoaika tunteina", [validators.NumberRange(min=1)])
    projekti_id = IntegerField("projektin id (löydät sen listaa projektit osiosta)", [validators.InputRequired()]) 
    class Meta:
        csrf = False


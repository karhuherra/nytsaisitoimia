from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TyontekijaForm(FlaskForm):
    name = StringField("Tyontekija nimi", [validators.Length(min=2)])
 
    class Meta:
        csrf = False

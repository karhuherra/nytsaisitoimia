from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ProjektiForm(FlaskForm):
    name = StringField("Projekti nimi", [validators.Length(min=2,max=100)])
 
    class Meta:
        csrf = False


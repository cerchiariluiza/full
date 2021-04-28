import json
from ext.db import db
from flask import url_for
from flask_wtf import FlaskForm,widgets
from wtforms_alchemy import Unique,ModelForm
from wtforms.widgets import ListWidget, RadioInput,CheckboxInput
from modules.core.forms import BaseForm

from modules.core.auth.models import User
from wtforms import PasswordField, StringField, SubmitField, ValidationError,SelectField,Form,FloatField,DateField
from wtforms_alchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms import DecimalField, RadioField,FileField,FieldList,FormField,SelectMultipleField, BooleanField,StringField,PasswordField, validators,SelectField,IntegerField,RadioField,HiddenField,TextAreaField
from wtforms.fields.html5 import DateField,EmailField,URLField,IntegerRangeField
from modules.core.messages import *
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField,
    DateField,
    SelectField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    URL
)

# este u é normal?
class PropostasForm(BaseForm):
    cvv = StringField('Id')
    text = TextAreaField('Texto com cartoes', render_kw={"rows": 13, "cols": 11})    
    operador = SelectField(
        'Analista',
        [DataRequired()],
        choices=[
            ('Luciano', 'Luciano'),
            ('Priscila', 'Priscila'),
            ('Bira', 'Bira'),
            ('Fernanda', 'Fernanda'),
            ('Daniel', 'Daniel'),
  
        ] 

    )  

class PropostasPesquisaForm(FlaskForm):
    cvv = StringField('Cartão',validators=[validators.DataRequired(),validators.Length(min=16,max=16,message="MINIMO 16 MONGO")],render_kw={'type':'number'})
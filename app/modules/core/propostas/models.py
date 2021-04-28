from flask import url_for
from ext.db import db
from sqlalchemy.ext.orderinglist import ordering_list
from flask_wtf import FlaskForm,widgets
from sqlalchemy.ext.mutable import MutableList
from modules.core.models import BaseModels


class Propostas(db.Model):
    
    __bind_key__ = 'regex_cartoes'
    id = db.Column(db.Integer, primary_key=True)
    
    
    text = db.Column(db.String(10000))   
    operador = db.Column(db.String(1000))   
  

class Propostas2(db.Model):
    
    __bind_key__ = 'temp'
    id = db.Column(db.Integer, primary_key=True)   
    
    text = db.Column(db.String(10000))   
    # cvv = db.Column(db.String(1000)) 
    operador = db.Column(db.String(1000))   
  
 

    
  




   
    
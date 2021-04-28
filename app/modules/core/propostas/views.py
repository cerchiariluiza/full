from ext.db import db
import requests,json
from flask_wtf import FlaskForm,widgets
from functools import wraps
from modules.core.propostas.models import Propostas
from modules.core.propostas.forms import PropostasForm,PropostasPesquisaForm

from flask_security.decorators import roles_required,roles_accepted
from flask import render_template, request, jsonify,redirect,url_for,flash,g,abort ,current_app as app
from modules.core.messages import *


routes = []


def propostas():
    return render_template("propostas/listas.html", lista=Propostas.query.all())


      
@roles_accepted('admin','estagiario')
def propostas():
    return render_template("propostas/listas.html", lista=Propostas.query.all()) 


@roles_accepted('admin','estagiario')
def propostas_busca_cartao():
    lista = Propostas.query.filter().limit(20).all()
    form = PropostasPesquisaForm()
    if form.validate_on_submit():
        q = Propostas.query.filter()
        q = (q,q.filter(Propostas.text ==form.cvv.data))[form.cvv.data not in ['',None]]
        lista = q.limit(20).all()
        return render_template('propostas/listas.html',form=form,lista=lista)
    return render_template('propostas/listas.html',form=form,lista= lista)



@roles_accepted('admin', 'estagiario')
def nova_proposta():
    form = PropostasForm()
    if form.validate_on_submit():
        obj  = Propostas()
        form.populate_obj(obj)
        db.session.add(obj)
        db.session.commit()
        MESSAGES.CADASTRADO_COM_SUCESSO('Propostas')
        return redirect(url_for('core.nova_proposta'))
    return render_template('propostas/form.html',form=form)

@roles_accepted('admin','estagiario')
def proposta_edicao(id):
    obj = Propostas.query.filter_by(id=id).first_or_404()
    form = PropostasForm(obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        MESSAGES.ATUALIZADO_COM_SUCESSO('Proposta')
    return render_template('propostas/form.html', form=form)
#tem estagiario?
routes.append(dict(rule='propostas/',view_func=propostas, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='proposta/',view_func=nova_proposta, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='proposta/<int:id>',view_func=proposta_edicao, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='proposta/proposta-busca-cartao/',view_func=propostas_busca_cartao, options=dict(methods=['GET','POST'])))
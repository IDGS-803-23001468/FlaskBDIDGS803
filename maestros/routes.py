from . import maestros
from flask import render_template, request, redirect, url_for
from models import db
from models import Maestros
import forms


@maestros.route('/maestros', methods=['GET', 'POST'])
def listado_maestros():
    create_form = forms.MaestroForm(request.form)
    lista_maestros = Maestros.query.all()
    return render_template("maestros/maestros.html",
                           form=create_form,
                           maestros=lista_maestros)


@maestros.route("/crear", methods=['GET', 'POST'])
def crear():
    create_form = forms.MaestroForm(request.form)

    if request.method == 'POST':
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))

    return render_template("maestros/crear.html", form=create_form)


@maestros.route("/detallesm", methods=['GET', 'POST'])
def detallesm():
    create_form = forms.MaestroForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        maes1 = Maestros.query.get(id)

        return render_template("maestros/detallesm.html",
                               form=create_form,
                               nombre=maes1.nombre,
                               apellidos=maes1.apellidos,
                               email=maes1.email,
                               especialidad=maes1.especialidad)


@maestros.route("/modificarm", methods=['GET', 'POST'])
def modificarm():
    create_form = forms.MaestroForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        maes1= Maestros.query.get(id)

        create_form.matricula.data = maes1.matricula 
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.email.data = maes1.email
        create_form.especialidad.data = maes1.especialidad

    if request.method == 'POST':
        id = create_form.matricula.data
        maes1 = Maestros.query.get(id)

        maes1.nombre = create_form.nombre.data
        maes1.apellidos = create_form.apellidos.data
        maes1.email = create_form.email.data
        maes1.especialidad = create_form.especialidad.data

        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))

    return render_template("maestros/modificarm.html", form=create_form)


@maestros.route("/eliminarm", methods=['GET', 'POST'])
def eliminarm():
    create_form = forms.MaestroForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        maes1 = Maestros.query.get(id)

        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.email.data = maes1.email
        create_form.especialidad.data = maes1.especialidad

    if request.method == 'POST':
        id = create_form.matricula.data
        maes = Maestros.query.get(id)
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.listado_maestros'))

    return render_template("maestros/eliminarm.html", form=create_form)


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"
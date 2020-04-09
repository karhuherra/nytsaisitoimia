from application import app, db
from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for
from application.tyoaikaseuranta.projektit.models import projektit
from application.tyoaikaseuranta.projektit.forms import ProjektiForm

@app.route("/tyoaikaseuranta/projektit/", methods=["GET"])
def projektit_index():
    return render_template("tyoaikaseuranta/projektit/list.html", projektit = projektit.query.all())

@app.route("/tyoaikaseuranta/projektit/new/")
@login_required
def projektit_form():
    return render_template("tyoaikaseuranta/projektit/new.html", form = ProjektiForm())

@app.route("/tyoaikaseuranta/projektit/<projekti_id>/", methods=["POST", "GET"])
@login_required
def projektit_aseta_valmiiksi(projekti_id):

    p = projektit.query.get(projekti_id)
    p.valmis = True
    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("projektit_index"))

@app.route("/tyoaikaseuranta/projektit/<projekti_id>/poista", methods=["POST","GET"])
@login_required
def projektit_poista(projekti_id):

    p = projektit.query.get(projekti_id)
    db.session().delete(p)
    db.session().commit()

    return redirect(url_for("projektit_index"))


@app.route("/tyoaikaseuranta/projektit/", methods=["POST"])
@login_required
def projektit_create():
    form  = ProjektiForm(request.form)

    if not form.validate():
        return render_template("tyoaikaseuranta/projektit/new.html", form = form)

    p = projektit(form.name.data)

    db.session().add(p)
    db.session().commit()
    return redirect(url_for("projektit_index"))

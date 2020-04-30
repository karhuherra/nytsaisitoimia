from application import app, db
from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for
from application.tyoaikaseuranta.tyoajat.models import tyoajat
from application.tyoaikaseuranta.tyoajat.forms import TyoaikaForm

@app.route("/tyoaikaseuranta/tyoajat/", methods=["GET"])
def tyoajat_index():
    return render_template("tyoaikaseuranta/tyoajat/list.html", tyoajat = tyoajat.query.all(), monta_tuntia=tyoajat.monta_tuntia())

@app.route("/tyoaikaseuranta/tyoajat/new/")
@login_required
def tyoajat_form():
    return render_template("tyoaikaseuranta/tyoajat/new.html", form = TyoaikaForm())

@app.route("/tyoaikaseuranta/tyoajat/", methods=["POST"])
@login_required
def tyoajat_create():
    form  = TyoaikaForm(request.form)

    if not form.validate():
        return render_template("tyoaikaseuranta/tyoajat/new.html", form = form)

    t = tyoajat(form.tyoaika.data, form.projekti_id.data)
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
    return redirect(url_for("tyoajat_index"))

@app.route("/tyoaikaseuranta/tyoajat/<tyoaika_id>/poista", methods=["POST","GET"])
@login_required
def tyoajat_poista(tyoaika_id):

    t = tyoajat.query.get(tyoaika_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("tyoajat_index"))


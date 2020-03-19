from application import app, db
from flask import render_template, request, redirect, url_for
from application.tyoaikaseuranta.tyontekijat.models import tyontekijat

@app.route("/tyoaikaseuranta/tyontekijat/", methods=["GET"])
def tyontekijat_index():
    return render_template("tyoaikaseuranta/tyontekijat/list.html", tyontekijat = tyontekijat.query.all())

@app.route("/tyoaikaseuranta/tyontekijat/new/")
def tyontekijat_form():
    return render_template("tyoaikaseuranta/tyontekijat/new.html")

@app.route("/tyoaikaseuranta/tyontekijat/<tyontekija_id>/", methods=["POST","GET"])
def tyontekijat_muuta_nimi(tyontekija_id):

    t = tyontekijat.query.get(tyontekija_id)
    t.nimi = "Sauli Niinisto"
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tyontekijat_index"))

@app.route("/tyoaikaseuranta/tyontekijat/", methods=["POST"])
def tyontekijat_create():
    t = tyontekijat(request.form.get("nimi"))

    db.session().add(t)
    db.session().commit()
    return redirect(url_for("tyontekijat_index"))

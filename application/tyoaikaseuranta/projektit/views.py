from application import app, db
from flask import render_template, request, redirect, url_for
from application.tyoaikaseuranta.projektit.models import projektit

@app.route("/tyoaikaseuranta/projektit/", methods=["GET"])
def projektit_index():
    return render_template("tyoaikaseuranta/projektit/list.html", projektit = projektit.query.all())

@app.route("/tyoaikaseuranta/projektit/new/")
def projektit_form():
    return render_template("tyoaikaseuranta/projektit/new.html")

@app.route("/tyoaikaseuranta/projektit/<projekti_id>/", methods=["POST", "GET"])
def projektit_aseta_valmiiksi(projekti_id):

    p = projektit.query.get(projekti_id)
    p.valmis = True
    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("projektit_index"))

@app.route("/tyoaikaseuranta/projektit/", methods=["POST"])
def projektit_create():
    p = projektit(request.form.get("nimi"))

    db.session().add(p)
    db.session().commit()
    return redirect(url_for("projektit_index"))

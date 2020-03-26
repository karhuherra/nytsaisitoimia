from application import db

class projektit(db.Model):
    __tablaname__='projektit'
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(200),nullable=False)
    valmis = db.Column(db.Boolean)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)


    def __init__(self, nimi):
        self.nimi = nimi
        self.valmis = False

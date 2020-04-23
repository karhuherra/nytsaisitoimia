from application import db

class tyoajat(db.Model):
    __tablaname__='tyoajat'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    tyoaika = db.Column(db.Numeric)
    projekti_id = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


    def __init__(self, tyoaika, projekti_id):
        self.tyoaika = tyoaika
        self.projekti_id = projekti_id

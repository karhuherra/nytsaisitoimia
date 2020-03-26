from application import db

class tyoajat(db.Model):
    __tablaname__='tyoajat'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    tyoaika = db.Column(db.Numeric)


    def __init__(self, tyoaika):
        self.tyoaika = tyoaika

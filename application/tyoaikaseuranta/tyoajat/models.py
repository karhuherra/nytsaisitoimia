from application import db
from sqlalchemy.sql import text

class tyoajat(db.Model):
    __tablaname__='tyoajat'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer,nullable=False)
    tyoaika = db.Column(db.Numeric)
    projekti_id = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


    def __init__(self, tyoaika, projekti_id):
        self.tyoaika = tyoaika
        self.projekti_id = projekti_id

    @staticmethod
    def monta_tuntia():
        stmt = text("SELECT account_id, SUM(tyoaika) FROM tyoajat GROUP BY account_id")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0],"tyoaika":row[1]})

        return response


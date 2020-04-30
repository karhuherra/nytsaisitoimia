from application import db
from sqlalchemy.sql import text
class projektit(db.Model):
    __tablaname__='projektit'
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(200),nullable=False)
    valmis = db.Column(db.Boolean)
    projektipaallikko = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi
        self.valmis = False

    @staticmethod
    def monta_hetkea():
        stmt = text("SELECT projekti_id, SUM(tyoaika) FROM tyoajat GROUP BY projekti_id")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0],"tyoaika":row[1]})

        return response


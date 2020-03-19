from application import db

class tyontekijat(db.Model):
    __tablaname__='tyontekijat'
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(200),nullable=False)


    def __init__(self, nimi):
        self.nimi = nimi
        

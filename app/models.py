from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    num_bed= db.Column(db.Integer)
    num_bath= db.Column(db.Integer)
    location = db.Column(db.String(100))
    price=db.Column(db.String(80))
    type= db.Column(db.String(80))
    desc= db.Column(db.String(500))
    filename= db.Column(db.String(80))



    def __init__(self, title,num_bed,num_bath,location,price,type,desc,filename):
        self.title = title
        self.num_bed = num_bed
        self.num_bath= num_bath
        self.location=location
        self.price=price
        self.type=type
        self.desc=desc
        self.filename=filename

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support



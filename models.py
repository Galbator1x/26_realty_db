from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    settlement = db.Column(db.String(100))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    oblast_district = db.Column(db.String(100))
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(255))
    construction_year = db.Column(db.Integer)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean)

    def __str__(self):
        return '{}, {}'.format(self.settlement, self.address)


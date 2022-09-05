from flower_predictor import db

class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable = False)
    colour = db.Column(db.String(100),nullable= False)

    def __repr__(self) -> str:
        return "{self.name}"

def search_flowers_by_colour(colour):
    return Flower.query.filter_by(colour=colour)
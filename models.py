from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

db = SQLAlchemy()

class EnumeratorSubmission(db.Model):
    __tablename__ = 'enumerator_submissions'
    id                = db.Column(db.Integer, primary_key=True)
    enumerator_id     = db.Column(db.String(20), nullable=False)
    enumerator_name   = db.Column(db.String(100), nullable=False)
    region            = db.Column(db.String(100), nullable=False)
    total_respondents = db.Column(db.Integer, nullable=False)
    location          = db.Column(Geometry(geometry_type='POINT', srid=4326))
    timestamp         = db.Column(db.DateTime, server_default=db.func.now())

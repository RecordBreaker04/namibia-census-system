from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # ✅ This is what you're missing

class EnumeratorSubmission(db.Model):
    __tablename__ = 'enumerator_submissions'

    id = db.Column(db.Integer, primary_key=True)
    enumerator_id = db.Column(db.String(20), nullable=False)
    enumerator_name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    total_respondents = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# census_questionnaire_response.py

from models import db

class CensusResponse(db.Model):
    __tablename__ = 'census_responses'
    
    id = db.Column(db.Integer, primary_key=True)
    household_head = db.Column(db.String(100))
    household_size = db.Column(db.Integer)
    region = db.Column(db.String(100))
    income = db.Column(db.String(50))
    water_access = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    # Section A
    constituency = db.Column(db.String(100))
    ea_code = db.Column(db.String(4))
    locality = db.Column(db.String(100))
    household_number = db.Column(db.String(4))
    physical_address = db.Column(db.Text)
    phone = db.Column(db.String(20))
    respondent_name = db.Column(db.String(100))

    # Section B
    housing_type = db.Column(db.String(50))
    housing_type_other = db.Column(db.String(100))
    ownership = db.Column(db.String(50))
    ownership_other = db.Column(db.String(100))
    roof_material = db.Column(db.String(50))
    roof_material_other = db.Column(db.String(100))
    sleeping_rooms = db.Column(db.Integer)

    # Consent
    consent = db.Column(db.Boolean, default=False)


from models import db
from datetime import datetime

class CensusResponse(db.Model):
    __tablename__ = 'census_responses'

    id = db.Column(db.Integer, primary_key=True)
    
    # Basic Demographics
    household_head = db.Column(db.String(100))
    household_size = db.Column(db.Integer)
    region = db.Column(db.String(100))
    income = db.Column(db.String(50))
    water_access = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Section A: Identification Information
    constituency = db.Column(db.String(100))
    ea_code = db.Column(db.String(4))  # 4-digit code
    locality = db.Column(db.String(100))
    household_number = db.Column(db.String(4))  # 4-digit number
    physical_address = db.Column(db.Text)
    phone = db.Column(db.String(20))
    respondent_name = db.Column(db.String(100))

    # Section B: Housing Information
    housing_type = db.Column(db.String(50))
    housing_type_other = db.Column(db.String(100))  # if "Other" selected
    ownership = db.Column(db.String(50))
    ownership_other = db.Column(db.String(100))     # if "Other" selected
    roof_material = db.Column(db.String(50))
    roof_material_other = db.Column(db.String(100)) # if "Other" selected
    sleeping_rooms = db.Column(db.Integer)

    # Consent
    consent = db.Column(db.Boolean, default=False)

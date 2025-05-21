from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from config import SQLALCHEMY_DATABASE_URI
from models import db, EnumeratorSubmission
from census_questionnaire_response import CensusResponse
from geoalchemy2.elements import WKTElement
from sqlalchemy import func



app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
CORS(app)
@app.route('/')
def census_form():
    return render_template('census_form.html')
@app.route('/enumerator')
def enumerator_form():
    return render_template('enumerator.html')

@app.route('/census/submit', methods=['POST'])
def submit_census():
    data = request.form
    response = CensusResponse(
        household_head=data.get('householdHead'),
        household_size=data.get('householdSize'),
        region=data.get('region'),
        income=data.get('income'),
        water_access=data.get('waterAccess'),
        constituency=data.get('constituency'),
        ea_code=data.get('ea_code'),
        locality=data.get('locality'),
        household_number=data.get('household_number'),
        physical_address=data.get('physical_address'),
        phone=data.get('phone'),
        respondent_name=data.get('respondent_name'),
        housing_type=data.get('housing_type'),
        housing_type_other=data.get('housing_type_other'),
        ownership=data.get('ownership'),
        ownership_other=data.get('ownership_other'),
        roof_material=data.get('roof_material'),
        roof_material_other=data.get('roof_material_other'),
        sleeping_rooms=data.get('sleeping_rooms'),
        consent=data.get('consent') == 'on'  # checkbox
    )
    db.session.add(response)
    db.session.commit()
    return "Census data submitted successfully!"

@app.route('/api/submit/', methods=['POST'])
def submit():
    data = request.json

    # Create a PostGIS point geometry
    point = WKTElement(f'POINT({data["longitude"]} {data["latitude"]})', srid=4326)

    submission = EnumeratorSubmission(
        enumerator_id     = data['enumeratorId'],
        enumerator_name   = data['enumeratorName'],
        region            = data['regionName'],
        total_respondents = int(data['totalRespondents']),
        location          = point
    )

    db.session.add(submission)
    db.session.commit()
    return jsonify({"message": "Data saved successfully"}), 201


@app.route('/api/submissions', methods=['GET'])
def get_submissions():
    submissions = db.session.query(
        EnumeratorSubmission.enumerator_name,
        EnumeratorSubmission.region,
        func.ST_Y(EnumeratorSubmission.location).label('latitude'),
        func.ST_X(EnumeratorSubmission.location).label('longitude'),
        EnumeratorSubmission.timestamp
    ).all()

    result = []
    for sub in submissions:
        result.append({
            "enumerator_name": sub.enumerator_name,
            "region": sub.region,
            "latitude": sub.latitude,
            "longitude": sub.longitude,
            "timestamp": sub.timestamp.isoformat() if sub.timestamp else None
        })

    return jsonify(result)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)

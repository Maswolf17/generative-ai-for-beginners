from flask import Blueprint
from flask import request
from flask import jsonify

from detectors import detect
from ai_engine import analyze_security_event

security_bp = Blueprint(
    "security",
    __name__
)

@security_bp.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    data = request.json

    payload = str(data)

    alerts = detect(payload)

    ai_report = analyze_security_event(
        payload
    )

    return jsonify({

        "alerts": alerts,

        "ai_analysis": ai_report
    })
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

# existing Assessment model remains unchanged...

class DeadlineRiskAssessment(db.Model):
    __tablename__ = "deadline_risk_assessments"

    id = db.Column(db.Integer, primary_key=True)

    # Firm basics
    firm_name = db.Column(db.String(255), nullable=False)
    contact_name = db.Column(db.String(255), nullable=False)
    contact_role = db.Column(db.String(255), nullable=True)
    employee_count = db.Column(db.Integer, nullable=True)
    primary_discipline = db.Column(db.String(64), nullable=True)  # Architecture / Civil / Both / Other

    # Section summaries as JSON blobs – mirrors your call prep structure
    software_environment = db.Column(JSON, nullable=True)
    deadline_calendar = db.Column(JSON, nullable=True)
    version_control = db.Column(JSON, nullable=True)
    backup_continuity = db.Column(JSON, nullable=True)
    performance_impressions = db.Column(JSON, nullable=True)

    # Internal post-call fields
    exposure_level = db.Column(db.String(16), nullable=True)  # Low / Medium / High
    specific_risks = db.Column(JSON, nullable=True)          # list of strings
    smb_audit_recommended = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

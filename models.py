from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(100))
    user_id = db.Column(db.String(50))
    amount = db.Column(db.Float)
    status = db.Column(db.String(20))


class PaymentLog(db.Model):
    __tablename__ = "payment_logs"

    log_id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.Integer)
    old_status = db.Column(db.String(20))
    new_status = db.Column(db.String(20))
    reason = db.Column(db.String(100))


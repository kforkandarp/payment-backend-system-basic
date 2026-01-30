from flask import Flask, request, jsonify
from models import db, Payment, PaymentLog
from config import SQLALCHEMY_DATABASE_URI
import random
import uuid
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = Flask(__name__)

# connect flask to database
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/create_payment", methods=["POST"])
def create_payment():
    data = request.json

    txn_id = "TXN-" + str(uuid.uuid4())

    payment = Payment(
    transaction_id=txn_id,
    user_id=data["user_id"],
    amount=data["amount"],
    status="PENDING"
)


    db.session.add(payment)
    db.session.commit()
    logger.info(f"Payment created: {txn_id} for user {data['user_id']} with amount {data['amount']}")


    return jsonify({
        "message": "Payment created",
        "payment_id": payment.id
    })


@app.route("/process_payment/<int:payment_id>", methods=["POST"])
def process_payment(payment_id):
    payment = Payment.query.get(payment_id)
    logger.info(f"Processing payment ID {payment.id} with transaction {payment.transaction_id}")

    old_status = payment.status


    if not payment:
        return jsonify({"error": "Payment not found"}), 404

    max_retries = 3
    attempt = 0
    success = False

    while attempt < max_retries and not success:
        success = random.choice([True, False])
        attempt += 1

    if success:
        payment.status = "SUCCESS"
        reason = "Processed successfully after retry attempts"
    else:
        payment.status = "FAILED"
        reason = "All retry attempts failed"

    log = PaymentLog(
    payment_id=payment.id,
    old_status=old_status,
    new_status=payment.status,
    reason=reason
)

    db.session.add(log)

    db.session.commit()

    return jsonify({
        "payment_id": payment.id,
        "status": payment.status
    })


@app.route("/payments", methods=["GET"])
def get_payments():
    payments = Payment.query.all()

    result = []

    for p in payments:
        result.append({
            "id": p.id,
            "user_id": p.user_id,
            "amount": p.amount,
            "status": p.status
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

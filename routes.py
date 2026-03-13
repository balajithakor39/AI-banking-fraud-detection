from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Account
from ai_fraud_detection import FraudDetector

router = APIRouter()

detector = FraudDetector()
detector.train()

@router.post("/create-account")
def create_account(name: str):

    db: Session = SessionLocal()

    account = Account(name=name, balance=0)

    db.add(account)
    db.commit()

    return {"message":"Account created"}

@router.post("/deposit")
def deposit(account_id:int, amount:float):

    if detector.predict(amount):
        return {"status":"blocked","reason":"fraud suspected"}

    db: Session = SessionLocal()

    account = db.query(Account).filter(Account.id==account_id).first()

    account.balance += amount

    db.commit()

    return {"balance":account.balance}

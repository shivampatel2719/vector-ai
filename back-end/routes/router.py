from fastapi import APIRouter
from schemas.card import CardRequest
from sqlalchemy.orm import Session
from helpers.database import get_db
from models.card import Card
from fastapi import Depends

router = APIRouter()

@router.post('/')
def create_cards(details: CardRequest, db: Session = Depends(get_db)):
    try:
        to_create = Card(
        title=details.title,
        type=details.type,
        position=details.position,
        url=details.url)
        db.add(to_create)
        db.commit()
        return {
            "success": True,
            "created_id": to_create.id
        }
    except Exception as e:
        return {
            "success": False,
            "Error":e
        }

@router.get('/')
def get_all_cards(db: Session = Depends(get_db)):
    try:
        return db.query(Card).filter().all()
    except Exception as e:
        return {
            "success": False,
            "Error":e
        }

@router.patch('/position/{pos1}/{pos2}')
def change_position(pos1: int, pos2:int,db: Session = Depends(get_db)):
    try:
        for u in db.query(Card).filter(Card.position == pos1).all(): 
            id1 = u.__dict__['id']
        for u in db.query(Card).filter(Card.position == pos2).all(): 
            id2 = u.__dict__['id']
        db.query(Card).filter(Card.id == id1).update({'position': pos2})
        db.query(Card).filter(Card.id == id2).update({'position': pos1})
        db.commit()
        return {
            "success": True
        }
    except Exception as e:
        return {
            "success": False,
            "Error":e
        }

@router.delete('/{id}')
def delete_card(id: int,db: Session = Depends(get_db)):
    try:
        db.query(Card).filter(Card.id == id).delete()
        db.commit()
        return {
            "success": True
        }
    except Exception as e:
        return {
            "success": False,
            "Error":e
        }

from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..database import get_db
from ..models.transactions import Transaction
from ..services.transactions import get_flagged_transactions

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/flagged", response_model=list[Transaction])
def flagged_transaction(
    flag: Optional[str] = None,
    target_date: Optional[date] = None,
    tolerance_type: str = "percentage",
    tolerance_value: float = 5,
    db: Session = Depends(get_db),
):
<<<<<<< HEAD
    # active_date = target_date or date.today()
    return get_flagged_transactions(db, target_date or date.today(), flag)
=======
    return get_flagged_transactions(
        db,
        target_date or date.today(),
        flag,
        tolerance_type,
        tolerance_value,
    )
>>>>>>> 9b62df3762500a414bd8216a1b5cef5eeff9d67d


@router.get("/flagged/{flag}", response_model=list[Transaction])
def flagged_transaction_by_type(
    flag: str,
    target_date: Optional[date] = None,
    tolerance_type: str = "percentage",
    tolerance_value: float = 5,
    db: Session = Depends(get_db),
):
    return get_flagged_transactions(
        db,
        target_date or date.today(),
        flag,
        tolerance_type,
        tolerance_value,
    )

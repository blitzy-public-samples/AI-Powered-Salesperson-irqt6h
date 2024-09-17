from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User
from app.schema.user import UserUpdate
from app.core.security import get_current_user

router = APIRouter()

@router.get('/users/me')
def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user

@router.put('/users/me')
def update_user(user_update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(current_user, key, value)
    
    db.commit()
    db.refresh(current_user)
    return current_user

# HUMAN ASSISTANCE NEEDED
# The following improvements might be necessary:
# 1. Add error handling for database operations
# 2. Implement input validation for user_update data
# 3. Add logging for user update operations
# 4. Consider adding rate limiting for update requests
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Quote, QuoteItem
from app.schema.quote import QuoteCreate, QuoteUpdate
from app.services.quote_generator import generate_quote
from app.core.security import get_current_user

router = APIRouter()

@router.post('/quotes')
async def create_quote(quote: QuoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness
    try:
        # Generate quote using quote generator service
        generated_quote = generate_quote(quote.chat_session)
        
        # Create Quote object
        new_quote = Quote(user_id=current_user.id, total_price=generated_quote['total_price'])
        db.add(new_quote)
        db.flush()
        
        # Create QuoteItem objects
        for item in generated_quote['items']:
            quote_item = QuoteItem(
                quote_id=new_quote.id,
                item_name=item['name'],
                quantity=item['quantity'],
                price=item['price']
            )
            db.add(quote_item)
        
        # Add quote and items to database
        db.commit()
        db.refresh(new_quote)
        
        # Return created quote
        return new_quote
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the quote: {str(e)}")

@router.get('/quotes/{quote_id}')
async def get_quote(quote_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Query database for quote
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    
    # Check if quote exists and user has permission
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    if quote.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You don't have permission to access this quote")
    
    # Return quote
    return quote
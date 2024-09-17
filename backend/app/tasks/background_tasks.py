from celery import Celery
from app.core.config import settings
from app.services.nlp_processor import process_user_input
from app.services.rag_engine import retrieve_context
from app.services.quote_generator import generate_quote
from app.db.database import SessionLocal
from app.db.models import ChatSession, Message, Quote

celery_app = Celery('ai_salesperson', broker=settings.CELERY_BROKER_URL)

@celery_app.task
def process_chat_message(session_id: str, message_content: str) -> dict:
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness and error handling
    db = SessionLocal()
    try:
        chat_session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
        if not chat_session:
            raise ValueError(f"Chat session with id {session_id} not found")

        processed_input = process_user_input(message_content)
        context = retrieve_context(processed_input)
        
        # TODO: Implement AI response generation using the processed input and context
        ai_response = "AI response placeholder"  # Replace with actual AI response generation

        user_message = Message(content=message_content, is_user=True, chat_session_id=session_id)
        ai_message = Message(content=ai_response, is_user=False, chat_session_id=session_id)
        
        db.add(user_message)
        db.add(ai_message)
        db.commit()

        return {
            "user_message": message_content,
            "ai_response": ai_response,
            "context": context
        }
    finally:
        db.close()

@celery_app.task
def generate_quote_async(quote_request: dict, user_id: str) -> dict:
    # HUMAN ASSISTANCE NEEDED
    # This function needs review for production readiness, error handling, and input validation
    db = SessionLocal()
    try:
        generated_quote = generate_quote(quote_request)
        
        quote = Quote(
            user_id=user_id,
            product=generated_quote.get('product'),
            price=generated_quote.get('price'),
            details=generated_quote.get('details')
        )
        
        db.add(quote)
        db.commit()
        db.refresh(quote)

        return {
            "quote_id": quote.id,
            "product": quote.product,
            "price": quote.price,
            "details": quote.details
        }
    finally:
        db.close()
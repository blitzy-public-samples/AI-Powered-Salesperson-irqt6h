from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import ChatSession, Message
from app.schema.chat import ChatSessionCreate, MessageCreate
from app.services.nlp_processor import process_user_input
from app.services.rag_engine import retrieve_context
from app.core.security import get_current_user

router = APIRouter()

@router.post('/sessions')
def create_chat_session(session: ChatSessionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_session = ChatSession(user_id=current_user.id, **session.dict())
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@router.post('/sessions/{session_id}/messages')
def add_message_to_session(session_id: str, message: MessageCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # HUMAN ASSISTANCE NEEDED
    # The following code needs review and potential improvements for production readiness
    
    # Verify chat session exists
    chat_session = db.query(ChatSession).filter(ChatSession.id == session_id, ChatSession.user_id == current_user.id).first()
    if not chat_session:
        raise HTTPException(status_code=404, detail="Chat session not found")

    # Process user input
    processed_input = process_user_input(message.content)

    # Retrieve context using RAG
    context = retrieve_context(processed_input)

    # Generate AI response (this step is not clearly defined in the given specification)
    # For now, we'll use a placeholder
    ai_response = f"AI response based on: {processed_input} and context: {context}"

    # Create and save user message
    user_message = Message(session_id=session_id, content=message.content, is_user=True)
    db.add(user_message)

    # Create and save AI response message
    ai_message = Message(session_id=session_id, content=ai_response, is_user=False)
    db.add(ai_message)

    db.commit()
    db.refresh(user_message)
    db.refresh(ai_message)

    return {"user_message": user_message, "ai_message": ai_message}
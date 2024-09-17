from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    content: str
    sender_type: str
    timestamp: datetime

class ChatSession(BaseModel):
    session_id: str
    user_id: str
    messages: List[Message]
    start_time: datetime
    end_time: Optional[datetime]
    status: str
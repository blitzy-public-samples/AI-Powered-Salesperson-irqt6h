from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class QuoteItem(BaseModel):
    item_id: str
    sku_id: str
    quantity: int
    unit_price: float
    total_price: float

class Quote(BaseModel):
    quote_id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    status: str
    total_amount: float
    items: List[QuoteItem]

# HUMAN ASSISTANCE NEEDED
# The confidence level for the Quote class is 0.85, which is below 0.9.
# Please review the Quote class to ensure all fields are correct and complete.
# Consider adding any additional fields or validation that might be necessary for a production-ready model.
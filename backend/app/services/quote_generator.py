from typing import List, Dict
from app.db.models import SKU, Quote, QuoteItem
from app.services.sku_catalog import SKUCatalog
from sqlalchemy.orm import Session

# HUMAN ASSISTANCE NEEDED
# The following code may need further refinement and error handling for production readiness.
# Please review and adjust as necessary.

def generate_quote(requirements: Dict, db_session: Session) -> Quote:
    # Extract part requirements from input
    parts_required = requirements.get('parts', [])
    
    # Query SKU catalog for matching parts
    sku_catalog = SKUCatalog(db_session)
    matching_skus = []
    for part in parts_required:
        sku = sku_catalog.find_matching_sku(part)
        if sku:
            matching_skus.append(sku)
    
    # Calculate pricing based on quantity and any applicable discounts
    total_price = 0
    quote_items = []
    for sku in matching_skus:
        quantity = next((p['quantity'] for p in parts_required if p['name'] == sku.name), 1)
        price = sku.price * quantity
        # Apply discounts (simplified, may need more complex logic)
        if quantity > 10:
            price *= 0.9  # 10% discount for bulk orders
        total_price += price
        quote_items.append(QuoteItem(sku=sku, quantity=quantity, price=price))
    
    # Create Quote and QuoteItem objects
    quote = Quote(total_price=total_price, items=quote_items)
    
    # Save quote to database
    db_session.add(quote)
    db_session.commit()
    
    # Return generated Quote object
    return quote
from spacy import load
from typing import List, Dict
from app.core.config import settings

nlp = load(settings.NLP_MODEL)

# HUMAN ASSISTANCE NEEDED
# The following function needs review and potential improvements for production readiness
def process_user_input(text: str) -> Dict:
    # Tokenize and process input text using spaCy
    doc = nlp(text)
    
    # Extract named entities
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    
    # Determine intent based on processed text
    # This is a simplified intent detection and may need to be improved
    intent = 'unknown'
    if any(token.text.lower() in ['search', 'find', 'look'] for token in doc):
        intent = 'search'
    elif any(token.text.lower() in ['create', 'add', 'new'] for token in doc):
        intent = 'create'
    elif any(token.text.lower() in ['update', 'change', 'modify'] for token in doc):
        intent = 'update'
    elif any(token.text.lower() in ['delete', 'remove'] for token in doc):
        intent = 'delete'
    
    # Return structured NLP data
    return {
        'intent': intent,
        'entities': entities,
        'tokens': [token.text for token in doc],
        'pos_tags': [token.pos_ for token in doc]
    }
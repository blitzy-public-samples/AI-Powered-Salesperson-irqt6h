from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, chat, quotes, users
from app.core.config import settings
from app.db.database import init_db, close_db
from app.services.rag_engine import RAGEngine
from app.services.nlp_processor import NLPProcessor
from app.services.sku_catalog import SKUCatalog

app = FastAPI()

# Global instances
rag_engine: RAGEngine = None
nlp_processor: NLPProcessor = None
sku_catalog: SKUCatalog = None

@app.on_event("startup")
async def startup_event():
    # HUMAN ASSISTANCE NEEDED
    # The confidence level for this function is below 0.8. Please review and adjust as necessary.
    global rag_engine, nlp_processor, sku_catalog
    
    # Initialize database connection
    await init_db()
    
    # Initialize RAG engine
    rag_engine = RAGEngine()
    
    # Initialize NLP processor
    nlp_processor = NLPProcessor()
    
    # Initialize SKU catalog
    sku_catalog = SKUCatalog()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

def get_rag_engine() -> RAGEngine:
    return rag_engine

def get_nlp_processor() -> NLPProcessor:
    return nlp_processor

def get_sku_catalog() -> SKUCatalog:
    return sku_catalog

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(quotes.router)
app.include_router(users.router)
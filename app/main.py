# IMPORTANT: settings must be imported FIRST
from app import settings  # noqa: F401

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from titiler.core.factory import TilerFactory
from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers

app = FastAPI(title="Titiler API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TiTiler router
cog = TilerFactory(router_prefix="/cog")
app.include_router(cog.router)

add_exception_handlers(app, DEFAULT_STATUS_CODES)

@app.get("/health", tags=["System"])
def health():
    return {"status": "ok", "env": settings.APP_ENV}

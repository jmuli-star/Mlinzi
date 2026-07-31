from fastapi.middleware.cors import CORSMiddleware

from .application.app import create_app

CORS_ALLOWED_ORIGINS = [
    "https://mlinzi-theta.vercel.app",
    "https://mlinzi-tau.vercel.app",
    "http://localhost:5173",
]

app = create_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

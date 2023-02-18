from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from the_app.router import router as theapp_router

app = FastAPI()

app = FastAPI(title="The App", version="0.1.0", description="The App API")
origins = [
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(theapp_router, prefix="/api", tags=["api"])

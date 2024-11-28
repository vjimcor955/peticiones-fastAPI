from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import petitionRoutes
from routers import userRoutes

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fastapi-client.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Peticiones FastAPI": "Grupo 3"}

app.include_router(petitionRoutes.router)
app.include_router(userRoutes.router)
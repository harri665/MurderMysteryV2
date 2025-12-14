from fastapi import FastAPI

from .routers import default

app = FastAPI()

# Import routers
app.include_router(router=default.router)

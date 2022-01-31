from routes.user import user
from fastapi import FastAPI

app=FastAPI()

app.include_router(user)

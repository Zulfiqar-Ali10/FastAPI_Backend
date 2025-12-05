from fastapi import FastAPI
from database.connection import Base, engine
from routers.product_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


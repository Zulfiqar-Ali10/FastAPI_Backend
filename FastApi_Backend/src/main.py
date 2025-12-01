from fastapi import FastAPI
from routers import product_router, user_router, order_router

app = FastAPI(title="E-commerce API", version="1.0")

# Include routers
app.include_router(product_router.router)
app.include_router(user_router.router)
app.include_router(order_router.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to E-commerce API"}

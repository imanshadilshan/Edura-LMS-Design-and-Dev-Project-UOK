import uvicorn
from fastapi import FastAPI
from uvicorn import lifespan

app = FastAPI(lifespan=lifespan)

app.add_middleware()

@app.get("/")
async def main():
    return {"service": "payment_service"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
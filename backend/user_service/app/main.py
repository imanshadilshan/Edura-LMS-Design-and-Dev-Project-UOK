from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "fastapi user_services"}

@app.get("/admin/{admin_id}")
async def admin(admin_id: int):
    return {"message": "admin-data"}

@app.put("/admin/{admin_id}")
async def admin(admin_id: int):
    return {"message": "admin-update"}
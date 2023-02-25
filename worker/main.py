from fastapi import FastAPI

app = FastAPI()


@app.get("/", status_code=200)
async def health_check():
    return {"message": "HealthCheck Success"}

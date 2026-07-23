from fastapi import FastAPI

app = FastAPI(
    title="Healthcare Clinic API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Healthcare Backend Running Successfully"}
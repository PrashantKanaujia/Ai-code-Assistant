from fastapi import FastAPI

app = FastAPI(title="AI Repository Engineer")


@app.get("/")
def root():
    return {"message": "Backend is running"}
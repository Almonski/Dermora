from fastapi import FastAPI

app = FastAPI(
    title="Dermora API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Dermora API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
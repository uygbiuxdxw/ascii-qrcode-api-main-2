import uvicorn



if __name__ == "__main__":
    uvicorn.run("main:app", host="https://ascii-qrcode-api.onrender.com", port=8000, log_level="info",reload=True)
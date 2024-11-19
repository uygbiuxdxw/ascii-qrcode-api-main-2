import uvicorn



if __name__ == "__main__":
    uvicorn.run("main:app", host="ascii-qrcode-api.onrender.com", port=8000, log_level="info",reload=True)
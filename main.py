from fastapi import FastAPI

import convert
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/genAsciiQr")
def generate(text):
    asciiQr = convert.generateasciiQR(text, invert=False, white='██', black='  ', version=1, border=1, correction='M')
    return HTMLResponse(content=("<pre>" + asciiQr + "</pre>"), status_code=200)





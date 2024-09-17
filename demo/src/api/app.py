from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from vncorenlp import VnCoreNLP
import re

class FunctionList(BaseModel):
    text: str

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def tach_tu(sentence):
    rdrsegmenter = VnCoreNLP("http://nginx", 80)
    output = rdrsegmenter.tokenize(sentence)
    return output

@app.post("/process")
async def process_text(input: FunctionList):
    output = input.model_dump()["text"]

    output = tach_tu(output)
                
    return {"Kết quả": output}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

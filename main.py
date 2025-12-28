from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from extract import extract_fields

app = FastAPI()

class ExtractRequest(BaseModel):
    text: str

@app.post("/extract")
def extract(request: ExtractRequest):
    try:
        result = extract_fields(request.text)
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
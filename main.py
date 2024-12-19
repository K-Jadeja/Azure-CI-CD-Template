from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
from uuid import uuid4

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile):
    file_extension = file.filename.split('.')[-1]
    if file_extension not in ("png", "jpg", "jpeg"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")
    
    file_id = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, file_id)
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    return {"file_id": file_id, "url": f"/view/{file_id}"}

@app.get("/view/{file_id}")
async def view_file(file_id: str):
    file_path = os.path.join(UPLOAD_DIR, file_id)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

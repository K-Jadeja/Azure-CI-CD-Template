from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from uuid import uuid4
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

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

@app.get("/checkenv")
def check_environment_variables():
    # Return environment variables as a dictionary
    return {"environment_variables": {key: os.getenv(key) for key in os.environ}}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

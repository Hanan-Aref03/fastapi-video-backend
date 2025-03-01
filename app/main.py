# Main FastAPI application

from fastapi import FastAPI, UploadFile, File, HTTPException
from services import save_upload_file, download_video
from pathlib import Path

app = FastAPI()

# Directory to store uploaded files
UPLOAD_DIR = Path("static")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    """Uploads a video file and stores it in the file system."""
    try:
        file_path = await save_upload_file(file)
        return {"message": "Upload successful", "file_path": str(file_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/download/")
async def download_video_from_link(url: str):
    """Downloads a video from a given URL and saves it to the file system."""
    try:
        file_path = await download_video(url)
        return {"message": "Download successful", "file_path": str(file_path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

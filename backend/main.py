from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from decryptor.decrypt import decrypt_file

app = FastAPI()
PORT = 8000

#allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

"""

@app.post("/decrypt")
async def decrypt(file: UploadFile = File(...)):
    result = await decrypt_file(file)
    return {"status": "success", "file_path": result}

@app.post("/convert")
async def convert(file: UploadFile = File(...), target_type: str = "mp3"):
    result = await convert_file(file, target_type)
    return {"status": "success", "file_path": result}


"""

print(f"\nStarting FastAPI server on port {PORT}")
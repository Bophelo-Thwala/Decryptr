import os
from fastapi import UploadFile
from cryptography.fernet import Fernet

KEY = os.getenv("DECRYPTION_KEY")

async def decrypt_file():
    pass

"""
async def decrypt_file(file: UploadFile) -> str:
    contents = await file.read()
    f = Fernet(KEY)
    decrypted = f.decrypt(contents)
    
    output_path = f"uploads/dec_{file.filename}"
    with open(output_path, "wb") as f_out:
        f_out.write(decrypted)
    return output_path

"""
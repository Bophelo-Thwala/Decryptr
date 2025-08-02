import os
from fastapi import UploadFile
from pydub import AudioSegment

async def convert_file(file: UploadFile, target_type: str = "mp3") -> str:
    pass

"""

input_path = f"uploads/input_{file.filename}"
    output_path = f"uploads/converted.{target_type}"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=target_type)
    return output_path

"""
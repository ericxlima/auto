import os
import qrcode
from config import MEDIA_FOLDER
from uuid import uuid4


def generate_qr_code(url: str) -> str:
    img = qrcode.make(data)
    filename = f'{uuid4()}.png'
    img.save(os.path.join(MEDIA_FOLDER, filename))
    return filename
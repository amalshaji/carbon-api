import os
import uuid
import urllib.parse

from fastapi import APIRouter, HTTPException, status, File, UploadFile, Body, Depends
from fastapi.datastructures import UploadFile
from fastapi.responses import FileResponse

from app.schema import DefaultOptions
from app.utils import create_url_query
from app.carbon import get_image

api = APIRouter(prefix="/api")


@api.post("/")
async def grab_screenshot(
    file: UploadFile = File(None),
    params: DefaultOptions = Depends(DefaultOptions.as_form),
):
    if file is None and (params.code is None or params.code == ""):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="either code or code file is required",
        )

    if file:
        code = await file.read()
        code = code.decode("utf-8")
        code = urllib.parse.quote_plus(code)
        params.code = code
    url = create_url_query(params)
    filename = uuid.uuid4().hex
    path = os.getcwd() + f"/{filename}.png"
    path = await get_image(url, path)
    return FileResponse(path)
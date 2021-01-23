import inspect
from typing import Type
from fastapi import Form
from pydantic import BaseModel

# from app.schema import DefaultOptions


BASE_URL = "https://carbon.now.sh/"

optionToQueryParam = {
    "backgroundColor": "bg",
    "code": "code",
    "dropShadow": "ds",
    "dropShadowBlurRadius": "dsblur",
    "dropShadowOffsetY": "dsyoff",
    "exportSize": "es",
    "fontFamily": "fm",
    "firstLineNumber": "fl",
    "fontSize": "fs",
    "language": "l",
    "lineNumbers": "ln",
    "paddingHorizontal": "ph",
    "paddingVertical": "pv",
    "squaredImage": "si",
    "theme": "t",
    "watermark": "wm",
    "widthAdjustment": "wa",
    "windowControls": "wc",
    "windowTheme": "wt",
}


def as_form(cls: Type[BaseModel]):
    """
    Adds an as_form class method to decorated models. The as_form class method
    can be used with FastAPI endpoints
    """
    new_params = [
        inspect.Parameter(
            field.alias,
            inspect.Parameter.POSITIONAL_ONLY,
            default=(Form(field.default) if not field.required else Form(...)),
        )
        for field in cls.__fields__.values()
    ]

    async def _as_form(**data):
        return cls(**data)

    sig = inspect.signature(_as_form)
    sig = sig.replace(parameters=new_params)
    _as_form.__signature__ = sig
    setattr(cls, "as_form", _as_form)
    return cls


def create_url_query(params) -> str:
    first = True
    url: str = ""

    val: str = None

    for option in params.dict():
        if params.dict()[option] is True:
            val = "true"
        elif params.dict()[option] is False:
            val = "false"
        else:
            val = params.dict()[option]

        if first:
            first = False
            url = BASE_URL + f"?{optionToQueryParam[option]}={val}"
        else:
            url = url + f"&{optionToQueryParam[option]}={val}"
    return url
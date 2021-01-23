from pydantic import BaseModel, validator, Field

from app import utils


@utils.as_form
class DefaultOptions(BaseModel):
    backgroundColor: str = "rgba(171, 184, 195, 1)"
    code: str = None
    dropShadow: bool = True
    dropShadowBlurRadius: str = "68px"
    dropShadowOffsetY: str = "20px"
    exportSize: str = "2x"
    fontFamily: str = "Hack"
    firstLineNumber: int = 1
    fontSize: str = "14px"
    language: str = "auto"
    lineNumbers: bool = False
    paddingHorizontal: str = "56px"
    paddingVertical: str = "56px"
    squaredImage: bool = False
    theme: str = "seti"
    watermark: bool = False
    widthAdjustment: bool = True
    windowControls: bool = True
    windowTheme: str = None

    @validator("backgroundColor")
    def hex2rgb(cls, h: str) -> str:
        if h.startswith("#") or len(h) == 6:
            h = h.lstrip("#")
            return "rgb" + str(tuple(int(h[i : i + 2], 16) for i in (0, 2, 4)))
        return h
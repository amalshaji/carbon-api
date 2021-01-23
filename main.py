from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api import api

app = FastAPI()
app.include_router(api)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HTML = """
<center>
    <p><a href="https://github.com/amalshaji/carbon-api" target="_blank">GitHub</a></p>
    <p><a href="/docs" target="_blank">Try here</a></p>
</center>
"""


@app.get("/", include_in_schema=False)
async def homepage():
    return HTMLResponse(content=HTML, status_code=200)
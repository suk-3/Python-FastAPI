import uvicorn
from fastapi import FastAPI, Request, Form, File, UploadFile, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse, HTMLResponse, StreamingResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Literal, Optional
from udfunctions import *
import io

from services.health.router import router as healthRouter

app = FastAPI()
router = APIRouter()

origins = ["*"]

templates = Jinja2Templates(directory="ui")

app.add_middleware(GZipMiddleware, minimum_size=512)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# UI components
app.mount("/css",StaticFiles(directory="./ui/css"),name="css")
app.mount("/images",StaticFiles(directory="./ui/images"),name="images")
app.mount("/js",StaticFiles(directory="./ui/js"),name="js")
app.mount("/font",StaticFiles(directory="./ui/font"),name="font")

# Blueprint routes
app.include_router(healthRouter, prefix="/health", tags=["Health"])

log = putlog("MainExecutor")

configFile = "config/app.setting.json"
configuration = readJson(configFile)

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def basePage(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", 
                host=configuration["App"]["Host"],
                port=configuration["App"]["Port"],
                reload=configuration.get("App",{}).get("IsDev",False))
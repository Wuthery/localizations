from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

services = [
    "website",
    "api",
    "sniffer"
]
for service in services:
    app.mount(f"/Wuthery/localizations/main/{service}", StaticFiles(directory=service), name=service)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

services = [
    "website",
    "api",
    "sniffer"
]
for service in services:
    app.mount(f"/Wuthery/localizations/main/{service}", StaticFiles(directory=service), name=service)

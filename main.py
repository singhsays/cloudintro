import fastapi
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = fastapi.FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return FileResponse("static/index.html")

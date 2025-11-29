from datetime import datetime
import json
from typing import Callable
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static",
          StaticFiles(directory="resources/static"), name="static")
templates = Jinja2Templates(directory="resources/templates")


class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = datetime.now()
            # print(before)
            response: Response = await original_route_handler(request)
            duration = datetime.now() - before
            response.headers["X-Response-Time"] = str(duration)
            response.headers["test-value"] = "test-value"
            # print(f"route duration: {duration}")
            # print(f"route response: {response}")
            # print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler


router = APIRouter(route_class=TimedRoute)


@app.get("/")
def root():
    return {"message": "hello world!!"}


@app.get("/index", response_class=HTMLResponse)
async def index(req: Request):
    print(f"request: {req}")
    return templates.TemplateResponse(request=req, name='index.html')


@router.get("/time")
def time():
    return {"message": "time"}


@router.post("/time-format")
async def time_format(req: str):
    print(req)
    return {"message": "time"}


app.include_router(router)

import os
from functools import lru_cache
from typing import Collection

from fastapi import FastAPI
from lagom import Container, Singleton
from lagom.integrations.fast_api import FastApiIntegration
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .checkers import ALL_CHECKERS
from .hacky_hosting import get_homepage_html
from .models import SevenChecker, nope, IsSevenResult

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


app = FastAPI(title="Isseven", version="7")

container = Container()
deps = FastApiIntegration(container)

container[Jinja2Templates] = Singleton(
    lambda: Jinja2Templates(directory=__location__ + "/../templates")
)

container[Collection[SevenChecker]] = ALL_CHECKERS  # type: ignore

homepage_html = get_homepage_html(__location__ + "/../")


@app.get("/", include_in_schema=False)
def root(request: Request, templates=deps.depends(Jinja2Templates)):
    return templates.TemplateResponse(
        "page.html",
        {
            "content": homepage_html,
            "request": request,
        },
    )


@app.get(
    "/is/{possible_seven}",
    response_model=IsSevenResult,
    description="Checks if the input isseven",
    name="isseven",
)
@lru_cache(maxsize=128)
def check(possible_seven: str, checkers=deps.depends(Collection[SevenChecker])):  # type: ignore
    for checker in checkers:
        result = checker(possible_seven)
        if result.isseven:
            return JSONResponse(content=result.dict(), headers={})
    return JSONResponse(content=nope("We tried. This doesn't seem to be seven").dict())


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory=__location__ + "/../static_assets"), name="static")

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

DEFAULT_CACHE_SECONDS = 3600  # 1 hour


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
def check(possible_seven: str, checkers: Collection[SevenChecker] = deps.depends(Collection[SevenChecker])):  # type: ignore
    shortest_cache = DEFAULT_CACHE_SECONDS
    for checker in checkers:
        result = checker(possible_seven)
        if result.isseven:
            lifespan = result.valid_for_seconds or DEFAULT_CACHE_SECONDS
            return _make_json_response(result, lifespan)
        elif result.valid_for_seconds:
            shortest_cache = min(shortest_cache, result.valid_for_seconds)
    return _make_json_response(
        nope("We tried. This doesn't seem to be seven"), shortest_cache
    )


def _make_json_response(result: IsSevenResult, cache_for_seconds: int):
    return JSONResponse(
        content=result.dict(),
        headers={"Cache-Control": f"max-age={cache_for_seconds}"},
    )


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory=__location__ + "/../static_assets"), name="static")

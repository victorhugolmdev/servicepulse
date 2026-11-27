from pathlib import Path
from typing import Literal
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from app.checker import check_service, list_checks
from app.models import ServiceCheckRequest, ServiceCheckResult

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="ServicePulse API",
    description="Service health & latency monitoring API",
    version="0.3.0",
)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def dashboard() -> str:
    html_path = BASE_DIR / "templates" / "index.html"
    return html_path.read_text(encoding="utf-8")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/checks", response_model=ServiceCheckResult, status_code=201)
async def run_service_check(payload: ServiceCheckRequest) -> ServiceCheckResult:
    return await check_service(payload)


@app.get("/checks", response_model=list[ServiceCheckResult])
def get_checks(
    status: Literal["up", "down"] | None = Query(
        default=None,
        description="Optional filter by service status: 'up' or 'down'",
    )
) -> list[ServiceCheckResult]:
    return list_checks(status=status)
from fastapi import FastAPI
from app.checker import check_service
from app.models import ServiceCheckRequest, ServiceCheckResult

app = FastAPI(
    title="ServicePulse API",
    description="Service health & latency monitoring API",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/checks", response_model=ServiceCheckResult)
async def run_service_check(payload: ServiceCheckRequest) -> ServiceCheckResult:
    return await check_service(payload)
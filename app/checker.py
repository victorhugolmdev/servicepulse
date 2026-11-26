from datetime import datetime, timezone
from typing import Literal
import time
import httpx
from app.models import ServiceCheckRequest, ServiceCheckResult

_check_history: list[ServiceCheckResult] = []


async def check_service(payload: ServiceCheckRequest) -> ServiceCheckResult:
    start = time.perf_counter()
    checked_at = datetime.now(timezone.utc)

    try:
        async with httpx.AsyncClient(timeout=payload.timeout_seconds) as client:
            response = await client.get(str(payload.url))

        elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
        is_up = 200 <= response.status_code < 500

        result = ServiceCheckResult(
            name=payload.name,
            url=str(payload.url),
            status="up" if is_up else "down",
            status_code=response.status_code,
            response_time_ms=elapsed_ms,
            checked_at=checked_at,
        )
    except httpx.RequestError as exc:
        elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
        result = ServiceCheckResult(
            name=payload.name,
            url=str(payload.url),
            status="down",
            response_time_ms=elapsed_ms,
            error=str(exc),
            checked_at=checked_at,
        )

    _check_history.append(result)
    return result


def list_checks(status: Literal["up", "down"] | None = None) -> list[ServiceCheckResult]:
    if status is None:
        return list(_check_history)
    return [item for item in _check_history if item.status == status]
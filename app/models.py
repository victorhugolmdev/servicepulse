from datetime import datetime
from typing import Literal
from pydantic import BaseModel, HttpUrl


class ServiceCheckRequest(BaseModel):
    name: str
    url: HttpUrl
    timeout_seconds: float = 5.0


class ServiceCheckResult(BaseModel):
    name: str
    url: str
    status: Literal["up", "down"]
    status_code: int | None = None
    response_time_ms: float | None = None
    error: str | None = None
    checked_at: datetime
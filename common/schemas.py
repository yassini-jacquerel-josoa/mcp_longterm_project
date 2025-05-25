# common/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class TodoItem(BaseModel):
    item: str

class Alert(BaseModel):
    event: str
    area: str
    severity: str
    description: str
    instructions: Optional[str] = None

class ForecastPeriod(BaseModel):
    name: str
    temperature: int
    temperatureUnit: str
    windSpeed: str
    windDirection: str
    detailedForecast: str

class GetAlertsArgs(BaseModel):
    state: str

class GetForecastArgs(BaseModel):
    latitude: float
    longitude: float

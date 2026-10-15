
from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel, Field


class QuerySensorsIntent(BaseModel):
    """Estructura para extraer parámetros de consulta sobre series temporales de sensores."""

    metric: Literal["temperature", "humidity", "pressure"] = Field(
        default="temperature",
        description="Métrica a consultar (temperature, humidity, pressure).",
    )
    aggregation: Literal["MAX", "MIN", "AVG", "NONE"] = Field(
        default="NONE",
        description="Operación matemática solicitada: MAX, MIN, AVG o NONE si se pide la serie completa.",
    )
    start_time: datetime = Field(
        description="Marca de tiempo de inicio en formato ISO 8601 (YYYY-MM-DDTHH:MM:SS)."
    )
    end_time: datetime = Field(
        description="Marca de tiempo de fin en formato ISO 8601 (YYYY-MM-DDTHH:MM:SS)."
    )
    device_id: Optional[str] = Field(
        default=None,
        description="Identificador del sensor o dispositivo si se especifica.",
    )

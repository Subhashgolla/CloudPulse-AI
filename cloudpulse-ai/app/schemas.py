from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4
from pydantic import BaseModel, Field

class TransactionEvent(BaseModel):
    transaction_id: str = Field(default_factory=lambda: str(uuid4()))
    customer_id: str
    amount: float = Field(gt=0)
    merchant_category: str
    country: str
    device_type: Literal["mobile","web","pos"]
    card_present: bool
    event_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    transaction_velocity_1h: int = Field(ge=0)
    customer_avg_amount: float = Field(gt=0)

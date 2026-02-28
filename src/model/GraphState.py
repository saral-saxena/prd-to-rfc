from typing import Any, Dict

from pydantic import BaseModel, Field


class GraphState(BaseModel):

    bpd_raw: Dict[str, Any] = Field(default_factory=dict)
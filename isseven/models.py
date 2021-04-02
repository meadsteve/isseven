from pydantic import BaseModel


class IsSevenResult(BaseModel):
    isseven: bool
    explanation: str
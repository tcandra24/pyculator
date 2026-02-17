from dataclasses import dataclass

@dataclass(frozen=True)
class HistoryItem:
  param1: int
  param2: int
  operator: str
  result: float
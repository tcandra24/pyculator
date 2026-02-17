from dataclasses import dataclass

@dataclass
class Config:
  max_history: int
  auto_save: bool
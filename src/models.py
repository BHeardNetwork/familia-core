from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Any, Optional, Literal
from datetime import datetime, timezone
from enum import Enum
import uuid

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class TriadRole(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    ANTISTUDENT = "antistudent"

# ... (full models.py content with all Pydantic classes: DigitalSelf, MemoryEvent, Goal, Task, InternalDialogue, PlanPath, InferenceResult) ...
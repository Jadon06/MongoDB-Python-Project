from pydantic import BaseModel, EmailStr, BeforeValidator, Field, ConfigDict
from typing import Optional, Annotated
from bson.objectid import ObjectId
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

PyObjectId = Annotated[str, BeforeValidator(str)]

class student(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[int] = None

class student_response(student):
    pass
    id: PyObjectId
    created_at: datetime = datetime.now(timezone.utc)

class course_schema(BaseModel):
    course_code: str
    course_name: str
    time_added: datetime = datetime.now(timezone.utc)
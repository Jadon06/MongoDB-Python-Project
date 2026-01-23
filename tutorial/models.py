from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr, BeforeValidator, Field, ConfigDict
from typing import Optional, Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]

class students(Document):
    id: PydanticObjectId | None
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[int] = None
    GPA: Optional[float] = 0.0
    model_config = ConfigDict(
        populate_by_name=True
    )
    
    class Settings:
        collection_name="students"

class courses(Document):
    id: PydanticObjectId | None
    course_name: str
    course_code: str
    model_config = ConfigDict(
        populate_by_name=True
    )

    class Settings:
        collection_nam="courses"
    
from pydantic import BaseModel, ConfigDict, Field

class StudyBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    progress: int = Field(default=0, ge=0, le=100)
    description: str | None = None

class StudyCreate(StudyBase):
    pass

class StudyRead(StudyBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel, ConfigDict

class StudyBase(BaseModel):
    title: str
    progress: int = 0

class StudyCreate(StudyBase):
    pass

class Study(StudyBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

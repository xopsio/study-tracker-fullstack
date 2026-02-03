from pydantic import BaseModel

class StudyBase(BaseModel):
    title: str
    progress: int = 0

class StudyCreate(StudyBase):
    pass

class Study(StudyBase):
    id: int

    class Config:
        orm_mode = True

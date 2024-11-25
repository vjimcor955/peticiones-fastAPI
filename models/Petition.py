from pydantic import BaseModel

class Petition(BaseModel):
    body: str

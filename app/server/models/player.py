# here i define the player schema -> how the information will stored in the database
# choosing my prefered database as mongodb

from typing import Optional
from pydantic import BaseModel, Field


class PlayerSchema(BaseModel):
    first_name: str = Field(None)
    last_name: str = Field(None)
    weight: str = Field(None)
    age: int = Field(None)
    position: str = Field(None)
    height: str = Field(None)
    country: str = Field(None)
    club: str = Field(None)


    class Config:
        schema_extra = {
            "example": {
                "first_name": "Cristiano Ronaldo",
                "last_name": "Dos Santos",
                "weight": "148kg",
                "age": 37,
                "position": "LW",
                "height": "1.92m",
                "country": "Portugal",
                "club": "Manchester United",
    
            },
        }

class UpdatePlayerModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    weight: Optional[str]
    age: Optional[int]
    position: Optional[str]
    height: Optional[str]
    country: Optional[str]
    club: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Cristiano Ronaldo",
                "last_name": "Dos Santos",
                "weight": "148kg",
                "age": 37,
                "position": "LW",
                "height": "1.92m",
                "country": "Portugal",
                "club": "Manchester United",
            
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
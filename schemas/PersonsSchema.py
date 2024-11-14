# https://docs.pydantic.dev/latest/concepts/types/
# https://docs.pydantic.dev/latest/concepts/fields/

from pydantic import BaseModel, Field
from typing import Optional, List,Text
from datetime import datetime

class PersonsSchema(BaseModel):

    firstName1: str = Field() # type: string
    firstName2: str = Field() # type: string
    lastName1: str = Field() # type: string
    lastName2: str = Field() # type: string
    genre: str = Field() # type: string
    dateBirth: int = Field() # type: timestamp
    isAlive: bool = Field() # type: boolean
    email: str = Field() # type: mail

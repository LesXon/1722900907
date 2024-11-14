# https://docs.pydantic.dev/latest/concepts/types/
# https://docs.pydantic.dev/latest/concepts/fields/

from pydantic import BaseModel, Field
from typing import Optional, List,Text
from datetime import datetime

class UsersSchema(BaseModel):

    name: str = Field() # type: string
    password: str = Field() # type: string
    mail: str = Field() # type: mail

# https://docs.pydantic.dev/latest/concepts/types/
# https://docs.pydantic.dev/latest/concepts/fields/

from pydantic import BaseModel, Field
from typing import Optional, List,Text
from datetime import datetime

class IdsSchema(BaseModel):

    number: str = Field() # type: string
    issueDate: int = Field() # type: timestamp
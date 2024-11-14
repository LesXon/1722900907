# https://docs.pydantic.dev/latest/concepts/types/
# https://docs.pydantic.dev/latest/concepts/fields/

from pydantic import BaseModel, Field
from typing import Optional, List,Text
from datetime import datetime

class LicensesSchema(BaseModel):

    data: str = Field() # type: string

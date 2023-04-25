from pydantic import BaseModel
from typing import  Optional, List

class Adress(BaseModel):
    id: str
    dictrict: str
    code: str

class User(BaseModel):
    id: int
    name: str
    mail: Optional[str] = "1841284"
    phone: Optional[str] = "091283"
   # adress: List(Adress)


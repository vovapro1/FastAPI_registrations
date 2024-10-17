from datetime import datetime
import enum
from pydantic import BaseModel

class Type_type(enum.Enum):
    shtraf ="Оплата штрафа"
    pokupka = "Покупка акций"



class AddOperation(BaseModel):
    id: int
    quanti: str
    figi: str
    instrumental_type: str
    date: datetime
    type: Type_type




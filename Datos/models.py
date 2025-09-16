from dataclasses import dataclass, field #field Evita generar constructores 
from typing import Optional, List

@dataclass
class Tennis:
    marca: str
    modelo:str
    precio: float
    cantidad: str
    id: Optional[int]

from pydantic import BaseModel, Field
import uuid

class Libro(BaseModel):
    id_libro: str = Field(default=any)
    titulo: str = Field(min_length=5, max_length=20)
    autor: list[str] = Field(examples=['17738d3c-9f1e-11ec-8d3d-0242ac130022'])
    categoria: str = Field(min_length=5, max_length=20)
    year: int = Field(le=2024)

    # Ejemplo del request para que se vea en la documentacion
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "",
                    "titulo": "En agosto nos vemos",
                    "autor": ['17738d3c-9f1e-11ec-8d3d-0242ac130004'],
                    "year": 2024,
                    "categoria": "Realismo magico"
                }
            ]
        }
    }
    
class LibroActualizado(BaseModel):
    id_libro: list[str] = Field(examples=['17738d3c-9f1e-11ec-8d3d-0242ac130010'])
    titulo: str = Field(min_length=5, max_length=20)
    autor: list[str] = Field(examples=['17738d3c-9f1e-11ec-8d3d-0242ac130022'])
    categoria: str = Field(min_length=5, max_length=20)
    year: int = Field(le=2024)

    # Ejemplo del request para que se vea en la documentacion
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "17738d3c-9f1e-11ec-8d3d-0242ac130003",
                    "titulo": "En agosto nos vemos",
                    "autor": ['17738d3c-9f1e-11ec-8d3d-0242ac130004'],
                    "year": 2024,
                    "categoria": "Realismo magico"
                }
            ]
        }
    }
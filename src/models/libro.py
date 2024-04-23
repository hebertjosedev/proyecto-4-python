from pydantic import BaseModel, Field
import uuid

class Libro(BaseModel):
    id: uuid.UUID
    titulo: str = Field(min_length=5, max_length=20)
    autor: list[str] = Field(examples=[])
    categoria: str = Field(min_length=5, max_length=20)
    year: int = Field(le=2024)

    # Ejemplo del request para que se vea en la documentacion
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "titulo": "Un titulo del libro",
                    "autor": ['17738d3c-9f1e-11ec-8d3d-0242ac130033'],
                    "year": 2023,
                    "categoria": "accion, romance"
                }
            ]
        }
    }
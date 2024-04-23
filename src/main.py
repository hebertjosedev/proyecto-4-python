# main.py
from fastapi import FastAPI, status, Body 
from fastapi.responses import JSONResponse
import uuid
from json import load, dump
from src.models.libro import Libro
from operator import itemgetter

app = FastAPI()

app.title = "Proyecto 4"

#ENDPOINTS DE LIBROS

@app.get('/libros', tags=['libros'])
def obtener_libros():
    with open('db.json', 'r', encoding='utf-8') as db:
      datos = load(db)
      libros = datos['books']
      
    return libros

@app.get('/libros/{id}', tags=['libros'])
def obtener_libro(id: str):
    with open('db.json', 'r', encoding='utf-8') as db:
        datos = load(db)
        libros = datos['books']

        libro = list(filter(lambda libro: libro['id'] == id ,libros))

        if libro != []:
            return libro
    return 'no existe tu libro'

@app.get('/libros/', tags=['libros'])
def obtener_libros_por_titulo(titulo: str):
    titulo = titulo.capitalize()
    with open('db.json', 'r', encoding='utf-8') as db:
        datos = load(db)
        libros = datos['books']
        
        libro = [libro for libro in libros if libro['title'][0:2] == titulo[0:2]]
        if libro != []:
         return libro
        
    return 'No existe un libro con ese titulo'


# @app.post('/libros', tags=['libros'])
# def crear_libro(
#     id: uuid.UUID = Body(serialization_alias=''),
#     titulo: str = Body(),
#     autor: list = Body(),
#     year: int = Body()
#     ):
    
#     with open('db.json', 'r', encoding='utf-8') as db:
#         datos = load(db)
        
#     datos['books'].append({
#         'id': uuid.UUID,
#         'titulo': titulo,
#         'autor': autor,
#         'year': year
#     })
    
#     with open('db.json', 'w', encoding='utf-8') as db_nueva:
#         dump(datos, db_nueva, indent=2)
        
#     return JSONResponse(content={'message': 'Pelicula creada con exito'}, status_code=status.HTTP_201_CREATED)

@app.post('/libros', tags=['libros'])
def crear_libro(libro: Libro):
    id, titulo, autor, categoria, year = itemgetter('id', 'titulo', 'autor', 'categoria', 'year')(libro.model_dump())
    

    libro_nuevo = ({
            'id': id,
            'titulo': titulo,
            'autor': autor,
            'categoria': categoria,
            'year': year
        })
    
    with open('db.json', 'r', encoding='utf-8') as db:
        datos = load(db)
        
    datos['books'].append(libro_nuevo)
    
    with open('db.json', 'w', encoding='utf-8') as db_nueva:
        dump(datos, db_nueva, indent=2)
        
    return JSONResponse(content={'message': 'Pelicula creada con exito'}, status_code=status.HTTP_201_CREATED)


@app.delete('/libros/{id}', tags=['libros'])
def eliminar_libro_por_id(id = str):
    with open('db.json', 'r', encoding='utf-8') as db:
        datos = load(db)
        libros = datos['books']
        
        for libro in libros:   
         if libro['id'] == id:
          libros.remove(libro)
          return libros
        
    return 'No existe un libro con ese ID'        


#ENDOINTS DE AUTORES

@app.get('/autores', tags=['autores'])
def obtener_autores():
    with open('db.json', 'r', encoding='utf-8') as db:
      datos = load(db)
      autores = datos['authors']
      
    return autores

@app.get('/autores/{id}', tags=['autores'])
def obtener_autor(id: str):
    with open('db.json', encoding='utf-8') as db:
        datos = load(db)
        autores = datos['authors']

        autor = list(filter(lambda autor: autor['id'] == id ,autores))

        if autor != []:
            return autor
    return 'no existe tu autor'
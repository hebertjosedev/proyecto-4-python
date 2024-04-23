# main.py
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid
from json import load, dump
from src.models.libro import Libro, LibroActualizado

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

@app.post('/libros', tags=['libros'])
def crear_libro(libro: Libro):
    id_libro = libro.id_libro
    id_libro = str(uuid.uuid1())
    titulo = libro.titulo
    
    libro_nuevo = ({
            'id_libro': id_libro,
            'titulo': titulo,
            'autor': libro.autor,
            'categoria': libro.categoria,
            'year': libro.year
        })
    
    with open('db.json', 'r', encoding='utf-8') as db:
        datos = load(db)    
        
    autores_nuevo = []
    longitud_autores = len(autores_nuevo)
    comparacion = []
    longitud_comparacion = len(comparacion)
    
    for autores in libro.autor:
        autores_nuevo.append({'id':autores})
    
    for autor_id in datos['authors']:
        for autor_ingresado in autores_nuevo:
            if autor_id['id'] == autor_ingresado['id']:
                comparacion.append(autor_id)
                if longitud_autores == longitud_comparacion:   
                 datos['books'].append(libro_nuevo)
                 with open('db.json', 'w', encoding='utf-8') as db_nueva:
                  dump(datos, db_nueva, indent=2)
                  return JSONResponse(content={'message': 'Pelicula creada con exito'}, status_code=status.HTTP_201_CREATED)
     
    return JSONResponse(content={'message': 'Tu id de autor no pertenece a ninguno'}, status_code=status.HTTP_400_BAD_REQUEST)

@app.put('/libros', tags=['libros'])
def actualizar_libro_por_id(libro_actualizar: LibroActualizado):
    #id_libro = str(libro_actualizar.id_libro)
    libro_actualizado = ({
            'id_libro': libro_actualizar.id_libro,
            'titulo': libro_actualizar.titulo,
            'autor': libro_actualizar.autor,
            'categoria': libro_actualizar.categoria,
            'year': libro_actualizar.year
        })
    
    with open('db.json', 'r', encoding='utf-8') as db:
        datos = load(db)
    longitud = len('17738d3c-9f1e-11ec-8d3d-0242ac130004')
    print(longitud)    
    print(libro_actualizado)
    print(libro_actualizado['id_libro'])
    filtrado = list(filter(lambda libro: libro['id'] == libro_actualizar.id_libro ,datos['books'])) 
    print(filtrado)  
        
    autores_nuevo = []
    longitud_autores = len(autores_nuevo)
    comparacion = []
    longitud_comparacion = len(comparacion)
    
    # for autores in libro.autor:
    #     autores_nuevo.append({'id':autores})
    
    # for autor_id in datos['authors']:
    #     for autor_ingresado in autores_nuevo:
    #         if autor_id['id'] == autor_ingresado['id']:
    #             comparacion.append(autor_id)
    #             if longitud_autores == longitud_comparacion:   
    #              datos['books'].append(libro_actualizado)
    #              with open('db.json', 'w', encoding='utf-8') as db_nueva:
    #               dump(datos, db_nueva, indent=2)
    #               return JSONResponse(content={'message': 'Pelicula creada con exito'}, status_code=status.HTTP_201_CREATED)
     
    # return JSONResponse(content={'message': 'Tu id de autor no pertenece a ninguno'}, status_code=status.HTTP_400_BAD_REQUEST)


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
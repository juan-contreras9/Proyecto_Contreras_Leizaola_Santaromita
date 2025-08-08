
from Departmento import Departamento
from Artista import Artista
from Obra import Obra

import requests
import csv

class App:
    
    #Clase principal de la aplicación del museo para el menú y las búsquedas de obras y artistas.
    
    def __init__ (self):
        
        #Inicializa las listas de departamentos y obras.
        
        self.departamentos=[]
        self.obras=[]
    
    def start(self):
        
        #Muestra el menú principal y gestiona la interacción con el usuario.
        
        while True:

            menu = input(""" Bienvenidos al museo, seleccione una opción:
1. Buscar obras por nombre de artista
2. Buscar obras por nacionalidad del autor
3. Buscar obras por departamento
4. Salir
Seleccione una opción: """)

            if menu == '1':
                self.obras_por_nombre_autor()

            elif menu == '2':
                self.obras_por_nacionalidad()


            elif menu == '3':
                self.carga_datos_departamentos()
                
            
            elif menu == '4':
                print("Salir")
                break
            else:
                print("Opción no válida, intente de nuevo.")

    def datos_departamentos(self):
        
        #Obtiene la lista de departamentos desde la API del museo.
        
        try:
            departamentos_api = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/departments').json()['departments']
            print('Los datos de los departamentos fueron obtenidos')
            return departamentos_api
        except:
            print('No se logro obtener datos de la API')
            
    def carga_datos_departamentos(self):

        #Muestra los departamentos disponibles, permite seleccionar uno y ver obras de ese departamento.

        departamentos_api = self.datos_departamentos()
        if not departamentos_api:
            return
        self.departamentos.clear()
        for i in departamentos_api:
            nuevo_departamento = Departamento(i['departmentId'], i['displayName'])
            self.departamentos.append(nuevo_departamento)

        print("Departamentos disponibles:")
        for dep in self.departamentos:
            print(f"ID: {dep.id} - Nombre: {dep.nombre}")

        try:
            seleccion_departamento = int(input("Seleccione un departamento por ID: "))
        except ValueError:
            print("ID inválido.")
            return

        dep_seleccionado = None
        for dep in self.departamentos:
            if dep.id == seleccion_departamento:
                dep_seleccionado = dep
                break

        if dep_seleccionado is None:
            print("Departamento no encontrado.")
            return

        print(f"Departamento seleccionado: {dep_seleccionado.nombre}")
        url_obras = f'https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentId={dep_seleccionado.id}'
        response = requests.get(url_obras).json()
        self.obras.clear()
        
        if response.get('objectIDs'):
            print(f"Mostrando hasta 10 obras del departamento '{dep_seleccionado.nombre}':")
            self.obras.clear()
            for idx, object_id in enumerate(response['objectIDs'][:10], 1):
                obra_data = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}').json()
                artista_object = Artista(
                    obra_data.get("artistDisplayName", "Desconocido"),
                    obra_data.get("artistNationality", "Desconocido"),
                    obra_data.get("artistBeginDate", ""),
                    obra_data.get("artistEndDate", "")
                )
                obra_object = Obra(
                    obra_data.get("objectID", 0),
                    obra_data.get("title", "Sin título"),
                    artista_object,
                    obra_data.get("department", ""),
                    obra_data.get("classification", ""),
                    obra_data.get("accessionYear", ""),
                    obra_data.get("primaryImage", "")
                )
                self.obras.append(obra_object)
                print(f"{idx}. Obra: {obra_object.titulo} | Artista: {obra_object.artista.nombre} | Año: {obra_object.anio}")

            try:
                seleccion_obra = int(input("\nSeleccione el número de la obra para ver detalles: "))
                if 1 <= seleccion_obra <= len(self.obras):
                    obra_seleccionada = self.obras[seleccion_obra - 1]
                    print("\n--- Detalles de la obra seleccionada ---")
                    print(f"Título: {obra_seleccionada.titulo}")
                    print(f"Nombre del artista: {obra_seleccionada.artista.nombre}")
                    print(f"Nacionalidad del artista: {obra_seleccionada.artista.nacionalidad}")
                    print(f"Fecha de nacimiento: {obra_seleccionada.artista.fecha_de_nacimiento}")
                    print(f"Fecha de muerte: {obra_seleccionada.artista.fecha_de_muerte}")
                    print(f"Tipo: {obra_seleccionada.tipo}")
                    print(f"Año de creación: {obra_seleccionada.anio}")
                    print(f"URL de la imagen: {obra_seleccionada.imagen_url}")
                else:
                    print("Selección fuera de rango.")
            except ValueError:
                print("Selección inválida.")
        else:
            print("No se encontraron obras para este departamento.")

def obras_por_nombre_autor(self):
        
        #Permite buscar obras por el nombre del autor, mostrar una lista y ver detalles de una obra seleccionada.
        
        nombre_autor = input("Ingrese el nombre del autor a buscar correctamente: ")
        if not nombre_autor:
            print("Debe ingresar un nombre de autor.")
            return
        print(f"\nBuscando obras del autor: {nombre_autor}\n(Espere, esto puede tardar unos segundos...)")
        url = f'https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_autor}'
        response = requests.get(url).json()
        obras = []
        if response.get('objectIDs'):
            print(f"Se encontraron {len(response['objectIDs'])} obras. Mostrando hasta 10:")
            for idx, object_id in enumerate(response['objectIDs'][:10], 1):
                obra_data = requests.get(f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}').json()
                obras.append(obra_data)
                print(f"{idx}. {obra_data.get('title', 'Sin título')} | Artista: {obra_data.get('artistDisplayName', 'Desconocido')} | Año: {obra_data.get('accessionYear', '')}")

            try:
                seleccion_obra = int(input("\nSeleccione el número de la obra para ver detalles: "))
                if 1 <= seleccion_obra <= len(obras):
                    obra = obras[seleccion_obra - 1]
                    print("\n--- Detalles de la obra seleccionada ---")
                    print(f"Título: {obra.get('title', 'Sin título')}")
                    print(f"Nombre del artista: {obra.get('artistDisplayName', 'Desconocido')}")
                    print(f"Nacionalidad del artista: {obra.get('artistNationality', 'Desconocido')}")
                    print(f"Fecha de nacimiento: {obra.get('artistBeginDate', '')}")
                    print(f"Fecha de muerte: {obra.get('artistEndDate', '')}")
                    print(f"Tipo: {obra.get('classification', '')}")
                    print(f"Año de creación: {obra.get('accessionYear', '')}")
                    print(f"URL de la imagen: {obra.get('primaryImage', '')}")
                else:
                    print("Selección fuera de rango.")
            except ValueError:
                print("Selección inválida.")
        else:
            print("No se encontraron obras para este autor.")



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

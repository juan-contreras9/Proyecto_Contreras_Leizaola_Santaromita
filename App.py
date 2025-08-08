
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

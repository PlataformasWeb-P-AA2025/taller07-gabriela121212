import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Club

# Cargar y guardar datos de clubs
clubs = {}
# Leemos el archivo datos_club.txt
with open('data/datos_clubs.txt', 'r', encoding='utf-8') as f:
    lineas_clubs = f.readlines()#leemos todo el archivo

# Leemos el archivo datos_jugador.txtcd
with open('data/datos_jugadores.txt', 'r', encoding='utf-8') as f:
    lineas_jugadores = f.readlines()

#leemos linea por linea
for lineas_ in lineas_clubs:
        #obtenenos las columnas separadas por ;
        colums = lineas_.split(";")
        
        #asignamos cada valor de la columna a las variables
        n,d,f=colums
        #crwamos cadaobjeto de la tabla club convirtiendo fundacion a entero por recomendacion
        club = Club(nombre=n,deporte=d,fundacion=int(f))
        #añadimos a la sesion
        session.add(club)
        #asignamos un objeto al diccionario pasando su key el nombre del club
        #esto nos ayudara para localizar el club que le pertenece a cada jugado
        #dandome su valor que seria el objeto club
        clubs[n]=club

#realizamos lo mismo para jugadores añadiendo la busqueda del objeto en el diccionario     
for lineas_ in lineas_jugadores:
        colums = lineas_.split(";")
        c,p,d,nj=colums
        club=clubs.get(c)#le mandamos como key al diccionario el nombre del club del jugador y el diccionario me va devolver su valor
        jugador = Jugador(nombre=nj,posicion =p,dorsal=int(d),club=club)
        session.add(jugador)


# se confirma las transacciones
session.commit()
print("consulta ", session.query(Club).filter_by(nombre="Barcelona").one())


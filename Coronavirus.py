from pacients import pacient
from datetime import * 
from os import system, name
import re

def mostrarMenu(opcions):
    #Mostrara totes les opcions numerades
     for i,opcio in enumerate(opcions):
        print(f"{i+1:2}. {opcio}")

def sortir():
    print("Fins un altre")

def escullOpcio(n):
    patro = "^\d{1,}$"
    while True:
        o = input("Escull una opció: ")
        if re.search(patro,o):
            if n>=int(o) and int(o)!=0:
                return o
        
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def esperaTecla():
     input("Pulsa intro per continuar... ")

def nouPacient():    
    #Demanarà per teclat les dades del nou pacient:
    #codi, dataNaixement,sexe,estat i iniciContagi
    #i retornarà un pacient nou
    codi = input("Codi Pacient: ")
    p = pacient(codi)
    dataStr = input("Data Naixement: ")
    p.dataNaixement = datetime.strptime(dataStr,'%d/%m/%Y')
    iniciStr = input("Inici Contagi: ")
    p.iniciContagi = datetime.strptime(dataStr,'%d/%m/%Y')
    p.estat = input("Estat : ")
    return p

def afegeixPacient(l:list,p:pacient):
    l.append(p)

def canviEstatPacient(p:pacient,estat:str):
    p.estat=estat

def mostrarPacients(l:list):
    for p in l:
        print(f"{p.Codi}-{p.dataNaixement}-{p.estat}")

def cercarPacient(l:list,codi:str):
    for p in l:
        if p.Codi==codi:
            return p
    return None

def edat(p:pacient,data:date):
    data1=p.dataNaixement
    data2=date
    datafinal= data1-data2
    return datafinal

def pacientsEstat(l:list,estat:str):
    estatpacients=[]
    for p in l:
        if estat == p.estat:
            estatpacients.append(p)
    return estatpacients

opcions = ("Afegir pacients","Mostrar pacients","Canviar l'estat","Saber edat del pacient","Saber estat del pacient","Sortir")
pacients = []
fi = False


while not fi:
    clear() 
    mostrarMenu(opcions)
    #Escullir opcio
    opcio=escullOpcio(len(opcions))
    if opcio == "1":
        #Afegir pacient
        p=nouPacient()
        afegeixPacient(pacients,p)
        print(pacients)
        esperaTecla()
    
    elif opcio=="2":
        mostrarPacients(pacients)
        esperaTecla()

    elif opcio=="3":
        codi = input("Codi pacient que li vols canviar l'estat: ")
        p = cercarPacient(pacients,codi)
        if p:
            #mostrar pacient
            estat = input("Nou Estat: ")
            canviEstatPacient(p,estat)
    
    elif opcio=="4":
        codi=input("Digues el codi del pacient: ")
        p=cercarPacient(pacients,codi)
        idata=input("Digues una data: ")
        dataresta=datetime.strptime(idata,'%d/%m/%Y')
        print(int((dataresta-p.dataNaixement).days//365.25))
        esperaTecla()

    elif opcio == "5":
        estat = input("Estat dels pacients que vols saber: ")
        estatpacients = pacientsEstat(pacients,estat)
        mostrarPacients(estatpacients)
        esperaTecla()
        
    elif opcio == "6":
        sortir()
        fi = True
    

    
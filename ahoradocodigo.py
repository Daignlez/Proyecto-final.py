from tkinter import *
import random

letras_usadas=[] #creo una lista vacia
def funcion_probarletra():
    letras_usadas.append(letraObtenida.get())  #agrega las letras del boton al final de la lista
    print(letras_usadas)  #imprime las letras usadas 
    if letraObtenida.get() in palabra:  #si nuestra letra obtenida (.get=traer la letra de nuestra entry) entonces ramplaza un guion por una letra
        if palabra.count(letraObtenida.get())>1: #count cuenta las veces se repite una letra en una palabra y si esto es mayor que uno
           for i in range(len(palabra)):        #entonces hay que descubrir las otras letras
                if palabra[i]==letraObtenida.get():    #comprobacion, donde recorre toda la palabra y coloca la letra intoducida entonces cambiamos de guion a letra
                    guiones[i].config(text=""+letraObtenida.get())
        else:
            guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get()) #si hay una letra sin repeticion en mi indice(.indix busca y obtiene el indice de mi variable) solo la remplaza.

Ventana=Tk()#crea una ventana y su configuracion.

archivo=open("palabras.txt","r") #creo un archivo y abro palabras.py solo en forma de lectura.
conjuntodepalabras=list(archivo.read().split(","))
palabra=random.choice(conjuntodepalabras)

letraObtenida=StringVar() #declara varieable de tipo cadena
Ventana.title("Juego del ahorcado")
Ventana.config(width=1000,height=600,bg="purple",relief="groove",bd=10)
#aqui creo una frame (una hoja,sobreo otra)para crear un borde
juegoFrame=Frame(Ventana)
juegoFrame.config(width=1000,height=600,relief="sunken",bd=10)
juegoFrame.grid_propagate(False)#evita que se ajuste al tamaño del grid si es falso
juegoFrame.pack()#agregar el frame a la ventana. 
Label1=Label(juegoFrame,text="Introduce cualquier letra:",font=("verdana",24))
Label1.grid(column=0,row=0,padx=10,pady=10)
letras=Entry(juegoFrame,width=1,font=("verdana",24),textvariable=letraObtenida)
letras.grid(column=1,row=0,padx=10,pady=10)

boton_de_letras=Button(juegoFrame,text="Probar",bg="pink",command=funcion_probarletra)#en esta parte creo un boton que guarda lass letras.
LetrasLabel=[Label(juegoFrame,text=chr(a+97),font=("verdana",20)) for a in range(26)] # chr Saber si una letra está entre determinado rango


boton_de_letras.grid(column=0,row=1,pady=10)#aqui configuro la ubicacion de mi boton

guiones=[Label(juegoFrame,text="_",font=("verdana",30)) for palabra in palabra]
inicialx=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialx,y=400)
    inicialx+=50





Ventana.mainloop()

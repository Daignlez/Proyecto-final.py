from tkinter import *
from random import randint

letras_usadas=[] #creo una lista vacia
def funcion_probarletra():
    letras_usadas.append(letraObtenida.get())  #agrega las letras del boton al final de la lista
    print(letras_usadas)  #imprime las letras usadas
Ventana=Tk()#crea una ventana y su configuracion.
archivo=open("palabras.py","r") #creo un archivo y abro palabras.py solo en forma de lectura.
conjuntodepalabras= archivo.read().split("\n")
palabra=conjuntodepalabras[randint(0,len(conjuntodepalabras))-1]

letraObtenida=StringVar()
Ventana.title("Juego del ahorcado")
Ventana.config(width=1000,height=600,bg="purple",relief="groove",bd=10)
#aqui creo una frame (una hoja,sobreo otra)para crear un borde
juegoFrame=Frame(Ventana)
juegoFrame.config(width=1000,height=600,relief="sunken",bd=10)
juegoFrame.grid_propagate(False)#evita que se ajuste al tamaño del grid si es falso
juegoFrame.pack()#agregar el frame a la ventana. 
Label1=Label(juegoFrame,text="Introduce cualquier letra:",font=("verdana",24))
Label1.grid(column=0,row=0,padx=10,pady=10)
letras=Entry(juegoFrame,width=1,font=("verdana",24),textvariable=letraObtenida).grid(column=1,row=0,padx=10,pady=10)

boton_de_letras=Button(juegoFrame,text="Probar",bg="pink",command=funcion_probarletra)#en esta parte creo un boton que guarda lass letras

boton_de_letras.grid(column=0,row=1,pady=10)#aqui configuro la ubicacion de mi boton

guiones=[Label(juegoFrame,text="_",font=("verdana",30)) for _ in palabra]
inicialx=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialx,y=400)
    inicialx+=50





Ventana.mainloop()


from tkinter import *
import random
from tkinter.messagebox import *


letras_usadas=[] #creo una lista vacia

vidas=7
letrasacertadas=0

def colocarletras():
    x=50
    y=150
    contador= 0
    Label(diagrama,text="letras sin usar").place(x=50,y=100) 
    for i in range(26):
          contador+=1
          LetrasLabel[i].place(x=x,y=y)
          x+=30
          if contador==5:
              y+=35
              contador=0
              x=50
def funcion_probarletra():
    global vidas
    global letrasacertadas
    letras_usadas.append(letraObtenida.get())  #agrega las letras del boton al final de la lista
    print(letras_usadas)  #imprime las letras usadas
    LetrasLabel[ord(letraObtenida.get())-97].config(text="")
    if letraObtenida.get() in palabra:  #si nuestra letra obtenida (.get=traer la letra de nuestra entry) entonces ramplaza un guion por una letra
        if palabra.count(letraObtenida.get())>1:  #count cuenta las veces se repite una letra en una palabra y si esto es mayor que uno #entonces hay que descubrir las otras letras
          letrasacertadas+=palabra.count(letraObtenida.get())                                         
          for i in range(len(palabra)):       
                if palabra[i]==letraObtenida.get():    #comprobacion, donde recorre toda la palabra y coloca la letra intoducida entonces cambiamos de guion a letra 
                    guiones[i].config(text=""+letraObtenida.get())
        else:
            letrasacertadas+=1 
            guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get()) #si hay una letra sin repetir en mi indice(.indix busca y obtiene el indice de mi variable) solo la remplaza.
        if letrasacertadas == len(palabra): #si las leras acertadas son igual a la longitud de la palabra
            showwarning(title="Ganaste",message="Felicidades,Ganaste")   #entonces mostramos un cartel con un mensaje.      
    else:
        vidas-=1 #Entonces si la letra uno esta en la palabra le restamos una vida
        diagrama.itemconfig(imagen_id,image=imagenes[vidas-1])
        if vidas == 0:
            showwarning(title="Perdiste",message="Se acabaron tus vidas") # usando el método messagebox.showwarning() en Tkinter, cómo se muestra un cuadro de mensaje de advertencia

Ventana=Tk()#crea una ventana y su configuracion.
archivo=open("palabras.txt","r") #creo un archivo y abro palabras.py solo en forma de lectura.
conjuntodepalabras=list(archivo.read().split(","))
palabra=random.choice(conjuntodepalabras)

letraObtenida=StringVar() #declara varieable de tipo cadena
Ventana.title("Juego del ahorcado")
Ventana.config(width=1000,height=600,bg="purple",relief="groove",bd=10)
Ventana.geometry("1000x600")
diagrama=Canvas(Ventana,width=1000,height=600)
diagrama.pack(expand=True,fill="both")
imagenes= [PhotoImage(file="1.png"),PhotoImage(file="2.png"),PhotoImage(file="3.png"),PhotoImage(file="4.png"),PhotoImage(file="5.png"),PhotoImage(file="6.png"),PhotoImage(file="7.png")]

imagen_id=diagrama.create_image(750,300,image=imagenes[6])

Label1=Label(diagrama,text="Introduce cualquier letra:",font=("verdana",24))
Label1.grid(column=0,row=0,padx=10,pady=10)
letras=Entry(diagrama,width=1,font=("verdana",24),textvariable=letraObtenida)
letras.grid(column=1,row=0,padx=10,pady=10)

boton_de_letras=Button(diagrama,text="Probar",bg="pink",command=funcion_probarletra)#en esta parte creo un boton que guarda lass letras.

#letras que faltan ocupar mediante una lista que se ve en la pantalla en forma de abcdario.
LetrasLabel=[Label(diagrama,text=chr(j+97),font=("verdana",20)) for j in range(26)] # chr Saber si una letra está entre determinado rango
                     #de esta forma se despliega el abcdario con todas las letras.
colocarletras()

boton_de_letras.grid(column=0,row=1,pady=10)#aqui configuro la ubicacion de mi boton

guiones=[Label(diagrama,text="_",font=("verdana",30)) for palabra in palabra]
inicialx=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialx,y=400)
    inicialx+=50





Ventana.mainloop()


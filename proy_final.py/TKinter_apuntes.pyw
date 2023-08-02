from tkinter import *

"""ventanas"""


Ventana=Tk()#crear ventana

Ventana.title("prueba")#titulo
# Ventana.iconbitmap("imagenes/logo para prueba.ico")#cambiar logo en el titulo (necesita un archivo .ico)

# Ventana.resizable(1,1)#permiso para editar el tamaño de ventana desde el programa (X,Y)
Ventana.geometry("650x650")#editar tamaño inicial de la ventana (X x Y). Si no se agrega, la ventana toma el tamaño del frame

Ventana.config(bg="blue")#cambiar el color de fondo de la ventana

"""frames"""

# frame1=Frame()#crear frame
# frame1.pack()#agregar el frame a la ventana. 
#si dentro del () se agrega side= se puede anclar el frame a un lado especifico ("left", "rigth","top","bottom")
#se luego del side=, se agrega un anchor= se puede establecer una esquina (n,s,e,w)
#si se escribe fill= se puede hacer que el frame adopte el tamaño de la ventana todo el tiempo (x,y,both,none)
#para que se expanda sobre el eje y se debe agregar el atributo expand=True

# frame1.config(bg="red")#cambiar color del frame
# frame1.config(width=650,height=500)#cambiar tamaño (X,Y)
# frame1.config(relief="groove")#cambiar color del borde
# frame1.config(bd=35)#establece el tamaño del borde
# frame1.config(cursor="pirate")#cambia el cuerosr en el frame

# label1 = Label(Ventana,text="¡Hola Mundo!",bg="red")
# label1.config(height=10,width=10)
# # label1.grid(column=0,row=0)
# # label1.pack(side=LEFT)
# label1.place(x=0,y=0)

# label2 = Label(Ventana,text="¡Hola Mundo!",bg="green",height=100,width=100)
# label2.config(height=1,width=10)
# # label2.grid(column=1,row=1)
# # label2.pack()
# label2.place(x=650,y=0)

label3 = Label(Ventana,text="¡Hola Mundo!",bg="yellow")
label3.config(height=1,width=18)
# label3.grid(column=3,row=3)
# label3.config(text="Adios mundo cruel")
label3.pack()


# label4 = Label(Ventana,text="¡Hola Mundo!",bg="yellow")
# label4.config(height=25,width=25)
# # label4.grid(column=1,row=0)
# label4.pack()

entry=Entry(Ventana,text="¡Hola Mundo!",bg="white")
# entry.grid(column=0,row=1)
entry.pack()

def ejemplo():
    textoDeLaEntry=entry.get()
    label3.config(text=textoDeLaEntry)

def ejemplo2():
    print("Chau")

def Boton():
    ejemplo()
    ejemplo2()

button=Button(Ventana,text="chau",command=Boton)
# button.grid(column=4,row=4)
button.pack()



Ventana.mainloop()#bucle para inicializar una ventana
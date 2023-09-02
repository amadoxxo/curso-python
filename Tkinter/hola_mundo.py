# GUI - Graphical User Interface
# Tkinter - TK Interface
# Importamos el módulo de tkinter
''' import tkinter as tk
# Importamos el módulo del tema de tkinter
from tkinter import ttk

# Creamos un objeto usando la clase tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')
# Cambiamos el nombre de la ventana
ventana.title('Hola mundo')
# Configuramos el ícono de la aplicación
ventana.iconbitmap('icono.ico')

# Creamos un método evento_click
def evento_click():
    boton1.config(text='Botón presionado')
    print('Ejecución del evento_click')
    # Creamos un nuevo botón y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo botón')
    boton2.pack()

# Creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)
# Utilizar el pack layout manager para mostrar el botón de la ventana
boton1.pack()
# Iniciamos la ventana (esto línea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop() '''

import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# width es la cantidad de caracteres que ocupa la caja de texto
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
# state = tk.DISABLED

# Definimos una variable que podremos modificar posteriormente (set), leer(get)
# entrada1_var = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(column=0, row=0)
# insert agrega un texto
# entrada1.insert(0, 'Introduce una cadena')
# entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(column=0, row=1, columnspan=2)

def enviar():
    # print(entrada1.get())
    # boton1.config(text=entrada1.get())
    # Eliminar el contenido
    # entrada1.delete(0, tk.END)
    # Seleccionador el texto de la caja
    # entrada1.select_range(0, tk.END)
    # Para ser efectiva la selección del texto
    # entrada1.focus()

    # Recuperamos la información a partir de la variable asociada con la caja de texto
    # boton1.config(text=entrada1_var.get())
    # Modificación utilizamos la variable de texto y el método set
    # entrada1_var.set('Cambio...')
    # Recuperamos la información
    # print(entrada1_var.get())
    # print(entrada1.get())
    # Modificamos el texto del label
    etiqueta1.config(text=entrada1.get())
    # Messagebox (cajas mensajes)
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')
        # messagebox.showerror('Mensaje Error', mensaje1 + ' Error')
        # messagebox.showwarning('Mensaje Advertencia', mensaje1 + ' Advertencia')

def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos...')
    sys.exit()

def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    #tearoff = False para evitar que se separe el menú de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción al menú de archivo
    submenu_archivo.add_command(label='Nuevo')
    # Agregar separador
    submenu_archivo.add_separator()
    # Agregamos la opción salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # Agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    # Submenu ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción al submenu
    submenu_ayuda.add_command(label='Acerca de')
    # Agregamos al menu principal este nuevo submenu
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(column=1, row=0)

crear_menu()

ventana.mainloop()

'''# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

# def evento2():
    # boton2.config(text='Botón 2 presionado')

# def evento4():
    # boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE, background='yellow')

# Definimos los botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(column=0, row=0, sticky='NSWE', padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)

# N(arriba), E(derecha), S(abajo), W(izquierda)
# boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
# boton2.grid(row=1, column=0, sticky='NSWE')

# Boton3
# boton3 = ttk.Button(ventana, text='Botón 3')
# boton3.grid(column=1, row=0, sticky='NSWE')

# Boton4
# boton4 = tk.Button(ventana, text='Botón 4', command=evento4)
# boton4.grid(column=1, row=1, sticky='NSWE')'''
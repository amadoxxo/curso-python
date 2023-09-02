import tkinter as tk

class Editor(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('GlobalMentoring.com.mx - Editor de Texto')
        # Configuración tamaño mínimo de la venta
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo campo de texto
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        # Atributo del archivo
        self.archivo = None
        # Atributo para saber si ya se abrió un archivo anteriormente
        self.archivo_abierto = False
        # Creación de componentes
        self._crear_componentes()

    def _crear_componentes(self):
        frame_boton = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_boton, text='Abrir')
        boton_guardar = tk.Button(frame_boton, text='Guardar')
        boton_guardar_como = tk.Button(frame_boton, text='Guardar como...')
        # Los botones los expandimos de manera horizontal (sticky='WE')
        boton_abrir.grid(column=0, row=0, sticky='WE', padx=5, pady=5)
        boton_guardar.grid(column=0, row=1, sticky='WE', padx=5, pady=5)
        boton_guardar_como.grid(column=0, row=2, sticky='WE', padx=5, pady=5)
        # Se coloca el frame de manera vertical
        frame_boton.grid(column=0, row=0, sticky='NS')
        # Agregamos el campo de texto, se expandirá por completo el espacio disponible
        self.campo_texto.grid(column=1, row=0, sticky='NSWE')

if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()
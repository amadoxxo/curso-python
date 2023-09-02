import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor del input 
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._creacion_componentes()

    # Métodos de Clase
    # Método para crear los componentes
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50 ,bg='grey')
        entrada_frame.pack(side=tk.TOP)
        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), 
                            textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(column=0,row=0, ipady=10)

        # Creamos otro frame para la parte inferior
        botones_frame = tk.Frame(width=400, height=450, bg='grey')
        botones_frame.pack()

        # Primer renglón
        # Botón limpiar
        boton_limpiar = tk.Button(botones_frame, text='C', width=41, height=4,
                                    bd=0 ,bg='#eee', cursor='hand2', 
                                    command=self._evento_limpiar)
        boton_limpiar.grid(column=0, row=0, columnspan=3, padx=1, pady=1)
        # Botón dividir
        boton_dividir = tk.Button(botones_frame, text='/', width=13, height=4,
                                    bd=0, bg='#eee', cursor='hand2',
                                    command=lambda: self._evento_click('/')
                                    ).grid(column=3, row=0, padx=1, pady=1)
        # boton_dividir.grid(column=3, row=0, padx=1, pady=1)

        # Segundo renglon
        boton_siete = tk.Button(botones_frame, text='7', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(7))
        boton_siete.grid(column=0, row=1, padx=1, pady=1)

        boton_ocho = tk.Button(botones_frame, text='8', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(8))
        boton_ocho.grid(column=1, row=1, padx=1, pady=1)

        boton_nueve = tk.Button(botones_frame, text='9', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(9))
        boton_nueve.grid(column=2, row=1, padx=1, pady=1)

        boton_multiplicacion = tk.Button(botones_frame, text='*', width=13, height=4, 
                                            bd=0, bg='#eee', cursor='hand2',
                                            command=lambda: self._evento_click('*'))
        boton_multiplicacion.grid(column=3, row=1, padx=1, pady=1)

        # Tercer renglon
        boton_cuatro = tk.Button(botones_frame, text='4', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(4))
        boton_cuatro.grid(column=0, row=2, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(5))
        boton_cinco.grid(column=1, row=2, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(6))
        boton_seis.grid(column=2, row=2, padx=1, pady=1)

        boton_resta = tk.Button(botones_frame, text='-', width=13, height=4, 
                                            bd=0, bg='#eee', cursor='hand2',
                                            command=lambda: self._evento_click('-'))
        boton_resta.grid(column=3, row=2, padx=1, pady=1)

        # Cuarto renglon
        boton_uno = tk.Button(botones_frame, text='1', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(1))
        boton_uno.grid(column=0, row=3, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text='2', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(2))
        boton_dos.grid(column=1, row=3, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(3))
        boton_tres.grid(column=2, row=3, padx=1, pady=1)

        boton_sumar = tk.Button(botones_frame, text='+', width=13, height=4, 
                                            bd=0, bg='#eee', cursor='hand2',
                                            command=lambda: self._evento_click('+'))
        boton_sumar.grid(column=3, row=3 ,padx=1, pady=1)

        # Quinto renglon
        boton_cero = tk.Button(botones_frame, text='0', width=27, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click(0))
        boton_cero.grid(column=0, row=4, columnspan=2, padx=1, pady=1)

        boton_punto = tk.Button(botones_frame, text='.', width=13, height=4, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._evento_click('.'))
        boton_punto.grid(column=2, row=4, padx=1, pady=1)

        boton_evaluar = tk.Button(botones_frame, text='=', width=13, height=4, 
                                    bd=0, bg='#eee', cursor='hand2', command= self._evento_evaluar)
        boton_evaluar.grid(column=3, row=4, padx=1, pady=1)

    def _evento_evaluar(self):
        # eval evalua la expresión str una expresión aritmética
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error: {e}')
        finally:
            self.expresion = ''

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento a la expresión ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
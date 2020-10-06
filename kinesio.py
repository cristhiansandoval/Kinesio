#!/usr/bin/env python
# -*- coding: utf-8 -*-
# +-------------------------------------------------------------------------------------+

# Importo las librerias necesrias para el programa

from Tkinter import *
import Tkinter as tk
#import cv2
from PIL import Image, ImageTk
from base_datos import Datos

# Clase Aplicacion
# Argumentos
#   tk.Tk: Método de Tkinter que se usa para la version Python 2.7
class Aplicacion:
    # Función init:
    #    Dibuja la parte de la ventana que funciona como un contenedor
    #    para los botones, campos y etiquetas.
    #    Apila todos los elementos en la parte superior de la ventana,
    #    y lo va haciendo en orden de declaración como se ve más abajo.
    #    Manejo de la ventana por parte de la función:
    #    +-----------------------------------------------------------+
    #    | Tk |  Kinesio                                       - O X |
    #    +-----------------------------------------------------------+
    #    |                                                           |
    #    |                                                           |
    #    |     self.imagen1 = tk.Label(ImageTk.PhotoImage()         |
    #    |                                                           |
    #    |                                                           |
    #    +-----------------------------------------------------------+
    #    |           self.etiq1 = tk.Label(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |           self.id_user = Spinbox(self.raiz, ...)          |
    #    +-----------------------------------------------------------+
    #    |           self.etiq2 = tk.Label(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |           self.id_puertas = Spinbox(self.raiz, ...)       |
    #    +-----------------------------------------------------------+
    #    |           self.etiq2 = tk.Label(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |           self.fotos = Spinbox(self.raiz, ...)            |
    #    +-----------------------------------------------------------+
    #    |           self.etiq3 = tk.Label(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |           self.email = tk.Entry(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |           self.etiq4 = tk.Label(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |     self.boton_capturar = tk.Button(self.raiz, ...)      |
    #    +-----------------------------------------------------------+
    #    |           self.etiq5 = tk.Label(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |     self.boton_entrenar = tk.Button(self.raiz, ...)      |
    #    +-----------------------------------------------------------+
    #    |           self.etiq6 = tk.Label(self.raiz, text)         |
    #    +-----------------------------------------------------------+
    #    |     self.boton_detectar = tk.Button(self.raiz, ...)      |
    #    +-----------------------------------------------------------+
    #    | self.separ1 = tk.Separator(self.raiz, orient=HORIZONTAL) |
    #    +-----------------------------------------------------------+
    #    |   self.boton_configuracion  |     self.boton_salir        |
    #    +-----------------------------------------------------------+
    # Argumentos:
    #	self: Variable que indica que estamos en el ambito de la
    #   ventana. (self.raiz , o de esta puede salir un
    #   self.ventan1 por ejemplo)
    # Retorno:
    #   No tiene valores de retorno
    #
    # Varibles auxiliares para las ventanas modales
    ventana=0
    posx_y=0
    def __init__(self, raiz):
        self.raiz = tk.Tk()
        self.raiz.title("Kinesio")
        # Se declara variables de control
        self.id_paciente = IntVar(value=1)
        self.pacientes = StringVar(value='')
        # Se agregaa una traza a el id_paciente para detectar que hayan
        # cambios y pueda impactar el cambio en el campo de pacientes
        self.id_paciente.trace('r', self.buscar)
        # Llama a la   funcion buscar para trar el nombre de la BD
        self.buscar()
        # Carga imagen para asociar a la parte de arriba de la ventana
        ubicacion_imagen ='kinesio.png'
        logotipo = ImageTk.PhotoImage(Image.open(ubicacion_imagen))
        # Defino uno por uno los elementos de la ventana.
        self.imagen1 = tk.Label(self.raiz, image=logotipo,
                                 anchor="center")
        self.etiq1 = tk.Label(self.raiz, text="Número de paciente:")
        self.id_paciente = Spinbox(self.raiz, from_=1, to=1000, wrap=True,
                             textvariable=self.id_paciente,
                             state='readonly')
        self.etiq2 = tk.Label(self.raiz, text="Paciente:")
        self.paciente = tk.Entry(self.raiz, textvariable=self.pacientes,
                               width=10)
        self.etiq3 = tk.Label(self.raiz, text="Presione el siguiente botón para comenzar a registrar los ejercicios:")
        self.boton_ejercitar = tk.Button(self.raiz, text="Ejercitar",
                                 command=self.funcion_ejercitar)
        self.etiq4 = tk.Label(self.raiz, text="Presione el siguiente botón para ver reportes:")
        self.boton_reportar = tk.Button(self.raiz, text="Reportes",
                                 command=self.funcion_reportes)
        self.etiq5 = tk.Label(self.raiz, text="Software desarrollado por Favio")
        self.boton_configurar = tk.Button(self.raiz, text="Configuración",
                                 command=self.funcion_configuracion)
        self.boton_salir = tk.Button(self.raiz, text="Salir",
                                 command=quit)
        # Apilo hacia arriba los elementos de la ventana: uno por uno.
        self.imagen1.pack(side=TOP, fill=BOTH, expand=True,
                          padx=10, pady=5)
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.id_paciente.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.paciente.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.etiq3.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.boton_ejercitar.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.etiq4.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.boton_reportar.pack(side=TOP, fill=BOTH, expand=True,
                         padx=10, pady=10)
        self.etiq5.pack(side=TOP, fill=BOTH, expand=True,
                       padx=10, pady=5)
        self.boton_configurar.pack(side=LEFT, fill=BOTH, expand=True,
                        padx=10, pady=10)
        self.boton_salir.pack(side=RIGHT, fill=BOTH, expand=True,
                         padx=10, pady=10)
        self.raiz.mainloop()
    # Función buscar:
    #    Busca en la base de datos el nombre del paciente en base
    #    al id del paciente en el campo corresponiente.
    # Argumentos:
    #	self: Variable que indica que eestamos en el ambito de la
    #   ventana. (self.raiz , o de esta puede salir un
    #   self.ventana1 por ejemplo)
    # Retorno:
    #   No tiene valores de retorno
    def buscar(self, *args):
        error_dato = False
        try:
            nro_paciente = int(self.id_paciente.get())
        except:
            error_dato = True
        if not error_dato:
            self.pacientes.set(Datos(self.id_paciente.get()).buscarPaciente())
        else:
            self.total.set("¡ERROR!")
    # Función ejercitar:
    #    Se activa al presionar el botón Ejecitar, instancia un objeto
    #    del tipo Ejercicios y llama al método comenzar
    # Argumentos:
    #	self: Variable que indica que eestamos en el ambito de la
    #   ventana. (self.raiz , o de esta puede salir un
    #   self.ventana1 por ejemplo)
    # Retorno:
    #   No tiene valores de retorno
    def funcion_ejercitar(self):
        # Instancio
        cadena = '0X0Y0Z-348A28B16724C'

        # Llamo
    # Función ejercitar:
    #    Se activa al presionar el botón Ejecitar, instancia un objeto
    #    del tipo Ejercicios y llama al método comenzar
    # Argumentos:
    #	self: Variable que indica que eestamos en el ambito de la
    #   ventana. (self.raiz , o de esta puede salir un
    #   self.ventana1 por ejemplo)
    # Retorno:
    #   No tiene valores de retorno
    def funcion_reportes(self):
        # Instancio
        self.buscar()
        # Llamo

	# Función configuración:
    #    Se activa al presionar el botón Configuración
    # Argumentos:
    #	self: Variable que indica que estamos en el ambito de la
    #   ventana. (self.raiz , o de esta puede salir un
    #   self.ventana1 por ejemplo). Hace que se ejecute despues del click.
    # Retorno:
    #   No tiene valores de retorno
    def funcion_configuracion(self):
        Configuracion(self.raiz)
# Clase Configuración
class Configuracion:
    def __init__(self, parent):
        # Se declaran las variables auxiliares y de control
        self.i = 0
        self.habilitado = False
        self.persona = StringVar(value='')
        # Se generan los componentes graficos de identica manera a lo explicado en la funcion init raiz
        self.hija = Toplevel(parent)
        self.hija.title("Configuración")
        self.etiq1 = tk.Label(self.hija, text="Configuración de nombres de las personas permitidas a ingresar")
        self.campo_usuario = tk.Entry(self.hija, textvariable=self.persona, width=10)
        self.agregar = tk.Button(self.hija, text="Agregar", command=self.funcion_agregar)
        self.etiq2 = tk.Label(self.hija, text="Número y Nombre de la persona")
        self.numeros = tk.Listbox(self.hija)
        self.lista = tk.Listbox(self.hija)
        self.etiq3 = tk.Label(self.hija, text="Escriba el nombre en el campo superior vacío")
        for linea in Datos(1).todosLosPacientes():
            self.lista.insert(self.i, Datos(1).todosLosPacientes()[self.i])
            self.numeros.insert(self.i, Datos(1).buscarNumero(Datos(1).todosLosPacientes()[self.i]))
            self.i+=1
        # Se ubican los correspondientes elementos graficos en orden
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.campo_usuario.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=10)
        self.agregar.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.numeros.pack(side=LEFT, fill=tk.Y, expand=1, padx=1, pady=5)
        self.lista.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=5)
        # Se verfica que la lista tenga elementos, en tal caso, que muestre el boton quitar
        if self.lista.size() > 0:
		       self.etiq3['text'] = "Escriba, seleccione y luego presione el botón para quitar:"
		       self.quitar = tk.Button(self.hija, text="Quitar", command=self.funcion_quitar)
		       self.quitar.pack(side=BOTTOM, fill=BOTH, expand=True, padx=10, pady=5)
		       self.habilitado = True
        self.etiq3.pack(side=BOTTOM, fill=BOTH, expand=True, padx=10, pady=5)
        self.hija.mainloop()
    def funcion_agregar(self):
	    if self.lista.size() > 0 and self.habilitado == False:
		    self.etiq3['text']="Escriba, seleccione y luego presione el botón para quitar:"
		    self.quitar = tk.Button(self.hija, text="Quitar", command=self.funcion_quitar)
		    self.quitar.pack(side=BOTTOM, fill=BOTH, expand=True, padx=10, pady=5)
		    self.habilitado = True
	    if (self.campo_usuario.get() != ''):
              self.lista.insert(END, Datos(self.i+1).agregarPaciente(self.campo_usuario.get()))
              self.numeros.insert(END, Datos(1).buscarNumero(Datos(1).todosLosPacientes()[self.i]))
              self.i = self.lista.size()+1

    def funcion_quitar(self):
		# Se valida se haya seleccionado algún elemento para poder operar
	    if self.lista.curselection():
		    seleccion = self.lista.curselection()
            Datos(int(str(self.numeros.get(seleccion))[1:2])).quitarPaciente()
            self.lista.delete(seleccion)
            self.numeros.delete(seleccion)
		# Si la lista esta vacia se cierra la ventana
	    if self.lista.size() == 0:
		    self.habilitado = False
            self.hija.destroy()

# Función main:
    #   Define la aplicación que se encuentra en la ventana,
    # Argumentos:
    #	No tiene argumentos

    # Retorno:
    #   Devuelve un valor 0.
def main():
    raiz = tk.Tk
    mi_app = Aplicacion(raiz)
    return 0

if __name__ == '__main__':
    main()

#En Esta Parte Del Codigo Se Realiza La Parte Fronted De La Aplicacion

import tkinter as tk
from tkinter import ttk
from model.pelicula_dao import *

#Barra De Menu
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff = 0) 
    barra_menu.add_cascade(label = "Inicio",  menu = menu_inicio)
    
    menu_inicio.add_command(label = "Crear Tabla", command = crear_tabla)
    menu_inicio.add_command(label = "Eliminar Tabla", command = borrar_tabla)
    menu_inicio.add_command(label = "Salir", command = exit)
    
    menu_consultas = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Consultas", menu = menu_consultas)
    
    menu_consultas.add_command(label = "Listar Registros", command = listar_registro)
    menu_consultas.add_command(label = "Exportar Registros", command = exportar_registro)
    
    menu_estadisticas = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Estadisticas", menu = menu_estadisticas)
    
    menu_estadisticas.add_command(label = "Películas Por Género", command = peliculas_por_genero)
    menu_estadisticas.add_command(label = "Duración Promedio De Las Películas", command = duracion_promedio)
    menu_estadisticas.add_command(label = "Cantidad Total De Películas", command = total_peliculas)    
        
    
    menu_ayuda = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Ayuda", menu = menu_ayuda)
    
    menu_ayuda.add_command(label = "Manual", command = manual)
    menu_ayuda.add_command(label = "Contacto", command = contacto)
      
#Frame De La Aplicacion Y Funciones Para Crear, Editar, Eliminar Y Listar Los Registros
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320,)
        self.root = root
        self.pack()
        self.id_pelicula = None
       
        
        
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
        
    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text = "Nombre: " )
        self.label_nombre.config(font = ("Arial", 12, "bold") )
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.label_duracion = tk.Label(self, text = "Duracion: " )
        self.label_duracion.config(font = ("Arial", 12, "bold") )
        self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.label_genero = tk.Label(self, text = "Genero: " )
        self.label_genero.config(font = ("Arial", 12, "bold") )
        self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10)
        
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width = 50, font = ("Arial", 12) )
        self.entry_nombre.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable = self.mi_duracion)
        self.entry_duracion.config(width = 50 , font = ("Arial", 12))
        self.entry_duracion.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)
        self.entry_genero.config(width = 50,  font = ("Arial", 12))
        self.entry_genero.grid(row = 2, column = 1, columnspan = 2, padx = 10, pady = 10)        
 
        self.boton_nuevo = tk.Button(self, text="Nuevo", command = self.habilitar_campos)
        self.boton_nuevo.config(width = 20, cursor = "hand2",  activebackground = "#5E5ADD", font = ("Arial", 12, "bold"), fg = "white", bg = "#0C087A")
        self.boton_nuevo.grid(row = 3, column = 0,  padx = 10, pady = 10)
            
        self.boton_guardar = tk.Button(self, text="Guardar", command = self.guardar_datos)
        self.boton_guardar.config(width = 20, cursor = "hand2", activebackground = "#7DED52", font = ("Arial", 12, "bold"), fg = "white", bg = "#2D8E06")
        self.boton_guardar.grid(row = 3, column = 1,  padx = 10, pady = 10)
                
        self.boton_cancelar = tk.Button(self, text="Cancelar", command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20, cursor = "hand2", activebackground = "#F76C6D", font = ("Arial", 12, "bold"), fg = "white", bg = "#E4080A")
        self.boton_cancelar.grid(row = 3, column = 2,  padx = 10, pady = 10)
        
    def habilitar_campos(self):
        self.entry_nombre.config(state="normal")
        self.entry_duracion.config(state="normal")
        self.entry_genero.config(state="normal")
        
        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal") 
        
    def deshabilitar_campos(self):
        self.id_pelicula = None
        
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")
        
        self.entry_nombre.config(state="disabled")
        self.entry_duracion.config(state="disabled")
        self.entry_genero.config(state="disabled")
        
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")
        
    def guardar_datos(self):
        
        
        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get()
        )
        
       
        if self.id_pelicula == None:
           guardar(pelicula)
        else:
           editar(pelicula, self.id_pelicula)

        
        self.tabla_peliculas()
        
        self.deshabilitar_campos()
        
        
    def tabla_peliculas(self):
        
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        self.tabla =ttk.Treeview(self, 
        column = ("Nombre", "Duracion", "Genero"))
        self.tabla.grid(row = 4, column = 0, columnspan = 4, sticky = "nse")
        
        self.scroll = ttk.Scrollbar(self, orient = "vertical", command = self.tabla.yview)
        self.scroll.grid(row = 4, column = 4, sticky = "nse")
        self.tabla.configure(yscrollcommand = self.scroll.set)
        
        self.tabla.heading("#0", text = "ID")
        self.tabla.heading("#1", text = "Nombre")
        self.tabla.heading("#2", text = "Duración")
        self.tabla.heading("#3", text = "Genero")

        for p in self.lista_peliculas:
            self.tabla.insert("",0, text = p[0], values = (p[1], p[2], p[3]))

        self.boton_editar = tk.Button(self, text="Editar", command = self.editar_datos)
        self.boton_editar.config(width = 20, cursor = "hand2",  activebackground = "#5E5ADD", font = ("Arial", 12, "bold"), fg = "white", bg = "#0C087A")
        self.boton_editar.grid(row = 5, column = 0,  padx = 10, pady = 10)
        
                 
        self.boton_eliminar = tk.Button(self, text="Eliminar", command = self.eliminar_datos)
        self.boton_eliminar.config(width = 20, cursor = "hand2", activebackground = "#F76C6D", font = ("Arial", 12, "bold"), fg = "white", bg = "#E4080A")
        self.boton_eliminar.grid(row = 5, column = 1,  padx = 10, pady = 10)
            
     
    def editar_datos(self):
        try: 
            self.id_pelicula = self.tabla.item(self.tabla.selection())["text"]
            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection())["values"][0]
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection())["values"][1]
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection())["values"][2]

            self.habilitar_campos()
            
            
            self.entry_nombre.delete(0, tk.END)
            self.entry_duracion.delete(0, tk.END)
            self.entry_genero.delete(0, tk.END)

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)

        except:
            titulo = "Edición De Datos"
            mensaje = "No Ha Seleccionado Ningun Registro"
            messagebox.showerror(titulo, mensaje)
            
    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())["text"]
            eliminar(self.id_pelicula)


            self.tabla_peliculas()
            self.id_pelicula = None
        except:
            titulo = "Eliminar Un Registro"
            mensaje = "No Ha Seleccionado Ningun Registro"
            messagebox.showerror(titulo, mensaje)
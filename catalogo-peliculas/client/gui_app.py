import tkinter as tk    
from tkinter import ttk
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar
from tkinter import messagebox

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label = 'inicio', menu = menu_inicio)
    
    menu_inicio.add_command(label='crear registro DB', command=crear_tabla)
    menu_inicio.add_command(label='eliminar registro DB', command=borrar_tabla)
    menu_inicio.add_command(label='salir', command= root.destroy)
    
    barra_menu.add_cascade(label = 'consultas')
    barra_menu.add_cascade(label = 'configuracion')
    barra_menu.add_cascade(label = 'ayuda')
    
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 800, height = 600)
        self.root = root
        self.pack()
        self.id_pelicula = None
        self.campos_peliculas()
        self.deshabilitar_campos()
        self.tabla_peliculas()
        #self.config(bg = 'green')
        
    def campos_peliculas(self):
        self.label_nombre = tk.Label(self, text = 'nombre: ')
        self.label_nombre.config(font = ('arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.label_duracion = tk.Label(self, text = 'duracion: ')
        self.label_duracion.config(font = ('arial', 12, 'bold'))
        self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.label_genero = tk.Label(self, text = 'genero: ')
        self.label_genero.config(font = ('arial', 12, 'bold'))
        self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10)
        
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        self.entry_nombre.config(width= 50, font = ('arial', 12))
        self.entry_nombre.grid(row = 0, column= 1, padx = 10, pady = 10, columnspan=2)
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable= self.mi_duracion)
        self.entry_duracion.config(width= 50, font = ('arial', 12))
        self.entry_duracion.grid(row = 1, column= 1, padx = 10, pady = 10, columnspan=2)
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)
        self.entry_genero.config(width= 50, font = ('arial', 12))
        self.entry_genero.grid(row = 2, column= 1, padx = 10, pady = 10, columnspan=2)
        
        self.boton_nuevo = tk.Button(self, text='nuevo', command= self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('arial', 12, 'bold'), fg = '#DAD5D6', bg='#9d9702', cursor = 'hand2', activebackground='#f2fe95')
        self.boton_nuevo.grid(row=3, column= 0, padx = 10, pady = 10)
        
        self.boton_guardar = tk.Button(self, text='guardar', command= self.guardar_datos)
        self.boton_guardar.config(width=20, font=('arial', 12, 'bold'), fg = '#DAD5D6', bg='#1658A2', cursor = 'hand2', activebackground='#87CEFA')
        self.boton_guardar.grid(row=3, column= 1, padx = 10, pady = 10)
        
        self.boton_cancelar = tk.Button(self, text='cancelar', command= self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('arial', 12, 'bold'), fg = '#DAD5D6', bg='#fc9403', cursor = 'hand2', activebackground='#fdb249')
        self.boton_cancelar.grid(row=3, column= 2, padx = 10, pady = 10)
        

        self.label_busqueda = tk.Label(self, text='Buscar:')
        self.label_busqueda.config(font = ('arial', 12, 'bold'))
        self.label_busqueda.grid(row=6, column=0, padx=10, pady=10)

        self.entrada_busqueda = tk.Entry(self)
        self.entrada_busqueda.grid(row=6, column=1, padx=10, pady=10)

        self.boton_buscar = tk.Button(self, text='Buscar', command=self.buscar_peliculas)
        self.boton_buscar.config(width=20, font=('arial', 12, 'bold'), fg = '#DAD5D6', bg='#57005c', cursor = 'hand2', activebackground='#ae00b8')
        self.boton_buscar.grid(row=6, column=2, padx=10, pady=10)
        # Agregar evento para buscar al presionar "Enter"
        self.entrada_busqueda.bind('<Return>', lambda event: self.buscar_peliculas())
        
        self.boton_restablecer = tk.Button(self, text='Restablecer', command=self.cargar_todas_peliculas)
        self.boton_restablecer.config(width=20, font=('arial', 12, 'bold'), fg = '#DAD5D6', bg='#011f00', cursor = 'hand2', activebackground='#7a7a7a')
        self.boton_restablecer.grid(row=6, column=3, padx=10, pady=10)
        
    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
            
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
        
    def deshabilitar_campos(self):
        self.id_pelicula = None
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
            
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        
    def guardar_datos(self):
        if not self.mi_nombre.get() or not self.mi_duracion.get() or not self.mi_genero.get():
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos antes de guardar.")
            return
        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
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
        
        self.tabla = ttk.Treeview(self, column= ('Nombre', 'Duracion', 'Genero'))
        self.tabla.grid(row= 4, column= 0, columnspan= 4, sticky= 'nse')
        
        #sacrolbar para la tabla si exede 10 registros
        self.scroll = ttk.Scrollbar(self, orient ='vertical', command= self.tabla.yview)
        self.scroll.grid(row= 4, column = 4, sticky= 'nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')
        
        for p in self.lista_peliculas:
            self.tabla.insert('',0, text=p[0], values=(p[1], p[2] , p[3]))
        
        self.boton_editar = tk.Button(self, text='editar', command= self.editar_datos)
        self.boton_editar.config(width=20, font=('arial', 12, 'bold'), fg = '#DAD5D6', bg='#158645', cursor = 'hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column= 0, padx = 10, pady = 10)
        
        self.boton_eliminar = tk.Button(self, text='eliminar', command= self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=('arial', 12, 'bold'), fg = '#DAD5D6', bg='#BD152E', cursor = 'hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=5, column= 1, padx = 10, pady = 10)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_campos()
            
            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
            
        except:
            titulo = 'edicion de datos'
            mensaje = 'no ah seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)   
    
    def eliminar_datos(self):
        try:
            seleccion = self.tabla.selection()
            if seleccion:
                self.id_pelicula = self.tabla.item(seleccion)['text']
                eliminar(self.id_pelicula)
                self.tabla_peliculas()
                self.id_pelicula = None
                #messagebox.showinfo('Eliminar datos', 'La película ha sido eliminada con éxito.')
            else:
                raise Exception("No ha seleccionado ningún registro.")
        except Exception as e:
            titulo = 'Eliminar datos'
            mensaje = str(e)
            messagebox.showerror(titulo, mensaje)   
            
    def buscar_peliculas(self):
        criterio = self.entrada_busqueda.get().lower()
        self.lista_peliculas = listar()  # Obtener todas las películas.
        # Filtrar películas que contengan el criterio en el nombre o género
        peliculas_filtradas = [
            p for p in self.lista_peliculas 
            if criterio in p[1].lower() or criterio in p[3].lower()
        ]
        # Actualizar la tabla con las películas filtradas
        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla
        for p in peliculas_filtradas:
            self.tabla.insert('', 'end', text=p[0], values=(p[1], p[2], p[3]))
            
    def cargar_todas_peliculas(self):
        self.lista_peliculas = listar()  # Obtener todas las películas
        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla
        for p in self.lista_peliculas:
            self.tabla.insert('', 'end', text=p[0], values=(p[1], p[2], p[3]))

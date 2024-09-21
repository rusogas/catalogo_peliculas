import tkinter as tk      
from client.gui_app import Frame, barra_menu
import os
from tkinter import messagebox
def main():
    root = tk.Tk()
    root.title('catalogo de peliculas')
    root.geometry('1000x700')
    #root.iconbitmap('img/cp-logo.ico')
    icon_path = os.path.join(os.path.dirname(__file__), 'img', 'cine.ico')
    
    if os.path.isfile(icon_path):
        try:
            root.iconbitmap(icon_path)
        except tk.TclError as e:
            messagebox.showwarning("Advertencia", f"No se pudo cargar el icono: {e}")
    else:
        messagebox.showwarning("Advertencia", "El archivo de icono no se encuentra en la ruta especificada.")
    root.resizable(0,0)
    barra_menu(root)
    
    app = Frame(root = root)
   
    app.mainloop()
    

if __name__ == '__main__':
    main()
import tkinter as tk
from tkinter import messagebox, ttk
from negocio import LogicaNegocio

class VentanaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Café Conecta - Acceso al Sistema")
        self.root.geometry("450x480")
        self.root.config(bg="#ffffff")

        # Título principal
        tk.Label(root, text="Café Conecta", font=("Arial", 20, "bold"), bg="#ffffff", fg="#2e5a27").pack(pady=(25, 5))
        tk.Label(root, text="Iniciar Sesión", font=("Arial", 12), bg="#ffffff", fg="#666666").pack(pady=(0, 20))

        # Campo Usuario
        tk.Label(root, text="Usuario", font=("Arial", 11), bg="#ffffff", fg="#333333").pack(anchor="w", padx=60)
        self.txt_usuario = tk.Entry(root, font=("Arial", 11), width=32, bd=1, relief="solid")
        self.txt_usuario.pack(pady=5, padx=60, ipady=4)

        # Campo Contraseña
        tk.Label(root, text="Contraseña", font=("Arial", 11), bg="#ffffff", fg="#333333").pack(anchor="w", padx=60, pady=(10, 0))
        self.txt_password = tk.Entry(root, font=("Arial", 11), width=32, show="*", bd=1, relief="solid")
        self.txt_password.pack(pady=5, padx=60, ipady=4)

        # Botón Ingresar
        btn_ingresar = tk.Button(root, text="Ingresar", font=("Arial", 11, "bold"), bg="#4a7c39", fg="white", width=28, bd=0, cursor="hand2", command=self.f_ingresar)
        btn_ingresar.pack(pady=20, ipady=6)

        # Enlaces inferiores (Registrarse y Recuperar contraseña)
        frame_links = tk.Frame(root, bg="#ffffff")
        frame_links.pack(pady=10)

        btn_registrar = tk.Button(frame_links, text="Registrarse", font=("Arial", 9), fg="#4a7c39", bg="#ffffff", bd=0, cursor="hand2", command=self.f_registrar)
        btn_registrar.grid(row=0, column=0, padx=15)

        btn_olvido = tk.Button(frame_links, text="¿Olvidaste tu contraseña?", font=("Arial", 9), fg="#4a7c39", bg="#ffffff", bd=0, cursor="hand2", command=self.f_recuperar)
        btn_olvido.grid(row=0, column=1, padx=15)

    def f_ingresar(self):
        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get().strip()
        
        # Validaciones de negocio
        resultado = LogicaNegocio.autenticar_usuario(usuario, password)
        messagebox.showinfo("Resultado", resultado["mensaje"])
        
        if resultado["exito"]:
            self.root.destroy()
            abrir_menu_principal()

    def f_registrar(self):
        messagebox.showinfo("Registro", "Cargando formulario Gestión Persona para registro...")

    def f_recuperar(self):
        usuario_o_correo = self.txt_usuario.get().strip()
        resultado = LogicaNegocio.procesar_recuperacion(usuario_o_correo)
        messagebox.showinfo("Recuperación de Credenciales", resultado["mensaje"])


def abrir_menu_principal():
    menu = tk.Tk()
    menu.title("Café Conecta - Menú Principal")
    menu.geometry("650x420")
    menu.config(bg="#f4f6f4")

    tk.Label(menu, text="Café Conecta - Panel de Gestión", font=("Arial", 16, "bold"), bg="#f4f6f4", fg="#2e5a27").pack(pady=25)
    tk.Label(menu, text="Seleccione el módulo que desea administrar:", font=("Arial", 10), bg="#f4f6f4", fg="#555").pack(pady=5)

    frame_btns = tk.Frame(menu, bg="#f4f6f4")
    frame_btns.pack(pady=30)

    tk.Button(frame_btns, text="Administrar Perfiles", font=("Arial", 10, "bold"), bg="#2e5a27", fg="white", width=20, height=2, command=lambda: abrir_crud("Perfil")).grid(row=0, column=0, padx=10)
    tk.Button(frame_btns, text="Administrar Personas", font=("Arial", 10, "bold"), bg="#4a7c39", fg="white", width=20, height=2, command=lambda: abrir_crud("Persona")).grid(row=0, column=1, padx=10)
    tk.Button(frame_btns, text="Administrar Usuarios", font=("Arial", 10, "bold"), bg="#386641", fg="white", width=20, height=2, command=lambda: abrir_crud("Usuario")).grid(row=0, column=2, padx=10)

    menu.mainloop()


def abrir_crud(entidad):
    ventana_crud = tk.Toplevel()
    ventana_crud.title(f"Café Conecta - Gestión de {entidad}")
    ventana_crud.geometry("650x400")
    
    tk.Label(ventana_crud, text=f"Gestión de {entidad}", font=("Arial", 14, "bold"), fg="#2e5a27").pack(pady=15)

    frame_acciones = tk.Frame(ventana_crud)
    frame_acciones.pack(pady=10)

    tk.Button(frame_acciones, text="Guardar", bg="#4a7c39", fg="white", width=10).grid(row=0, column=0, padx=5)
    tk.Button(frame_acciones, text="Modificar", bg="#d4a373", fg="white", width=10).grid(row=0, column=1, padx=5)
    tk.Button(frame_acciones, text="Inhabilitar", bg="#bc6c25", fg="white", width=10, command=lambda: accion_inhabilitar(entidad)).grid(row=0, column=2, padx=5)
    tk.Button(frame_acciones, text="Consultar", bg="#606c38", fg="white", width=10).grid(row=0, column=3, padx=5)

    cols = ("ID", "Detalle Principal", "Estado")
    tabla = ttk.Treeview(ventana_crud, columns=cols, show="headings", height=8)
    for col in cols:
        tabla.heading(col, text=col)
        tabla.column(col, width=180)
    tabla.pack(pady=15)

def accion_inhabilitar(entidad):
    # Prueba del borrado lógico (cambio de estado a Inactivo)
    resultado = LogicaNegocio.ejecutar_borrado_logico(entidad, 1)
    messagebox.showinfo("Borrado Lógico", resultado["mensaje"])

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaLogin(root)
    root.mainloop()
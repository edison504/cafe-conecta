import mysql.connector
from tkinter import messagebox

def conectar_bd():
    """Establece la conexión con la base de datos MySQL de Café Conecta."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cafeconecta"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos: {err}")
        return None
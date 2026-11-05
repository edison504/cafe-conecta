from conexion import conectar_bd

class DatosModelo:
    
    @staticmethod
    def validar_credenciales(usuario, password):
        """Consulta relacional para verificar el usuario y contraseña activos."""
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT u.*, p.descripc as perfil 
                FROM usuario u 
                INNER JOIN Perfil p ON u.idperfil = p.Idperfil 
                WHERE u.nombreu = %s AND u.contrasena = %s AND u.estado = 'Activo'
            """
            cursor.execute(sql, (usuario, password))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            return resultado
        return None

    @staticmethod
    def obtener_datos_recuperacion(usuario_o_correo):
        """Busca el usuario y correo relacionado para la recuperación de claves."""
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            sql = """
                SELECT u.nombreu, u.contrasena, per.correo 
                FROM usuario u 
                INNER JOIN Persona per ON u.idpersona = per.Idpersona 
                WHERE u.nombreu = %s OR per.correo = %s
            """
            cursor.execute(sql, (usuario_o_correo, usuario_o_correo))
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            return resultado
        return None

    @staticmethod
    def inhabilitar_registro_bd(tabla, id_registro):
        """Ejecuta el borrado lógico cambiando el estado a 'Inactivo' sin borrar físicamente[cite: 9]."""
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            if tabla == "Perfil":
                sql = "UPDATE Perfil SET estado = 'Inactivo' WHERE Idperfil = %s"
            elif tabla == "Persona":
                sql = "UPDATE Persona SET estado = 'Inactivo' WHERE Idpersona = %s"
            elif tabla == "Usuario":
                sql = "UPDATE usuario SET estado = 'Inactivo' WHERE Idusuario = %s"
            else:
                return False
            
            cursor.execute(sql, (id_registro,))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        return False
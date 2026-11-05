from datos import DatosModelo

class LogicaNegocio:

    @staticmethod
    def autenticar_usuario(usuario, password):
        """Valida las reglas de campos vacíos y credenciales para el Login."""
        if not usuario or not password:
            return {"exito": False, "mensaje": "Los campos de usuario y contraseña no pueden estar vacíos."}
        
        resultado = DatosModelo.validar_credenciales(usuario, password)
        if resultado:
            return {"exito": True, "mensaje": f"Bienvenido, {usuario}", "datos": resultado}
        else:
            return {"exito": False, "mensaje": "El usuario no se encuentra registrado o las credenciales son incorrectas."}

    @staticmethod
    def procesar_recuperacion(usuario_o_correo):
        """Gestiona la recuperación de claves y retorna el mensaje obligatorio exigido en el parcial[cite: 9]."""
        if not usuario_o_correo:
            return {"exito": False, "mensaje": "Por favor, digite su usuario o correo electrónico en el campo de usuario para la recuperación."}
        
        info_usuario = DatosModelo.obtener_datos_recuperacion(usuario_o_correo)
        if info_usuario:
            # Mensaje obligatorio solicitado en el documento del parcial[cite: 9]
            return {"exito": True, "mensaje": "Su usuario y contraseña fue enviado al correo registrado."}
        else:
            # Mensaje obligatorio si el usuario no existe[cite: 9]
            return {"exito": False, "mensaje": "El usuario no se encuentra registrado."}

    @staticmethod
    def ejecutar_borrado_logico(entidad, id_registro):
        """Coordina el borrado lógico (cambio de estado a inactivo)[cite: 9]."""
        if not id_registro:
            return {"exito": False, "mensaje": "Debe indicar el ID del registro a inhabilitar."}
        
        exito = DatosModelo.inhabilitar_registro_bd(entidad, id_registro)
        if exito:
            return {"exito": True, "mensaje": f"El registro de {entidad} fue inhabilitado correctamente (Borrado Lógico)."}
        else:
            return {"exito": False, "mensaje": "Error al inhabilitar el registro."}
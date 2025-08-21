class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje, codigo):
        super().__init__(mensaje)
        self.codigo = codigo

try:
    raise MiExcepcionPersonalizada("Ocurrió un error personalizado", 404)
except MiExcepcionPersonalizada as e:
    print(f"❌ Código de error: {e.codigo}, Mensaje: {e}")

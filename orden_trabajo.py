class OrdenTrabajo:

    def __init__(self,fecha,patente):
        self.fecha=fecha
        self.patente=patente
        self.estado="pendiente"
        # composición (cada orden tiene su info)
        self.reparaciones = []
        self.repuestos = []
        self.factura = None

    def mostrar_info(self):
        return (f"patente: {self.patente}, "
                f"fecha: {self.fecha}, "
                f"estado: {self.estado}")
    def cambiar_estado(self,nuevo_estado):
        self.estado=nuevo_estado

class Factura:
    def __init__(self,monto,fecha_pago,tipo_pago):
        self.monto=monto
        self.fecha_pago=fecha_pago
        self.tipo_pago=tipo_pago
    def mostrar_info(self):
        return f"Usted realizó un pago de un monto de {self.monto}, el día {self.fecha_pago} en {self.tipo_pago}"
    
class Reparacion:
    def __init__(self, tipo_reparacion,descripcion):
        self.tipo_reparacion=tipo_reparacion
        self.descripcion=descripcion
    def mostrar_info(self):
        return f"El tipo de reparación que se le hizo fue {self.tipo_reparacion} que consiste en {self.descripcion}"

class Repuesto:
    def __init__(self,nombre,stock,precio):
        self.nombre=nombre
        self.stock=stock
        self.precio=precio
    def mostrar_info(self):
        return (f"nombre del repuesto: {self.nombre} "
                f"stock: {self.stock} "
                f"precio: {self.precio}")
    
    
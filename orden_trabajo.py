class ordenTrabajo:

    def __init__(self,ticket,fecha,patente):
        self.ticket=ticket
        self.fecha=fecha
        self.patente=patente
        self.estado="pendiente"

    def mostrar_info(self):
        return (f"ticket: {self.ticket}, "
                f"patente: {self.patente}, "
                f"fecha: {self.fecha}, "
                f"estado: {self.estado}")
    def cambiar_estado(self,nuevo_estado):
        self.estado=nuevo_estado
    

c=ordenTrabajo(2,"24/4","cku44")
print (c.mostrar_info())
cm=c.cambiar_estado("reparado")
print(c.mostrar_info())
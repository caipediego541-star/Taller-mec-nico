class vehiculo:
    def __init__(self,patente,marca,modelo,año):
        self.patente=patente
        self.marca=marca
        self.modelo=modelo
        self.año=año
    
    def mostrar_vehiculo(self):
        return f"vehiculo: patente[{self.patente}],marca: [{self.marca}],modelo: [{self.año}]"
    
    

from p_estructural import p_estructural

class p_enzimatica(p_estructural):
    def __init__(self, nombre, descripcion, secuencia,tipo,substrato):
        super().__init__(nombre, descripcion, secuencia,tipo)
        self._substrato = substrato
    
    @property
    def asigna_substrato(self):
            return self._substrato        
    
    @asigna_substrato.setter
    def asigna_substrato(self, valor):
        if isinstance(valor, str):
            self._substrato = valor
    
    def mostrar_substrato(self):
         print("El substrato es: ", self._substrato)
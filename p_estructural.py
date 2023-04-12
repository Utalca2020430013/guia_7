from proteina import proteina

class p_estructural(proteina):
    def __init__(self, nombre, descripcion, secuencia, tipo):
        super().__init__(nombre, descripcion, secuencia)
        self._tipo = tipo
    
    @property
    def asigna_tipo(self):
            return self._tipo        
    
    @asigna_tipo.setter
    def asigna_tipo(self, valor):
        if isinstance(valor, str):
            self._tipo = valor
        
    def mostrar_tipo(self):
        print("Tipo de proteina estructural: ", self._tipo)
    
    def mostrar_nombre(self):
        print("Nombre de proteina: ", self._nombre)
    
    def mostrar_secuencia(self):
        print("Secuencia Fasta de la proteina: ", self._secuencia)
    
    def mostrar_descripcion(self):
        print("Descripción:", self._descripcion)
        
class proteina:
    def __init__(self, nombre, descripcion, secuencia):
        self._nombre = nombre
        self._descripcion = descripcion
        self._secuencia = secuencia
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor 
    
    @property
    def secuencia(self):
        return self._secuencia
    
    @secuencia.setter
    def secuencia(self, valor):
        self._secuencia = valor  
    

       
        
    
    
    
    
    
    
        
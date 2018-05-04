from clase_profesores import Profesores
from clase_alumno import Alumno
from clase_buffet import Buffet

b=Profesores()
c=Alumno()
d=Buffet()

class clientes(object):
    persona=None

    def getDesc(self):
        return self.descuento_prof

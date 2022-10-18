class Octubre:

    def __init__(self, nombre,apellido,grupo):
        self.nombre = nombre
        self.apellido = apellido
        self.grupo = grupo


    def mostrar_datos(self):
        print(f'El alumno {self.nombre} {self.apellido}  {self.grupo} ')

asistencia1 = Octubre('David', 'Esteche', 'The JavaDabaDevs')
print(f'Asistencia de Octubre del alumno {asistencia1.nombre}, {asistencia1.apellido},del grupo {asistencia1.grupo}')
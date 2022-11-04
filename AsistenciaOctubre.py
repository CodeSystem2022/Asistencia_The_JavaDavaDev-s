# ASISTENCIA MES OCTUBRE
# THE JAVADABADEV'S

# Alumno: David Esteche
class Octubre:

    def __init__(self, nombre,apellido,grupo):
        self.nombre = nombre
        self.apellido = apellido
        self.grupo = grupo


    def mostrar_datos(self):
        print(f'El alumno {self.nombre} {self.apellido}  {self.grupo} ')

asistencia1 = Octubre('David', 'Esteche', 'The JavaDabaDevs')
print(f'Asistencia de Octubre del alumno {asistencia1.nombre}, {asistencia1.apellido},del grupo {asistencia1.grupo}')

#-----------------------------------------------------------
# Alumno: Gilda Carolina Mamani Condori
# Aritmetica:
class Operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    #Metodo Sumar
    def suma(self):
        return self.num1 + self.num2

    #Metodo Multuplicar
    def multiplica(self):
        return self.num1 * self.num2
print('Vamos a realizar una suma y mulriplicacion')
num1 = int(input('Digite un numero cualquiera: '))
num2 = int(input('Digite otro numero mas: '))
operacion = Operacion(num1, num2)

print(f'La suma de los dos numeros es: {operacion.suma()} \nLa multiplicacion de los dos numeros es: {operacion.multiplica()}')

#------------------------------------------------------

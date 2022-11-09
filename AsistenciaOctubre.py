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
print('Vamos a realizar una suma y multiplicacion')
num1 = int(input('Digite un numero cualquiera: '))
num2 = int(input('Digite otro numero mas: '))
operacion = Operacion(num1, num2)

print(f'La suma de los dos numeros es: {operacion.suma()} \nLa multiplicacion de los dos numeros es: {operacion.multiplica()}')

#------------------------------------------------------

# ASISTENCIA MES DE OCTUBRE
# THE JAVADABADEV'S

# Alumno: Marcelo Alejandro Boujón

class Aritmetica:
    
    #El nombre de este tipo de comentario es: DocString
    #esto es documentacion de la clase en python
    #Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas
    
    def __init__(self, operandoA, operandoB):
        self.operandoA= operandoA
        self.operandoB= operandoB

       	def sumar(self):
       	return  self.operandoA + self.operandoB

        def resta(self):
        return self.operandoA - self.operandoB

        def multiplicar(self):
        return self.operandoA * self.operandoB

        def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1= Aritmetica(7, 9)    #pasamos los argumentos para los operandos

print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'La resta de los números es: {aritmetica1.resta()}')
print(f'La multiplicación de los números es: {aritmetica1.multiplicar()}')
print(f'La división de los números es: {aritmetica1.dividir():.2f}')

-----------------------------------------------------------------------------------------

# ASISTENCIA OCTUBRE
# Alumna: Sofía Aguirre Zelay

# CLASS RECTANGULO:
# Debe tener 2 atributos: altura y base.
# Se calcula el área del rectangulo, con datos de base y altura ingresados por el usuario.

 class rectangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base
    def area(self):
        return self.base * self.altura

altura = int(input('Ingrese la altura del rectángulo: '))
base = int(input('Ingrese la base del rectángulo: '))
area = Rectangulo(altura, base)
print(f'El área del rectángulo es: {area1.area():.2f}')

----------------------------------------------------------------------------------------------

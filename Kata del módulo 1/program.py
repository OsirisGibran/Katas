# program.py

sum = 1 + 2
product = sum * 2

#Función print()
print(product)
print(sum)
print('Hola desde la consola')

#Función Type(), determina un dato asigando o una clase asignada de una variable.
print(type(sum))

#Operadores de asignación
# = contiene un valor
# += incrementa (suma)
# -= decrementa (resta)
# /= divide
# *= multiplica

#Importar bibliotecas para usar fechas
from datetime import date
date.today()
print(date.today())

#Conversión de tipos de datos
print("Today's date is: "+ str(date.today()))

#Recopilar información
#Entrada de usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre")
print("Saludos: " + name)

#Trabajar con números
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))
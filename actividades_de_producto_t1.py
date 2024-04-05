# -*- coding: utf-8 -*-
"""actividades-de-producto-t1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/danfernie96/86e22d70dc5bad519ff51aaef7e33d68/actividades-de-producto-t1.ipynb

TALLER 1 Actividades PRODUCTO / ejercicios algoritmicos
"""

""" 1. Compra de artículos, Si los artículos comprados son menores a 3 Pagar en efectivo,
caso contrario pagar con tarjeta."""

#1. entender--compra--condicion--
#2. herramientas--"IF", comparadores logicos
#3. analisis--que , para que ,porque
#4. prueba y evaluaciones

precio=int(input('ingrese un numero de precio del artículo'))

#precio=5
#precio=4

if precio<3:
  print ('paga en efectivo')

if precio >3:
  print('paga con tarjeta')

""" 2. Programa que permita leer 3 valores"""

num1 = 3  # int(input('ingrese un numero'))
num2 = 4  # int(input('ingrese un segundo numero'))
num3 = 60  # int(input('ingrese un tercer numero'))

if num1 != num2 and num1 != num3:
    if num2 != num1 and num2 != num3:
        if num3 != num1 and num3 != num2:
            if num1 > num2 and num1 > num3:
                print(f"el {num1} es el mayor")
            elif num2 > num1 and num2 > num3:
                print(f"el {num2} es el mayor")
            elif num3 > num1 and num3 > num2:
                print(f"el {num3} es el mayor")
else:
    print('ingrese numeros diferentes')

""" 3. Ingresar por teclado 3 números enteros
y mostrar el menor de los 3 números ingresados
y la suma de dichos números."""

num1=5   # int(input("ingrese el numero"))
num2=7   # int(input("ingrese el segundo numero"))
num3=2   # int(input("ingrese el tercer numero"))

# mostrar el menor de los tres
# mostrar la suma de los tres

if num1 < num2 and num1 < num3:
    print(f"El {num1} es el menor")
elif num2 < num1 and num2 < num3:
    print(f"El {num2} es el menor")
elif num3 < num1 and num3 < num2:
    print(f"El {num3} es el menor")

print(f" y la suma de los numeros es:{num1+num2+num3}")

""" 4. a un trabajador le pagan según sus horas trabajadas por una tarifa
de pago por hora. si la cantidad de horas trabajadas es mayor a 40 horas.
 la tarifa se incrementa en un 50% para las horas extras. calcular el
 salario del trabajador dadas las horas trabajadas y la tarifa"""

#1. que tengo ----#HORAS POR CANTIDAD DE TRABAJO-----condicion de tarifa para horas extras
#2. #que herramientas tengo ---IF---operador logicos---saber calcular porcentaje
#3. analisis que , porque , para que?
#4. evaluacion y resultados

horas_trabajador=50 #int(input('ingrese horas trabajadas'))
valor_hora=4        #int(input('ingrese sus horas'))
#formula general

if horas_trabajador<40:
  print(f"el salario del trabajador es:{horas_trabajador*valor_hora}")
elif horas_trabajador>=40:
  hora_extra=horas_trabajador-40
  horas_totales=valor_hora*horas_trabajador
  incremento=hora_extra*0.5*valor_hora
  resultado=horas_trabajador * valor_hora + incremento
  print(f" su salario + hora extra es {resultado} ")

""" 5. Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
Si se compran tres camisas o más se aplica un descuento del 20% sobre el total de la compra
y si son menos de tres camisas un descuento del 10%"""

# total a pagar por la compra de camisas.

NCC = float(input("ingrese número de camisas compradas:"))
TU = 20000
# Se aplica  20% des si se compran 3 camisas o más, y del 10% si se compran menos de 3 camisas

TD1 = (NCC * TU) - ((NCC * TU) * 0.10)
TD2 = (NCC * TU) - ((NCC * TU) * 0.20)
if NCC <3 :
    print (f"El valor de las camisas es: {TD1}")
else :
    print (f"El valor de las camisas es {TD2}")

"""6. A un trabajador le descuentan de su sueldo el 10%,
si su sueldo es menor o igual a 1000.
por encima de 1000 y hasta 2000 el 5% del adicional,
y por encima de 2000 el 3% del adicional.
calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo"""


# Paso 1: Obtener el sueldo del trabajador
sueldo = float(input("Ingrese el sueldo del trabajador: "))
# Paso 2: Calcular el descuento
if sueldo <= 1000:
    descuento = 0.10 * sueldo
elif sueldo <= 2000:
    adicional = sueldo - 1000
    descuento = 0.10 * 1000 + 0.05 * adicional
else:
    adicional = sueldo - 2000
    descuento = 0.10 * 1000 + 0.05 * 1000 + 0.03 * adicional
# Paso 3: Calcular el sueldo neto
sueldo_neto = sueldo - descuento
# Mostrar resultados
print(f"Descuento: {descuento}")
print(f"Sueldo Neto: {sueldo_neto}")

""" 7. Determinar si un alumno aprueba o reprueba un curso,
sabiendo que aprobara si:
su promedio de cinco calificaciones es mayor o igual a 5;
reprueba en caso contrario."""

# Entender: el problema nos pide determinar si un alumno aprueba o reprueba un curso
# Para aprobar, el promedio de las cinco calificaciones del alumno debe ser mayor o igual a 5
# Para reprobar, el promedio debe ser menor que 5"""

#calificaciones:
c1= 6
c2= 7
c3= 5
c4= 4
c5= 8

# promedio = suma de calificaiones / 5 (total de calificaiones)
# Comparar el promedio con 5:

# condicional: Si el promedio es mayor o igual a 5, el alumno aprueba.
# condicional: Si el promedio es menor que 5, el alumno reprueba

promedio= (c1+c2+c3+c4+c5)/5
print(promedio)
if promedio >= 5:
  print(f"el alumno aprueba")

if promedio < 5:
  print(f"el alumno reprueba")

# Comparamos el promedio con 5 para determinar si el alumno aprueba o reprueba

""" 8.- Una distribuidora de motocicletas tiene una promoción
de fin de año que consiste en lo siguiente. Las motos marca Honda
tienen un descuento del 5%, las marcas Yamaha del 8% y las Suzuki
del 10%, las otras marcas 2%. Se debe mostrar el precio de la moto,
el descuento y el precio a pagar."""

#que tenemos?
#2. herramientas
#3. analisis
#4. evaluacion y resultados

# descuentos:

#honda: 5%
#yamaha 8%
#susuki 10%
#otras 2%

#mostras 3 cosas:

#precio de la moto
#descuento
#precio a pagar

#porcentaje
#234*0.1

#moto='hp'
#valor_moto= 300

moto= input("ingrese la marca de la moto")
valor_moto= int(input("ingrese el valor de la moto"))

if moto=='yamaha':
  resultado = valor_moto*0.08

  print(f" su descuento  es {resultado}  ")

elif moto=='honda':
  resultado = valor_moto*0.05

  print(f" su descuento  es {resultado}  ")

elif moto=='susuki':
  resultado = valor_moto*0.1

  print(f" su descuento  es {resultado}  ")

else:
  resultado = valor_moto*0.02
  print(f" su descuento es {resultado} ")

""" 9.- Pedir un valor numérico e indicar si es par o no es par"""

# Pedir al usuario que ingrese un valor numérico
numero = int(input("Ingresa un valor numérico: "))

# Verificar si el número es par o no
if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "no es par.")

"""10.- Un cliente va a comprar una moto y se percata que si lo compraba
el martes tiene un descuento del 12%, luego si lo compra el sábado tiene
un descuento del 18% y si es feriado un 25%, mostrar cuanto pagara en cada opción."""

# Precio base de la moto
precio_moto = 1000

# Descuento por comprar el martes (12%)
descuento_martes = 0.12
precio_martes = precio_moto - (precio_moto * descuento_martes)

# Descuento por comprar el sábado (18%)
descuento_sabado = 0.18
precio_sabado = precio_moto - (precio_moto * descuento_sabado)

# Descuento por comprar en feriado (25%)
descuento_feriado = 0.25
precio_feriado = precio_moto - (precio_moto * descuento_feriado)

# Mostrar los precios con descuento
print("Si compra la moto el martes, pagará:", precio_martes)
print("Si compra la moto el sábado, pagará:", precio_sabado)
print("Si compra la moto en feriado, pagará:", precio_feriado)


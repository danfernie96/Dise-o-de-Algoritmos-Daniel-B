# -*- coding: utf-8 -*-
"""Actividades de conocimiento.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hTf1uOqRdNx3_xzTcsfixsLVbm0FBCR3

Actividades de conocimiento / Estructuras de repetición
"""

""" 1. Elaborar un algoritmo y su debido proceso de prueba de escritorio que permita obtener
la factorial de un número """

factorial = 1  # esta es la factorial
for i in range(2,8):
 factorial *= i
print(f" la factorial del numero 7 es", factorial)



# 2

cant_personas = 10
contador_0_20 = 0
contador_20_30 = 0
contador_30_40 = 0
contador_40_60 = 0
contador_mas_60 = 0

for cont in range(cant_personas):
    print ("Ingrese la edad #" ,(cont+1))
    edad = int(input())
    if edad <= 20:
        contador_0_20 += 1
    elif edad <= 30:
        contador_20_30 += 1
    elif edad >30:
        contador_30_40 += 1
    elif edad >= 40:
        contador_40_60 += 1
    elif edad >= 60:
        contador_mas_60 += 1
    else:
        print("Error, ingrese una edad entre 0 y 60")
    print("Total de personas entre 0 y 20:", contador_0_20,"Total de personas entre 30 y 40:", contador_20_30,"  Total de personas entre 40 y 60:", contador_40_60, " Total de personas mayores de 60:", contador_mas_60)

#3

numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

for i in range(1, 101):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 4

productos = [10,20,25,30,35, 40,50,75,80,100]
sum_prod_sin_iva = 0
sum_prod_con_iva = 0


for producto in productos:
        sum_prod_sin_iva = sum_prod_sin_iva+ producto
        sum_prod_con_iva = sum_prod_sin_iva + 0.19* sum_prod_sin_iva
print (f"El costo total de los productos sin iva es: {sum_prod_sin_iva}")
print (f"El costo total de los productos con iva es: {sum_prod_con_iva}")


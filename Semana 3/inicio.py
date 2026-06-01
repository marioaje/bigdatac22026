print("Saludos clase")#Mostrar mensajes en la consola

# /() Sirven para pasar parametros
# Aca yo puedo escribir mensajes de guia o cosas importantes

#Las variables
textoNombre = "Profe Mario" #Texto
edad = 40 # Numero entero
numeros = 9.17 #Decimal
valores = True #boolean

print(textoNombre)
print(edad)
print(numeros)
print(valores)
#todo lo que esta antes de unos parentesis se les conoce como funciones
# soyUnaVariable = input("Ingrese su nombre")
# # la coma , sirve para pasar varios parametros
# print("Saludo usuario: ", soyUnaVariable)


# a = int( input("Ingrese su numero A:") )

# b = int( input("Ingrese su numero B:") )


# resultadoSuma = a + b

# print("El resultao de la suma es:" , resultadoSuma)

# c = float( input("Ingrese su numero c:") )

# d = float( input("Ingrese su numero d:") )
# sumaCondecimales = c + d


# a = int( input("Ingrese su numero A:") )
# b = int( input("Ingrese su numero B:") )

# numeroA = a
# numeroB = b

#bb
#Condicionales realizan pruebas con base a lo que le indiquemos

# if numeroA == numeroB:
#     print('Los numeros son iguales')
# elif numeroA > numeroB:
#     print("El numero ", numeroA, " es el mayor")
# else:
#     print("El numero ", numeroB, " es el mayor")



#Ciclos
print("while")
contador = 1
#Mientras cumpla con la condicion ingrese y haga sus operaciones
while contador < 10:
    print(contador)
    contador = contador + 1
    #contador +=1 

print("for")
for iContador in range(4,12):
    print(iContador)

# # 1 
# num1= int(input("ingrese un numero (0 para salir) "))
# while num1 != 0:
#     num1= int(input("ingrese un numero (0 para salir) "))
#     num2= int(input("ingrese un numero "))
#     suma = num1 + num2
#     print(f"resultado {suma}")

# # 2 
# password = input("ingrese contraseña ")
# while password != "python123":
#     print("contraseña incorrecta")
#     password = input("vuelve a intentarlo ")

# # 3
# productos = []
# add = input("ingrese el producto que quiere agregar a la lista ('salir' para cerrar) ").lower()
# while add != "salir":
#     productos.append(add)
#     add = input("ingrese el producto que quiere agregar a la lista ('salir' para cerrar) ").lower()
#     print(f"la lista es esta {productos}")

# # 4
# numero = int(input("ingresa numero "))
# attempts= 2
# par = 0
# impar = 0
# while attempts <= 10:
#     attempts += 1
#     numero = int(input("ingresa numero "))
#     if (numero // 2) * 2 == numero:
#         par += 1
#     else:
#         impar += 1
# print(f"el numero total de numeros pares {par} y el numero de impares es {impar}")

# # 5
# notas = []
# entrada = input("ingresa nota 0 - 5 ('salir' para cerrar) ")
# while entrada != "salir":
#     entrada = float
#     entrada= input("ingresa nota 0 - 5 ('salir' para cerrar) ")
#     notas.append(entrada)
#     promedio = sum(notas) / len(notas)
    
# print(f"el promedio de las notas es {promedio}")
# pendiente

## 6
# tabla = int(input("ingresa numero del cual quieres conocer su tabla de multiplicar (0 para salir) "))
# while tabla != 0:
#     tablaMulti = [tabla * 2,
#                   tabla * 3,
#                   tabla * 4,
#                   tabla * 5,
#                   tabla * 6,
#                   tabla * 7,
#                   tabla * 8,
#                   tabla * 9,
#                   tabla * 10
#                   ]
#     print(f"""la tabla de multiplicar de {tabla} es:
#           x2 {tablaMulti[0]}
#           x3 {tablaMulti[1]}
#           x4 {tablaMulti[2]}
#           x5 {tablaMulti[3]}
#           x6 {tablaMulti[4]}
#           x7 {tablaMulti[5]}
#           x8 {tablaMulti[6]}
#           x9 {tablaMulti[7]}
#           x10 {tablaMulti[8]} """)
#     tabla = int(input("ingresa numero del cual quieres conocer su tabla de multiplicar (0 para salir) "))

# # 7
# import random
# eleccion= range(200)
# secretNum= random.choice(eleccion)
# guess = int(input("intenta adivinar el numero secreto "))
# while guess != secretNum:
#     print("ese no es pero te dare una pista")
#     if guess < secretNum:
#         print("el numero secreto es mayor")
#     elif (secretNum + 100) < guess:
#         print("estas bastantes lejos, es menor")
#     elif guess > secretNum:
#         print("el numero secreto es menor")
#     guess= int(input("vuelve a intentarlo "))
# print("¡lo adivinaste!")

# # 8 
# frutas = ["guanabana","chontaduro","tomate","fresa","banano"]
# guess1= input("intenta adivinar la fruta ")
# while True:
#     print("vuelve a intentarlo")
#     guess1= input("+ ")
#     if guess1 in frutas:
#         print("adivinaste")
#         break


# # 9
# english = {
#     "mientras": "while",
#     "hola": "hello",
#     "cafe": "coffe",
#     "amarillo": "yellow",
#     "rojo": "red"
# }
# while True:
#     spanish = input("que palabra quieres traducir? (solo hay 5 traducidas) ").lower()
#     if spanish in english:
#         traductor= english[spanish]
#         print(f"la palabra {spanish} en ingles es: {traductor}")
#     spanish = input("quieres intentas con otra palabra? ('salir'para cerrar) ").lower()
#     if spanish == "salir":
#         break
#     elif spanish == "close":
#         break

# # 10
# print("""el programa requiere que se ingrese el tipo de operacion a realizar
#       suma
#       resta 
#       multiplicacion
#       division 
#       'salir' para cerrar el programa""")
# opera= input("elige el tipo de operacion que quieres hacer ").lower()
# while opera != "salir":
#     if opera == "suma":
#         numero1= int(input("ingrese primer numero a sumar "))
#         numero2= int(input("ingrese segundo numero a sumar "))
#         result = numero1 + numero2
#     elif opera == "resta":
#         numero1= int(input("ingrese primer numero a restar "))
#         numero2= int(input("ingrese segundo numero a restar "))
#         result = numero1 - numero2
#     elif opera == "multiplicacion":
#         numero1= int(input("ingrese primer numero a multiplicar "))
#         numero2= int(input("ingrese segundo numero a multiplicar "))
#         result = numero1 * numero2
#     elif opera == "division":
#         numero1= int(input("ingrese primer numero a dividir "))
#         numero2= int(input("ingrese segundo numero a dividir "))
#         result = numero1 / numero2
#     else:
#         print("caracter invalido")
#     print(f"resultado: {result}")
#     opera= input("elige el tipo de operacion que quieres hacer ").lower()

# # 11
# nombres = []
# added = input("ingrese el nombre que quiere agregar a la lista ('salir' para cerrar) ").lower()
# while added != "salir":
#     added = input("ingrese el nombre que quiere agregar a la lista ('salir' para cerrar) ").lower()
#     nombres.append(added)
#     print(f"la lista es esta {nombres}")
        
# # 12 
# colores = ["amarillo","verde","violeta","negro"]
# guess2 = input("intenta adivinar el color ")
# while True:
#     if guess2 in colores:
#         print("adivinaste")
#         break
#     print("vuelve a intentarlo")
#     guess2= input("+ ")

# # 13 
# base = int(input("ingrese numero a potenciar "))
# while True:
#     print(f"las potencias de {base} desde el 1 al 5 son: ")
#     potencia = [base ** 1,
#                 base ** 2,
#                 base ** 3,
#                 base ** 4,
#                 base ** 5
#                 ]
#     print(f""" potencia 1: {potencia[0]},
#           potencia 2 : {potencia[1]},
#           potencia 3 : {potencia[2]},
#           potencia 4 : {potencia[3]},
#           potencia 5 : {potencia[4]}""")
#     base = int(input("que otro numero quieres potenciar? "))

# # 14 
# cuadrados = []
# numPoten = []
# intentos = 1
# while intentos <= 5:
#     intentos += 1
#     numeroPot = int(input(f"ingresa numero del cual quieres conocer su cuadrado "))
#     numPoten.append(numeroPot)
#     cuadrados.append(numeroPot)
# total = [cuadrados[0]**2,cuadrados[1]**2,cuadrados[2]**2,cuadrados[3]**2,cuadrados[4]**2]    
# print(f"""
#       el cuadrado de {numPoten[0]} es {total[0]},
#       el cuadrado de {numPoten[1]} es {total[1]},
#       el cuadrado de {numPoten[2]} es {total[2]},
#       el cuadrado de {numPoten[3]} es {total[3]},
#       el cuadrado de {numPoten[4]} es {total[4]} """)

# 15 
info= {}
estudiante = input("ingrese nombre del estudiante ").lower()
notaFinal = input(f"ingrese la nota final del estudiante {estudiante} ")
while True:
    if estudiante or notaFinal == "fin":
        break 
    notaFinal= float
    info[estudiante] = notaFinal
    estudiante = input("ingrese nombre del estudiante ").lower()
    notaFinal = input(f"ingrese la nota final del estudiante {estudiante} ")
    
print(f"la informacion registrada fue : {info}")
    
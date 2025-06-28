# # 1
# num1= int(input("ingrese un numero (0 para salir) "))
# while num1 != 0:
#     num1= int(input("ingrese un numero (0 para salir) "))
#     num2= int(input("ingrese un numero (0 para salir) "))
#     sum = num1 + num2
#     print(f"resultado {sum}")

# # 2 
# contraseña= input("ingrese contraseña ")
# while contraseña != "python123":
#     print("contraseña incorrecta")
#     contraseña= input("vuelve a intentarlo ")

# # 3
# productos = []
# while add != "salir":
#     add = input("ingrese el producto que quiere agregar a la lista ('salir' para cerrar) ").lower()
#     productos.append(add)
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
#pendiente

# 6
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

# 7
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

# 8 
# frutas = ["guanabana","chontaduro","tomate","fresa","banano"]
# guess1= input("intenta adivinar la fruta ")
# while True:
#     print("vuelve a intentarlo")
#     guess1= input("+ ")
#     if guess1 in frutas:
#         print("adivinaste")

# 9
# english = {
#     "mientras": "while",
#     "hola": "hello",
#     "cafe": "coffe",
#     "amarillo": "yellow",
#     "rojo": "red"
# }
# while True:
#     if spanish in english:
#         spanish = input("que palabra quieres traducir? (solo hay 5 traducidas) ").lower()
#         traductor= english[spanish]
#         print(f"la palabra {spanish} en ingles es: {traductor}")
#     spanish = input("quieres intentas con otra palabra? ('salir'para cerrar) ").lower()
#     if spanish == "salir":
#         break
#     elif spanish == "close":
#         break
    
# 10
             
    
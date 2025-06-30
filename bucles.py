# 1
print("ejercicio 1")
num1= int(input("ingrese un numero (0 para salir) "))       # entrada de datos
while num1 != 0:                                            # bucle
    num1= int(input("ingrese un numero (0 para salir) "))   # varible numerica 1
    num2= int(input("ingrese un numero "))                  # variable numerica 2
    suma = num1 + num2                                      # suma
    print(f"resultado {suma}")

# 2
print("ejercicio 2")                                        # contraseña = "python123"
password = input("ingrese contraseña ")                     # entrada de datos
while password != "python123":                              # bucle 'mientras'
    print("contraseña incorrecta")                          # resultado si password != "python123"
    password = input("vuelve a intentarlo ")               

# 3
print("ejercicio 3")
productos = []                                                                                      # lista de productos
add = input("ingrese el producto que quiere agregar a la lista ('salir' para cerrar) ").lower()     # entrada de datos
while add != "salir":                                                                               # bucle 'mientras'
    productos.append(add)                                                                           # agrega datos a la lista
    add = input("ingrese el producto que quiere agregar ('salir' para cerrar) ").lower()            # entrada de datos 2
    print(f"la lista es esta {productos}")                                                        

# 4
print("ejercicio 4")
numero = int(input("ingresa numero "))
ATTEMPTS = 2
PAR = 0
IMPAR = 0
while ATTEMPTS <= 10:
    ATTEMPTS += 1
    numero = int(input("ingresa numero "))
    if (numero // 2) * 2 == numero:
        PAR += 1
    elif (numero // 2) * 2 != numero:
        IMPAR += 1
print(f"el numero total de numeros pares {PAR} y el numero de impares es {IMPAR}")

# 5
print("ejercicio 5 ")
notas = []
while True:
    control = input("bienvenido (escribe 'salir' para cerrar) ")
    if control == "salir":
        break
    try:
        entrada = float(input("ingresa nota (0 - 5) "))
        entrada = float(input("ingresa nota (0 - 5) "))
        notas.append(entrada)
        sumatoria = sum(notas)
        CANTI = len(notas)
        promedio = sumatoria / CANTI
    except ValueError:
        print("caracter invalido")
print(f"el promedio de las notas es {promedio}")

# 6
tabla = int(input("ingresa numero (0 para salir) "))
while tabla != 0:
    tablaMulti = [tabla * 2,
                  tabla * 3,
                  tabla * 4,
                  tabla * 5,
                  tabla * 6,
                  tabla * 7,
                  tabla * 8,
                  tabla * 9,
                  tabla * 10
                  ]
    print(f"""la tabla de multiplicar de {tabla} es:
          x2 {tablaMulti[0]}
          x3 {tablaMulti[1]}
          x4 {tablaMulti[2]}
          x5 {tablaMulti[3]}
          x6 {tablaMulti[4]}
          x7 {tablaMulti[5]}
          x8 {tablaMulti[6]}
          x9 {tablaMulti[7]}
          x10 {tablaMulti[8]} """)
    tabla = int(input("ingresa numero (0 para salir) "))

# 7
import random
eleccion= range(200)
secretNum= random.choice(eleccion)
guess = int(input("intenta adivinar el numero secreto "))
while guess != secretNum:
    print("ese no es pero te dare una pista")
    if guess < secretNum:
        print("el numero secreto es mayor")
    elif (secretNum + 100) < guess:
        print("estas bastantes lejos, es menor")
    elif guess > secretNum:
        print("el numero secreto es menor")
    guess= int(input("vuelve a intentarlo "))
print("¡lo adivinaste!")

# 8
frutas = ["guanabana","chontaduro","tomate","fresa","banano"]
guess1= input("intenta adivinar la fruta ")
while True:
    print("vuelve a intentarlo")
    guess1= input("+ ")
    if guess1 in frutas:
        print("adivinaste")
        break


# 9
english = {
    "mientras": "while",
    "hola": "hello",
    "cafe": "coffe",
    "amarillo": "yellow",
    "rojo": "red"
}
while True:
    spanish = input("que palabra quieres traducir? (solo hay 5 traducidas) ").lower()
    if spanish in english:
        traductor= english[spanish]
        print(f"la palabra {spanish} en ingles es: {traductor}")
    if spanish == "salir":
        break
    elif spanish == "close":
        break

# 10
print("""el programa requiere que se ingrese el tipo de operacion a realizar
      suma
      resta
      multiplicacion
      division
      'salir' para cerrar el programa""")
opera= input("elige el tipo de operacion que quieres hacer ").lower()
while opera != "salir":
    try:
        if opera == "suma":
            numero1= int(input("ingrese primer numero a sumar "))
            numero2= int(input("ingrese segundo numero a sumar "))
            result = numero1 + numero2
            print(f"resultado: {result}")
        elif opera == "resta":
            numero1= int(input("ingrese primer numero a restar "))
            numero2= int(input("ingrese segundo numero a restar "))
            result = numero1 - numero2
            print(f"resultado: {result}")
        elif opera == "multiplicacion":
            numero1= int(input("ingrese primer numero a multiplicar "))
            numero2= int(input("ingrese segundo numero a multiplicar "))
            result = numero1 * numero2
            print(f"resultado: {result}")
        elif opera == "division":
            numero1= int(input("ingrese primer numero a dividir "))
            numero2= int(input("ingrese segundo numero a dividir "))
            result = numero1 / numero2
            print(f"resultado: {result}")
        else:
            print("caracter invalido")
    except ValueError:
        print("caracter invalido")
    opera= input("elige el tipo de operacion que quieres hacer ").lower()

# 11
nombres = []
added = input("ingrese el nombre que quiere agregar ('salir' para cerrar) ").lower()
while added != "salir":
    added = input("ingrese el nombre que quiere agregar ('salir' para cerrar) ").lower()
    nombres.append(added)
    print(f"la lista es esta {nombres}")

# 12
colores = ["amarillo","verde","violeta","negro"]
guess2 = input("intenta adivinar el color ")
while True:
    if guess2 in colores:
        print("adivinaste")
        break
    print("vuelve a intentarlo")
    guess2= input("+ ")

# 13
base = int(input("ingrese numero a potenciar "))
while True:
    print(f"las potencias de {base} desde el 1 al 5 son: ")
    potencia = [base ** 1,
                base ** 2,
                base ** 3,
                base ** 4,
                base ** 5
                ]
    print(f""" potencia 1: {potencia[0]},
          potencia 2 : {potencia[1]},
          potencia 3 : {potencia[2]},
          potencia 4 : {potencia[3]},
          potencia 5 : {potencia[4]}""")
    base = int(input("que otro numero quieres potenciar? "))

# 14
cuadrados = []
numPoten = []
INTENTOS = 1
while INTENTOS <= 5:
    INTENTOS += 1
    numeroPot = int(input("ingresa numero "))
    numPoten.append(numeroPot)
    cuadrados.append(numeroPot)
total = [cuadrados[0]**2,cuadrados[1]**2,cuadrados[2]**2,cuadrados[3]**2,cuadrados[4]**2]
print(f"""
      el cuadrado de {numPoten[0]} es {total[0]},
      el cuadrado de {numPoten[1]} es {total[1]},
      el cuadrado de {numPoten[2]} es {total[2]},
      el cuadrado de {numPoten[3]} es {total[3]},
      el cuadrado de {numPoten[4]} es {total[4]} """)

# 15
info= {}
estudiante = input("ingrese nombre del estudiante ").lower()
GRADE= input(f"ingrese la nota final del estudiante {estudiante} ")
while True:
    info[estudiante] = GRADE
    if estudiante == "salir":
        break
    elif GRADE == "salir":
        break
    GRADE= float(GRADE)
    print(f"la informacion registrada fue : {info}")
    estudiante = input("ingrese nombre del estudiante ").lower()
    GRADE= input(f"ingrese la nota final del estudiante {estudiante} ")

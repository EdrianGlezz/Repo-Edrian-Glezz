# edad= input("escribe tu edad")
# print(f"Tipo de dato sin convertir{type(edad)}")
# edad= int(edad)
# print(f"tipo de dato ya convertido {type(edad)}")

# nombre= input("escribe tu nombre: ")
# edad=input("escribe tu edad: ")
# print(f"tu nombre es '{nombre}' y tu edad es '{edad}'")


# == falso0 y verdadero 1
# print(5==5)
# print("9"=="9")

#!=
# print(2!=4)
# print(2!=2)
# print(False!=True)

# nombre=input("escribe tu nombre: ")
# print(f"Hola compita {nombre}")

# horas_de_trabajo=int(input("cuantas horas trabajas al dia? "))
# tarifa_de_horas=float(input("Cuanto te pagan por hora? "))
# salario = horas_de_trabajo*tarifa_de_horas
# print(f"Tu salario total por las {horas_de_trabajo} horas de trabajo son {salario} MXN")

# temperatura= float(input("escribe la temperatura actual: "))
# formula= (temperatura * 9/5)+32
# print(f"La temperatura actual en fahrenheit es de: {formula}")

mayorria_edad= 18
edad= int(input("escribe la edad de la persona: "))

if edad > mayorria_edad:
    print("la persona es mayor de edad")
elif edad == mayorria_edad:
    print("la persona tiene exactamente 18 años")
elif edad < mayorria_edad:
    print("la persona no es mayor de edad")
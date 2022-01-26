"""print you are underage if the input is less than 18"""

age = int(input("¿Cuantos años tienes?: "))
if age < 18:
    print("eres menor de edad")
elif age < 21:
    print("ya puedes votar")
else:
    print("Eres mayor de edad")
        
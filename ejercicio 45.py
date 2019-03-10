## 45
print("Este programa le ayudará a saber el dia de acuerdo con el número que digite. Recuerde que los números son de 1 a 7")
num=int(input("Por favor digite un número"))
if num == 1:
    print("El numero ingresado fue", num, "y corresponde al dia lunes")
elif num == 2:
    print("El numero ingresado fue", num, "y corresponde al dia martes")
elif num == 3:
    print("El numero ingresado fue", num, "y corresponde al dia miercoles")
elif num == 4:
    print("El numero ingresado fue", num, "y corresponde al dia jueves")
elif num == 5:
    print("El numero ingresado fue", num, "y corresponde al dia viernes")
elif num == 6:
    print("El numero ingresado fue", num, "y corresponde al dia sábado")
elif num == 7:
    print("El numero ingresado fue", num, "y corresponde al dia domingo")
else:
    print("Número incorrecto. Por favor ingrese un numero entre 1 y 7")
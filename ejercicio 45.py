## 45
print("Este programa le ayudar� a saber el dia de acuerdo con el n�mero que digite. Recuerde que los n�meros son de 1 a 7")
num=int(input("Por favor digite un n�mero"))
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
    print("El numero ingresado fue", num, "y corresponde al dia s�bado")
elif num == 7:
    print("El numero ingresado fue", num, "y corresponde al dia domingo")
else:
    print("N�mero incorrecto. Por favor ingrese un numero entre 1 y 7")
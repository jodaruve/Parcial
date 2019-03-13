## 28
print("Este programa calculara si el numero ingresado es positivo o negativo")
num=float(input("Por favor ingrese un numero "))
if num == 0:
	print("El numero", num, "no es ni negativo ni positivo")
elif num > 0:
	print("El numero", num, "es positivo")
else:
	print("El numero", num, "es negativo")
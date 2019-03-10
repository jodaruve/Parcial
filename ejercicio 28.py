## 28
num=float(input("Por favor ingrese un numero para saber si es positivo o negativo"))
if num == 0:
	print("El numero", num, "no es ni negativo ni positivo")
elif num > 0:
	print("El numero", num, "es positivo")
else:
	print("El numero", num, "es negativo")
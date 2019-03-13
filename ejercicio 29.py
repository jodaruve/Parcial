## 29
print("Este programa calculara si el numero ingresado es par-positivo, par-negativo, impar-positivo o impar-negativo")
num=float(input("Por favor ingrese un numero "))
if num > 1:
	if num % 2 == 0:
		print("El numero", num, "es par positivo")
	else:
		print("El numero", num, "es impar positivo")
elif num % 2 == 0:
	print("El numero", num, "es par negativo")
else:
	print("El numero", num, "es impar negativo") 

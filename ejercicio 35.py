## 35
print("Este programa le ayudar� a calcular el mayor y menor de tres n�meros")
n1=int(input("Por favor ingrese un n�mero "))
n2=int(input("Por favor ingrese un n�mero "))
n3=int(input("Por favor ingrese un n�mero "))
if n1==n2 and n2==n3:
	print("Los n�meros son iguales")
else:
	if n1>n2 and n2>n3:
			print(n1, "es el n�mero mayor y", n3, "es el numero menor")
	elif n2>n3 and n3>n1:
			print(n2, "es el n�mero mayor y", n1, "es el numero menor")
	else:
			print(n3, "es el n�mero mayor y", n2, "es el numero menor")
		
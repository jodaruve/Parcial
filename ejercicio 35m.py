## 35
print("Este programa calculara el mayor y menor de tres números")
n1=int(input("Por favor ingrese un número "))
n2=int(input("Por favor ingrese un número "))
n3=int(input("Por favor ingrese un número "))
if n1==n2 and n2==n3:
	print("Los números son iguales")
else:
	if n1>n2 and n1>n3 and n2>n3:
			print(n1, "es el número mayor", n3, "menor")
	elif n2>n3 and n2>n1 and n3>n1:
			print(n2, "es el número mayor y", n1, "es el numero menor")
	elif n3>n1 and n3>n2 and n1>n2:
			print(n3, "es el número mayor y", n2, "es el numero menor")
		
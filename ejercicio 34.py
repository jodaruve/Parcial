## 34
print("Este programa le ayudara a calcular el numero mayor")
n1=int(input("Por favor ingrese eun numero "))
n2=int(input("Por favor ingrese un numero "))
n3=int(input("Por favor ingrese un numero "))
if n1==n2 and n2==n3:
	print("Los numeros son iguales")
else:
	if n1>n2:
		if n1>n3:
			print(n1, "es el numero mayor")
		else:
			print(n3, "es el numero mayor")
	else:
		if n2>n3:
			print(n2, "es el numero mayor")
		else:
			print(n3, "es el numero mayor")

## 33
print("Este programa mostrara el mayor de los numeros ingresados")
n1=int(input("Por favor ingrese un numero "))
n2=int(input("Por favor ingrese otro numero "))
if n1 == n2:
	print("Los numeros son iguales")
elif n1 > n2:
	print(n1, "es mayor que", n2)
else:
	print(n2, "es mayor que", n1)
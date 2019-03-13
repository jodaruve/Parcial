## 36
print("Este programa calculara si la suma del primer y segundo numero ingresado es mayor o menor que el tercero")
n1=int(input("Por favor ingrese el primer numero "))
n2=int(input("Por favor ingrese el segundo numero "))
n3=int(input("Por favor ingrese el tercer numero "))
suma=n1+n2
if suma>n3:
	print("La suma de los numeros", n1, "y", n2, "es:", suma, "Por lo tanto es mayor que", n3)
else:
	print("La suma de los numeros", n1, "y", n2, "es:", suma, "Por lo tanto es menor que", n3)
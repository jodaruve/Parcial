## 31
print("Este pograma leera un número y si este es mayor o igual a 10 devolvera el triple de este de lo contrario la cuarta parte de este.")
num=float(input("Por favor ingrese un numero "))
n_mayor=num*3
n_menor=num/4
if num >= 10:
	print("El triple del numero", num, "es:", n_mayor)
else:
	print("la cuarta parte del numero", num, "es:", n_menor)

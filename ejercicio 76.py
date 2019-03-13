## 76
print("Este programa mostrara la cantidad de numeros entre los cuales se puede dividir el numero ingresado")
c=0
num=int(input("Por favor ingrese el numero "))
for n in range(1,num+1):
	if num%n==0:
		c=c+1
print("El numero ingresado se puede dividir en", c, "numeros diferentes")
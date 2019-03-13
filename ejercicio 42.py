## 42
print("Este programa mostrara la cantidad de digitos que tiene el numero ingresado")
num=int(input("Por favor ingrese un numero "))
c=0
while num>0 and num<100000:
	num=int(num/10)
	c=c+1
	
print("El numero", num, "tiene", c, "digitos")
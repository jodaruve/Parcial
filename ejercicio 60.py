## 60
print("Este programa seguir� la siguiente secuencia(1 -2 3 -4 5 -6...) hasta el n�mero que desee")
cant=int(input("Por favor ingrese el numero "))
for num in range(1,cant+1):
	if num%2==0:
		num=num*-1
	print(num)

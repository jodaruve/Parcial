## 38
print("Este programa le mostrara si el agno ingresado es biciesto o no")
agno=int(input("Por favor ingrese el agno "))
if agno%4==0:
	if agno%100==0:
		if agno%400==0:
			print("El año", agno, "es bisiesto")
		else:
			print("El año", agno, "no es bisiesto")
	else:
		print("El año", agno, "es bisiesto")
else:
	print("El año", agno, "no es bisiesto")	

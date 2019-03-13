## 32
print("El siguiente programa calculara el promedio de las notas. Por favor ingrese cada una de las notas sin puntos ni comas. Gracias")
n1=int(input("Por favor ingrese la primera nota "))
n2=int(input("Por favor ingrese la segunda nota "))
n3=int(input("Por favor ingrese la tercera nota "))
n4=int(input("Por favor ingrese la cuarta nota "))
n5=int(input("Por favor ingrese la quinta nota "))
v_n1=n1*0.15
v_n2=n2*0.20
v_n3=n3*0.15
v_n4=n4*0.30
v_n5=n5*0.20
prom=v_n1+v_n2+v_n3+v_n4+v_n5
if prom < 20:
	print("Ha reprobado con una nota de", prom, ", sin posibilidad de habilitar")
elif prom < 30:
	print("Ha reprobado con una nota de", prom, ", con posibilidad de habilitar")
elif prom < 45:
	print("Ha aprobado con una nota de:", prom)
else:
	print("Ha aprobado con una nota de", prom, ", Felicitaciones!!!!!")
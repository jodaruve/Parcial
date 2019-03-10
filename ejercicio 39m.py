## 39
print ("x=-b+-(b**2-4*a*c)**(1/2)/2*a")
	a=float(input("Por favor ingrese el valor para reemplazar 'a' "))
	b=float(input("Por favor ingrese el valor para reemplazar 'b' "))
	c=float(input("Por favor ingrese el valor para reemplazar 'c' "))
	d=(((b**2)-(4*a*c))**(1/2))
	x1=(((-1*b)-(d**(1/2))/2*a))
	x2=(((-1*b)+(d**(1/2))/2*a))
	if d>0:
		print("la seccion negativa es: ", x1, "la parte positiva es: ", x2)
	else: 
	    if d==0:
	        print("el valor:", x1, "es igual a:", x2)
	    else:
		    if d<0:
		        print("este problema no tiene solucion en los numeros reales")

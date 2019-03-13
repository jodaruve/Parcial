## 30
print("Este algoritmo incrementara un 19% al valor ingresado pero si es mayor a 150000 le hara un descuento de 5%")
valor=float(input("Por favor ingrese el costo del producto"))
iva=valor*0.19
n_valor1=valor+iva
desc=n_valor1*0.05
n_valor2=n_valor1-desc
if n_valor1 > 150000:
	print("El costo del producto es igual a:", n_valor2)
else:
	print("El costo del producto es:", n_valor1)

## 30
valor=float(input("Por favor ingrese el costo del producto"))
iva=valor*0.19
n_valor1=valor+iva
desc=iva*0.05
n_valor2=n_valor1-desc
if n_valor1 > 150000:
	print("El costo del producto es igual a:", n_valor2)
else:
	print("El costo del producto es:", n_valor1)

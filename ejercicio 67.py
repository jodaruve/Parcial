## 67
print("Este programa le mostrara la cantidad de numeros mayores y menores a 100 ingresados. recuerde que cuando no desee ingresar mas numeros debe escribir -00")
mayores=0
menores=0
num=float(input("Por favor ingrese un numero "))
while num!=-00:
  if num>100:
    mayores=mayores+1
  else:
    menores=menores+1
  num=float(input("Por favor ingrese un numero "))
print("La cantidad de numeros mayoes a 100 es:", mayores)
print("La cantidad de numeroos menores a 100 es:", menores)
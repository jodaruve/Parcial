## 62
sum=0
print("Este programa mostrara los números naturales en el rango que usted desee")
n=int(input("Por favor ingrese desde donde desea que empiece el conteo "))
m=int(input("Por favor ingrese hasta donde desea que llegue el conteo "))
if m<n:
  print("Por favor asegúrese que el primer número ingresado sea menor que el segundo")
else:
  for i in range(n,m+1):
    sum=sum+i
print("la suma de los numeros naturales contenidos entre", n, "y", m, "es", sum)

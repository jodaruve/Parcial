## 61
print("Este programa mostrara los números naturales en el rango que usted desee")
n=int(input("Por favor ingrese desde donde desea que empiece el conteo "))
m=int(input("Por favor ingrese hasta donde desea que llegue el conteo "))
if n<m:
  print("Por favor asegúrese que el primer número ingresado sea menor que el segundo")
for i in range(n,m+1):
  print(i)

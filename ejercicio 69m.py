## 69
print("Este programa solo leerá números positivos hasta que complete 100 números pares o 80 números 5")
pares=0
cincos=0
nros=0
num=float(input("Por favor ingrese un numero "))
if num<0:
  print("Por favor ingrese un numero positivo")
else:
  while pares<100:
    nros=nros+1
    if num%2==0:
      pares=pares+1
  num=float(input("Por favor ingrese un numero "))
  
  while cincos<80:
    if num==5:
      cincos=cincos+1
  num=float(input("Por favor ingrese un numero "))
print("El total de números ingresados es de:" ,nros)
    

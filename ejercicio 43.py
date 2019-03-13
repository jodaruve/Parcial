## 43
print("Este programa le ayudara a calcular si los números ingresados están incrementando o disminuyendo")
n1=int(input("Por favor ingrese un numero "))
n2=int(input("Por favor ingrese otro número "))
n3=int(input("Por favor ingrese otro número "))
if n1>n2 and n2>n3:
  print("Los números están disminuyendo")
elif n1<n2 and n2<n3:
  print("Los números están incrementando")
else:
  print("Los números ni incrementan ni disminuyen")

## 43
print("Este programa le ayudara a calcular si los n�meros ingresados est�n incrementando o disminuyendo")
n1=int(input("Por favor ingrese un numero "))
n2=int(input("Por favor ingrese otro n�mero "))
n3=int(input("Por favor ingrese otro n�mero "))
if n1>n2 and n2>n3:
  print("Los n�meros", n1,n2,n3, "est�n disminuyendo")
elif n1<n2 and n2<n3:
  print("Los n�meros", n1,n2,n3, "est�n incrementando")
else:
  print("Los n�meros", n1,n2,n3, "ni incrementan ni disminuyen")

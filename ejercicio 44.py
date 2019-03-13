## 44
print("Este programa calculara si los números ingresados están entre 0 y 5")
num1=int(input("Por favor ingrese un numero "))
num2=int(input("Por favor ingrese otro numero "))
if num1 and num2>5:
  print("Los numeros", num1,num2, "no estan entre 0 y 5")
elif num1 and num2<0:
  print("Los numeros", num1,num2, "no estan entre 0 y 5")
else:
  print("Los numero", num1,num2, "estan entre 0 y 5")
  
  

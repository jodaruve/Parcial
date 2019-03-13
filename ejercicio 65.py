## 65
sum_p=0
sum_i=0
i=0
c_p=0
c_i=0
print("Este programa le mostrara el promedio de los números pares y impares ingresados")
cant=int(input("Por favor digite la cantidad de números que va a ingresar "))
while i<cant:
  i=i+1
  num=float(input("Por favor ingrese el numero "))
  if num%2==0:
    c_p=c_p+1
    sum_p=sum_p+num
  else:
    c_i=c_i+1
    sum_i=sum_i+num
prom_p=sum_p/c_p
prom_i=sum_i/c_i
print("El promedio de los números pares es de", prom_p)
print("El promedio de los números impares es de", prom_i)

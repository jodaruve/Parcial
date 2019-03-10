## 64
sum=0
i=0
print("Este programa le mostrara la suma y promedio de los números ingresados")
cant=int(input("Por favor digite la cantidad de números que va a ingresar "))
while i<cant:
 num=float(input("Por favor ingrese el numero "))
 sum=sum+num
 i=i+1
prom=sum/cant
print("La suma de los números ingresados es de", sum)
print("El promedio de los números ingresados es de", prom)

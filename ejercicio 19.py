## 19
import math
print("Este programa le mostrara la distancia entre las coordenadas dadas")
x1=int(input("Por favor ingrese un numero para asignarlo a x1 "))
y1=int(input("Por favor ingrese un numero para asignarlo a y1 "))
x2=int(input("Por favor ingrese un numero para asignarlo a x2 "))
y2=int(input("Por favor ingrese un numero para asignarlo a y2 "))
dist=math.sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
print("La distancia entre las cordenadas (x1,y1) y (x2,y2) es: ", dist)

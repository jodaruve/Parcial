## 15
print("Ete programa calculara la distancia recorrida por el objeto")
tiempo=float(input("Por favor ingrese el tiempo en segundos "))
vel=float(input("Por favor ingrese la velocidad en m/s "))
ac=float(input("Por favor ingrese la aceleracion en m/s^2 "))
dis=0.5*ac*(tiempo*2)+vel*tiempo
print("La distancia recorrida por el objeto fue de:", dis, "m/s")
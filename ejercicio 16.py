## 16
print("Este programa mostrara la velocidad final de un objeto")
tiempo=float(input("Por favor ingrese el tiempo en segundos "))
ac=float(input("Por favor ingrese la aceleracion en m/s^2 "))
v_i=float(input("por favor ingrese la velocidad inicial en m/s "))
v_final=(ac*tiempo)+v_i
print("L a velocidad final del objeto fue de:", v_final, "m/s")
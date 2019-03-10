## 23
print("Este programa le mostrara la hora de acuerdo con la cantidad de segundos que ingrese")
seg=int(input("Por favor ingrese la cantidad de segundos "))
min=seg/60
seg2=int(seg%60)
hora=int(min/60)
min2=int(min%60)
print("la hora es:", hora, ":", min2, ":", seg2)
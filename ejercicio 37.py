## 37
print("Este programa calculara en valor del tiquete en avion")
dist=float(input("Por favor ingrese la distancia en km "))
dias=int(input("Por favor ingrese los dias de estadia "))
v_dist=dist*5000
v_desc=v_dist*0.15
v_tiq=v_dist-v_desc
if v_tiq<100000:
  print("El costo del tiquete es de 100000")
elif dist>1000 and dias>7:
  print("El costo del tiquete es de:", v_tiq)
else:
  print("El costo del tiquete es de", v_dist)
  

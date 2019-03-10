## 78
print("ejercicio del Boing 747")
mayor_p=0
menor_p=0
me_peso=0
ma_peso=0
peso=0
pesos=0
c_bultos=0
p_bulto=float(input("Por favor ingrese el peso del bulto en Kgb "))
if p_bulto>500:
  print("El bulto es muy pesado y no podremos transportarlo")
while peso<18000:
  c_bultos=c_bultos+1
  if p_bulto<25:
    peso=peso+p_bulto
    menor_p=p_bulto
    if p_bulto>menor_p:
      me_peso=p_bulto
    pesos=pesos+0
  elif p_bulto<300:
    precio=p_bulto*1500
    peso=peso+p_bulto
    pesos=pesos+precio
  elif p_bulto<501:
    mayor_p=p_bulto
    if p_bulto>mayor_p:
      ma_peso=p_bulto
    precio=p_bulto*2500
    peso=peso+p_bulto
    pesos=pesos+precio
  p_bulto=float(input("Por favor ingrese el peso del bulto en Kgb "))
dolares=pesos*3165
prom=peso/c_bultos
print("El total de bultos es de:", c_bultos)
print("El bulto más pesado pesa:", ma_peso)
print("El bulto más liviano pesa:", me_peso)
print("El peso promedio es:", prom)
print("El ingreso en pesos es:", pesos)
print("El ingreso en dolares es:", dolares)

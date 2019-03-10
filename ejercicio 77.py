## 77
print("Este programa comparara su usuario y contrasegna")
intentos=1
usuario=input("Por favor ingrese el nombre de usuario ")
contra=input("Por favor ingrese la contrasegna ")
if usuario=='jodaruve' and contra=='qwerty':
  print("Usuario y contrasegna correcta...")
while intentos<3:
    if usuario!='jodaruve' and contra!='qwerty':
      intentos=intentos+1
      print("Usuario y/o contrasegna incorrectos. por favor inténtelo nuevamente")
      print("")
      usuario=input("-Por favor ingrese el nombre de usuario ")
      contra=input("-Por favor ingrese la contrasegna ")
print("Usuario y/o contrasegna incorrectos. por favor inténtelo nuevamente")
print("-Por favor inténtelo nuevamente otro día")

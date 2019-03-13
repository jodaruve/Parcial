## 68
print("Este programa le mostrara la cantidad de números positivos, negativos, pares, impares y multiplos de ocho ingresados. Recuerde que cuando no desee ingresar más números debe escribir -00")
t_positivos=0
t_negativos=0
t_pares=0
t_impares=0
mult=0
num=float(input("Por favor ingrese un numero "))
while num!=-00:
  if num>0:
    t_positivos=t_positivos+1
  else:
    t_negativos=t_negativos+1
  
  if num%2==0:
    t_pares=t_pares+1
  else:
    t_impares=t_impares+1
  if num%8==0
    mult=mult+1
  num=float(input("Por favor ingrese un numero "))
print("La cantidad de positivos es de:", t_positivos)
print("la cantidad de negativos es de:", t_negativos)
print("La cantidad de pares es de:", t_pares)
print("La cantidad de impares es de:", t_impares)
print("Los numeros multiplos de ocho fueron:", mult)

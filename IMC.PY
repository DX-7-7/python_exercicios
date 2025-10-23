print(input("indice de peso"))

massa = float(input("digite o valor da massa(m) : "))
altura = float(input("digite a sua altura (m)"))
IMC = massa/altura **2
print("o seu imc é {:.2f}" .format(IMC))

if  IMC <17 :
   print("Muito abaixo do peso.")
elif IMC >17 and IMC <= 18.5:
   print("abaixo  do  peso.")
elif IMC >18.5 and IMC <=25:
   print("peso ideal")
elif IMC > 25 and IMC <= 30:
   print("sobrepeso")
elif IMC >30 and IMC <= 35 :
   print("obesidade")
elif IMC> 35 and IMC <= 40:
   print("obesidade severa")
else:
   print("obesidade morbida")
   
   
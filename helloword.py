peso = float(input ("digite seu peso (kg):"))
altura = float(input ("digite sua altura(m):"))
imc = peso/(altura**2)
imc = round(imc,1)
#print(imc)
print("seu imc é:",imc)
#print("estou muito abaixo do peso" ,imc<17)
#print("estou abaixo do peso" ,imc>=17 and imc<18.5)
#print("estou com peso adequado" ,imc>=18.5 and imc<24.9)
#print ("estou acima do peso" ,imc>25)
if imc<17:
   print("estou muito abaixo do peso")
elif imc>=17 and imc<18.5:
   print("estou abaixo do peso")
elif imc>=18.5 and imc<24.9:
   print("estou com peso adequado")
elif imc>25:
   print("estou acima do peso")

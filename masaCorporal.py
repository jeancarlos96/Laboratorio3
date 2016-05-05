peso= float (input("Ingrese el peso de la persona en kg:  "))
estatura = float(input("Ingrese la estatura de la persona en metros:  "))

masa=peso/(estatura*estatura)
print ("IMC:")
print (round(masa,2))

if masa>=18 and masa<=25.9:
	print ("NORMAL")
elif masa<18:
	print ("Desnutricion")
elif masa==25 and masa<=26.9:
	print ("Sobrepeso")
elif masa>=27 and masa<=29.9:
	print ("Obesidad Grado I (ALTO)")
elif masa>=30 and masa<=39.9:
	print ("Obesidad Grado II (MUY ALTO)")
else:
	print ("Obesidad Grado III (EXtremadamente ALTO)")
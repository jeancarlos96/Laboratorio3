a = int(input("Ingrese Primer numero "))
b = int(input("Ingrese Segundo numero "))
x=str("ERROR")
z=str("La division para 0 no existe")

op=int(input("Que operacion Desea realizar"))
print ("1:Suma \n 2:Resta \n 3:Multiplicacion \n 4:Division")
if op==1:
	def suma():
		c=a+b
		return c
	s=suma()	
	print (s)
elif op==2:
	def resta():
		c=a-b
		return c
		print (c)
	r=resta()	
	print (r)
elif op==3:
	def multi():		
		c=a*b
		return c
		print (c)
	m=multi()	
	print (m)
else:
	def division():	
		if (b==0):
			return z
		elif (a==0):
			return x	
		else: 
			c=a/b
			return c
	d=division()
	print (d)

suma()
resta()
multi()
division()





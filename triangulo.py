import math
l1=int(input("Ingrese primer lado del triangulo :   "))
l2=int(input("Ingrese segundo lado del triangulo:   "))
l3=int(input("Ingrese tercer lado del triangulo:    "))
s=(l1+l2+l3)/2
a=(s-l1)
b=(s-l2)
c=(s-l3)
tot=s*a*b*c
area=math.sqrt(tot)

print (round(area,2)) 
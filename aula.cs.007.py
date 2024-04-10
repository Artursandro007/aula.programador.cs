print (" bom dia ")
# calcule o lados do piramide
a = float(input('escreva o tamanho do primeira lado '))
b = float(input('escreva o tamanho do segundo lado '))
c = float(input('escreva o tamano do terceiro lado '))
   

            # tipos de piramite
if(a + b < c) or ( a + c < b)or(b + c < a):
   print("nao e um triangulo") 
elif (a == b) and (a == c):
   print(" equilatero")
elif (a == b) or (a == c) or (b == c):
   print ("isosceles")
else:
   print ("escaleno")

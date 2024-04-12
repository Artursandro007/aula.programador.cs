# calculo de anos bissexto
print ("bom dia tudo bem")
ano = int(input('ano : '))
if(ano/4==0 and ano/100!=0)or(ano/400==0):
    print(" bissexto")
else:
    print(" nao e bissexto")
    
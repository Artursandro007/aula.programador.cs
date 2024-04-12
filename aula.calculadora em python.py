# calculadora em python
print ("bom dia tudo bem")
num1 = float(input('digite um numero '))
num2 = float(input('digite um numero '))
# operadores de calculos
operaçao = input ('digite o sinal da operaçao: ')
if operaçao == "+" :
    print(num1 + num2)
elif operaçao == "-" :
    print(num1 - num2)
elif operaçao == "*" :
    print(num1 * num2)
elif operaçao == "/" :
    print(num1 / num2)
else :
    print("erro ! por favor digite um sinal valido ")
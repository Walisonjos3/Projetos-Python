
def soma(n):

    soma = 0

    for i in range(n):
        num = float(input('Digite o número: '))
        soma += num
    
    return soma

def subtracao(n):

    n1 = float(input('Digite o número: '))
    resultado_subtracao = n1

    for i in range(n - 1):
        num = float(input('Digite o número: '))
        resultado_subtracao -= num

    return resultado_subtracao

def multiplicacao(n):
    resultado = 1

    for i in range(n):
        num = float(input('Digite o número: '))
        resultado *= num
    
    return resultado

def divisao(n):
    n1 = float(input('Digite o número: '))
    resultado_divisao = n1

    for i in range(n -1):
        num = float(input('Digite o número: '))
        resultado_divisao /= num
    
    return resultado_divisao

def potencia(n):
    resultado_potencia = 0

    for i in range(n):
        base = int(input('Digite a base: '))
        potenciacao = float(input('Digite o expoente: '))
        resultado_potencia += base ** potenciacao
    
    return resultado_potencia

def fatorial(n):

    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i
    
    return fatorial

def numero_primo(n):
    divisores = 0

    for i in range(1, n + 1):
        if n %  i == 0:
            divisores += 1
    
    if divisores == 2:
        return f'O número {n} é primo.'
    
    return f'O número {n} não é primo.'

def main():

    while True:

        print("""
===== CALCULADORA =====  
    0 - SAIR
    1 - SOMAR
    2 - SUBTRAIR
    3 - MULTIPLICAR
    4 - DIVIDIR
    5 - POTENCIAÇÃO
    6 - NÚMERO PRIMO
    7 - FATORIAL
            """)
        
        operador = int(input('Digite aqui: '))

        if operador == 0:
            break
        
        elif operador == 1:
            quantidade_soma = int(input('\nQuantos números quer somar ? '))
            print(f'\nResultado final = {soma(quantidade_soma)}')
        
        elif operador == 2:
            quantidade_menos = int(input('\nQuantos números quer subtrair ? '))
            print(f'\nResultado final = {subtracao(quantidade_menos)}')
        
        elif operador == 3:
            quantidade_multi = int(input('\nQuantos números quer multiplicar ? '))
            print(f'\nResultado final = {multiplicacao(quantidade_multi)}')
        
        elif operador == 4:
            quantidade_divisao = int(input('\nQuantos números quer dividir ? '))
            print(f'\nResultado final = {divisao(quantidade_divisao)}')
        
        elif operador == 5:
            quantidade_potencia = int(input('\nQuantas potências quer ? '))
            print(f'\nResultado final = {potencia(quantidade_potencia)}')
        
        elif operador == 6:
            num_primo = int(input('\nDigite o número: '))
            print(f'\n{numero_primo(num_primo)}')
        
        else:
            num_fatorial = int(input('\nDigite o número: '))
            print(f'\nResultado final = {fatorial(num_fatorial)}')
main()

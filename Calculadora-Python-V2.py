def soma(n):
    soma = 0
    for i in range(n):
        while True:
            try:
                num = float(input('Digite o número: '))
                soma += num
                break
            except ValueError:
                print('Entrada inválida! Digite apenas números.')
    return soma

def subtracao(n):
    while True:
        try:
            n1 = float(input('Digite o número: '))
            break
        except ValueError:
            print('Entrada inválida! Digite apenas números.')

    resultado_subtracao = n1

    for i in range(n - 1):
        while True:
            try:
                num = float(input('Digite o número: '))
                resultado_subtracao -= num
                break
            except ValueError:
                print('Entrada inválida! Digite apenas números.')

    return resultado_subtracao

def multiplicacao(n):
    resultado = 1
    for i in range(n):
        while True:
            try:
                num = float(input('Digite o número: '))
                resultado *= num
                break
            except ValueError:
                print('Entrada inválida! Digite apenas números.')
    return resultado

def divisao(n):
    while True:
        try:
            n1 = float(input('Digite o número: '))
            break
        except ValueError:
            print('Entrada inválida! Digite apenas números.')

    resultado_divisao = n1

    for i in range(n - 1):
        while True:
            try:
                num = float(input('Digite o número: '))
                if num == 0:
                    print('Erro: Não é possível dividir por zero! Digite outro número.')
                    continue
                resultado_divisao /= num
                break
            except ValueError:
                print('Entrada inválida! Digite apenas números.')

    return resultado_divisao

def potencia(n):
    resultado_potencia = 0
    for i in range(n):
        while True:
            try:
                base = float(input('Digite a base: '))
                potenciacao = float(input('Digite o expoente: '))
                resultado_potencia += base ** potenciacao
                break
            except ValueError:
                print('Entrada inválida! Digite apenas números.')
    return resultado_potencia

def fatorial(n):
    if n < 0:
        return 'Erro: Não existe fatorial de número negativo.'
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def numero_primo(n):
    if n <= 1:
        return f'O número {n} não é primo.'
        
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
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
        
        try:
            operador = int(input('Digite aqui: '))
        except ValueError:
            print('\nOpção inválida! Digite um número inteiro do menu.')
            continue

        if operador == 0:
            print('\nSaindo da calculadora...')
            break
        
        elif operador == 1:
            try:
                quantidade_soma = int(input('\nQuantos números quer somar ? '))
                print(f'\nResultado final = {soma(quantidade_soma)}')
            except ValueError:
                print('\nPor favor, digite um número inteiro para a quantidade.')
        
        elif operador == 2:
            try:
                quantidade_menos = int(input('\nQuantos números quer subtrair ? '))
                print(f'\nResultado final = {subtracao(quantidade_menos)}')
            except ValueError:
                print('\nPor favor, digite um número inteiro para a quantidade.')
        
        elif operador == 3:
            try:
                quantidade_multi = int(input('\nQuantos números quer multiplicar ? '))
                print(f'\nResultado final = {multiplicacao(quantidade_multi)}')
            except ValueError:
                print('\nPor favor, digite um número inteiro para a quantidade.')
        
        elif operador == 4:
            try:
                quantidade_divisao = int(input('\nQuantos números quer dividir ? '))
                print(f'\nResultado final = {divisao(quantidade_divisao)}')
            except ValueError:
                print('\nPor favor, digite um número inteiro para a quantidade.')
        
        elif operador == 5:
            try:
                quantidade_potencia = int(input('\nQuantas potências quer ? '))
                print(f'\nResultado final = {potencia(quantidade_potencia)}')
            except ValueError:
                print('\nPor favor, digite um número inteiro para a quantidade.')
        
        elif operador == 6:
            try:
                num_primo = int(input('\nDigite o número: '))
                print(f'\n{numero_primo(num_primo)}')
            except ValueError:
                print('\nPor favor, digite um número inteiro válido.')
        
        elif operador == 7:
            try:
                num_fatorial = int(input('\nDigite o número: '))
                print(f'\nResultado final = {fatorial(num_fatorial)}')
            except ValueError:
                print('\nPor favor, digite um número inteiro válido.')
        
        else:
            print('\nOpção inválida! Escolha um número de 0 a 7.')

main()

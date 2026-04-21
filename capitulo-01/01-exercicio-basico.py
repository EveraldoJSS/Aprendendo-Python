# input, por padrão, salva sempre o resultado em string
my_name = input('Qual o seu nome? ')
print()
print('É um prazer te conhecer, ' + my_name + '.')
print('Seu nome tem ' + str(len(my_name)) + ' letras.')
print()

my_age = input('Qual a sua idade? ')
print()
# int converte o resultado de my_age em um número inteiro — se não conseguir, gera um erro.
# str converte para string para concatenar.
print('Você tem ' + str(int(my_age)) + ' anos.')
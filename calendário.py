#Agenda Simples

import calendar #Utiliza a biblioteca padrão 'calendar' do Python

print('GERADOR DE CALENDARIO')

mes = int(input('Digite o numero do mes (1-12): '))
ano = int(input('Digite o ano: '))

if mes < 1 or mes > 12:
    print('MES INVALIDO! DIGITE UM NUMERO ENTRE 1 E 12. ')

else:
    print('\n SEU CALENDARIO \n')
    print(calendar.month(ano, mes)) 
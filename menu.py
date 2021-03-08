from feeders import *

def consulta_decisao():
  print('Opções:   ')
  print('1 - Deferidos\n2 - Indeferidos\n3 - Deferidos e Indeferidos')
  valor = int(input('Informe qual opção você deseja: '))
  if valor == 1:
    cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
    pessoa = encontra_pessoa(cpf)
    print(pessoa.get_nome() +':')
    print(pessoa.num_decisoes(True))
  elif valor == 2:
    cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
    pessoa = encontra_pessoa(cpf)
    print(pessoa.get_nome() +':')
    print(pessoa.num_decisoes(False))
  elif valor == 3:
    cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
    pessoa = encontra_pessoa(cpf)
    print(pessoa.get_nome() +':')
    print(pessoa.num_decisoes(True))
    print(pessoa.num_decisoes(False))







# def menu_principal():
#   valorMenu = True
#   while valorMenu == True:
#       print('--------------------- SysJurídico v12.00 -----------------------------')
#       print('----------------------------- MENU -----------------------------------\n')
#       print('1 - Tempo das Audiências')
#       print('2 - Listar as decisões de um processo de uma pessoa')
#       print('3 - Listar os custos processuais de uma pessoa')
#       print('4 - Listar os custos processuais de uma pessoa por advogado')
#       print('5 - Listar os clientes de um advogado')
#       print('6 - Inseri Audiência em um Processo')
#       print('9 - Informações')
#       print('9999 - Teste')
#       print('0 - Sair do Sistema')
#       print('----------------------------------------------------------------------\n')
#       valorMenu = int(input('Informe o número corresponde ao que deseja realizar: '))
#       if valorMenu == 1:
#           tempo = int(input('Informe o tempo da audiência em minutos: '))
#           for i in range (len(lista_processos)):
#               print(f'Processo {i+1}: {lista_processos[i].audiencias_temp(tempo)}')
#           valorMenu = int(input('Deseja voltar ao menu? Digite 1 para voltar ao Menu e 0 para encerrar: '))

#       elif valorMenu == 2 :
#             print('Opções:   ')
#             print('1 - Deferidos\n2 - Indeferidos\n3 - Deferidos e Indeferidos')
#             valor = int(input('Informe qual opção você deseja:'))
#             if valor == 1:
#               cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
#               pessoa = encontra_pessoa(cpf)
#               print(pessoa.get_nome() +':')
#               print(pessoa.num_decisoes(True))
#             elif valor == 2:
#               cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
#               pessoa = encontra_pessoa(cpf)
#               print(pessoa.get_nome() +':')
#               print(pessoa.num_decisoes(False))
#             elif valor == 3:
#               cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
#               pessoa = encontra_pessoa(cpf)
#               print(pessoa.get_nome() +':')
#               print(pessoa.num_decisoes(True))
#               print(pessoa.num_decisoes(False))
#             valorMenu = int(input('Deseja voltar ao menu? Digite 1 para voltar ao Menu e 0 para encerrar: '))

#       elif valorMenu == 3 :
#           cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
#           pessoa = encontra_pessoa(cpf)
#           print(pessoa.custo_total())

#       elif valorMenu == 4 :
#           cod_adv = input('Informe o código do advogado (Ex: OAB-DF 222.222): ')
#           cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
#           pessoa = encontra_pessoa(cpf)
#           print(pessoa.custo_total_adv(cod_adv))

#       elif valorMenu == 5 :
#           cod_adv = input('Informe o código do advogado (Ex: OAB-DF 222.222): ')
#           adv = encontra_adv(cod_adv)
#           print(adv.lista_clientes()) 

#       elif valorMenu == 6 :   
#         cria_audiencia()
      
#       elif valorMenu == 7 :   
#         compara_custo_adv()

#       elif valorMenu == 9 :
#         menu_informacoes()

#       elif valorMenu == 9999:
#           imp_teste()
#           valorMenu = int(input('Deseja voltar ao menu? Digite 1 para voltar ao Menu e 0 para encerrar: '))

#       elif valorMenu == 0 :
#           print('\n\nFinalizando o sistema! Até mais')
#           print('SysJurídico v12.00\n\n')
#           valorMenu = False
#       else:
#           print('Erro! O valor informado é inválido !!! Tente outra vez\n')


# def menu_informacoes():
#   menuOpcoes = 1
#   while menuOpcoes == 1:
#     print('----------------------------- OPÇÕES -----------------------------------\n')
#     print('1 - Processos')
#     print('2 - Pessoas')
#     print('3 - Advogados')
#     print('4 - Audiencias')
#     print('5 - Custos')
#     print('0 - Sair do Sistema')
#     print('----------------------------------------------------------------------\n')

#     valorOpcao = int(input('Escolha a categoria das informações que deseja visualizar: '))
#     if valorOpcao == 1:
#       print('Processos Disponíveis:')
#       for i in range(len(lista_processos)):
#         print(lista_processos[i].get_cod_proc())
      
#       numProc = int(input('\nInforme o código do processo desejado: '))
#       print(f'{encontra_proc(numProc)}\n')

#     elif valorOpcao == 2:
#       print('Pessoas Disponíveis:')
#       for i in range(len(lista_pessoas)):
#         print(lista_pessoas[i].get_nome(), lista_pessoas[i].get_cpf())
      
#       cpfPessoa = input('\nInforme o CPF da pessoa desejada: ')
#       pessoa = encontra_pessoa(cpfPessoa)
#       print('\n----------------------------------------------------------------------\n\n')
#       print(pessoa)

#     elif valorOpcao == 3:
#       print('Advogados Disponíveis:')
#       for i in range(len(lista_adv)):
#         print(lista_adv[i].get_nome(), lista_adv[i].get_cod_oab())
      
#       oabAdv = input('\nInforme o número da OAB do(a) advogado(a) desejado(a): ')
#       adv = encontra_adv(oabAdv)
#       print('\n----------------------------------------------------------------------\n\n')
#       print(f'{adv}\n')
    
#     elif valorOpcao == 4:
#       print('Audiências Disponíveis:')
#       for i in range(len(lista_audiencias)):
#         print(lista_audiencias[i].get_cod_aud())
      
#       codAud = int(input('\nInforme o código da Audiência desejada: '))
#       aud = encontra_aud(codAud)
#       print('\n----------------------------------------------------------------------\n\n')
#       print(f'{aud}\n')

#     elif valorOpcao == 5:
#       print('Custos Disponíveis:')
#       for i in range(len(lista_custos)):
#         print(lista_custos[i].get_cod_custo())
      
#       codCusto = int(input('\nInforme o código do Custo desejado: '))
#       custo = encontra_custo(codCusto)
#       print('\n----------------------------------------------------------------------\n\n')
#       print(f'{custo}\n')
    
#     elif valorOpcao == 0:
#       menu_principal()


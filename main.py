from advogado import Advogado
from processo import Processo
from pessoa import Pessoa
from audiencia import Audiencia
from custo import Custo

# CUSTOS
custo1 = Custo('01/01/2021', 'caro', 10000.00)
custo2 = Custo('02/02/2022', 'barato', 500.00)
custo3 = Custo('03/03/2023', 'medio', 5000.00)
custo4 = Custo('04/04/2024', 'gratuito', 0.00)
custo5 = Custo('05/05/2025', 'carissimo', 500000.00)
custo6 = Custo('06/06/2026', 'gratuito', 0.00)
custo7 = Custo('07/07/2027', 'carissimo', 1000000.00)
custo8 = Custo('08/08/2028', 'barato', 800.00)
custo9 = Custo('09/09/2029', 'gratuito', 0.00)
custo10 = Custo('10/10/2030', 'caro', 15000.00)

#Pessoa
lista_pessoas = []
Jair = Pessoa('666.666.666-17', 'Jair Bolsonaro')
Ciro = Pessoa('202.020.202-12', 'Ciro Gomes')
Fernando = Pessoa('030.030.030-13','Fernando Haddad')
Marina = Pessoa('420.420.420-18', 'Marina Silva')
Joao = Pessoa('171.171.171-30', 'Joao Amoedo')
Geraldo = Pessoa('123.456.789-45', 'Geraldo Alckmin')
Benevenuto = Pessoa('777.777.777-51', 'Benevenuto Daciolo')
lista_pessoas.append(Jair)
lista_pessoas.append(Ciro)
lista_pessoas.append(Fernando)
lista_pessoas.append(Marina)
lista_pessoas.append(Joao)
lista_pessoas.append(Geraldo)
lista_pessoas.append(Benevenuto)


def encontra_pessoa(cpf_pessoa):
    for i in range(len(lista_pessoas)):
        if lista_pessoas[i].get_cpf() == cpf_pessoa:
            return lista_pessoas[i]
            break

# ADVOGADOS
lista_adv = []
Gilmar = Advogado('OAB-MA 111.111', 'Gilmar Mendes')
Carmem = Advogado('OAB-DF 222.222', 'Carmem Lucia')
Roberto = Advogado('OAB-RJ 333.333', 'Roberto Lewandowski')
Rosa = Advogado('OAB-SP 444.444', 'Rosa Weber')
lista_adv.append(Gilmar)
lista_adv.append(Carmem)
lista_adv.append(Roberto)
lista_adv.append(Rosa)

def encontra_adv(cod_adv):
    for i in range(len(lista_adv)):
        if lista_adv[i].get_cod_oab() == cod_adv:
            return lista_adv[i]
            break


# AUDIENCIAS
audiencia1 = Audiencia('01/01/2021', 'Acordo', 60)
audiencia2 = Audiencia('02/02/2022', 'Litigio', 90)
audiencia3 = Audiencia('03/03/2023', 'Acordo', 30)
audiencia4 = Audiencia('04/04/2024', 'Litigio', 120)
audiencia5 = Audiencia('05/05/2025', 'Acordo', 90)
audiencia6 = Audiencia('06/06/2026', 'Litigio',120)
audiencia7 = Audiencia('07/07/2027', 'Acordo', 60)
audiencia8 = Audiencia('08/08/2028', 'Litigio', 30)
audiencia9 = Audiencia('09/09/2029', 'Acordo', 90)
audiencia10 = Audiencia('10/10/2030', 'Litigio', 60)


#PROCESSOS
processo1 = Processo('Dano Morais', custo3, False, 'Transitado em julgado', Ciro, Carmem)
processo2 = Processo('Divorcio Litigioso', custo5, True, 'Recurso', Jair, Gilmar)
processo3 = Processo('Indenizacao por Danos Materiais', custo2, True, 'Em execucao',Marina , Carmem)
processo4 = Processo('Execucao Contratual', custo9, False, 'Arquivado', Geraldo, Gilmar)
processo5 = Processo('Habeas Corpus', custo4, False, 'Negado', Jair, Gilmar)
processo6 = Processo('Habeas Data', custo6, True, 'Transitado em Julgado', Benevenuto, Rosa)
processo7 = Processo('Pedido de Liminar', custo8, False, 'Arquivado', Fernando, Carmem)
processo8 = Processo('Homicidio Duplamente Qualificado', custo7, True, 'Diligencia', Jair, Gilmar)
processo9 = Processo('Recurso Extraordinario', custo10, False, 'Embargos Declaratorios', Joao, Roberto)
processo10 = Processo('Dano Morais', custo3, True, 'Transitado em julgado', Ciro, Carmem)


Ciro.set_processos(processo1)
Ciro.set_processos(processo9)
Ciro.set_processos(processo10)
Carmem.set_processos(processo1)
Carmem.set_processos(processo3)
processo1.set_audiencia(audiencia1)
processo1.set_audiencia(audiencia2)
processo1.set_audiencia(audiencia3)

def imp_teste():
    print('\n\n')
    print("         DEMONSTRAÇÃO")
    print(Ciro.get_processos()[0].get_custo().get_valor())
    print(Ciro.custo_total())
    print(Ciro.custo_total_adv('OAB-DF 222.222'))
    print(Ciro.num_decisoes(True))
    print(Carmem.lista_clientes())
    print(processo1.audiencias_temp(60) + "\n\n")


valorMenu = 9999
while valorMenu != 0:
    print('--------------------- SysJurídico v12.00 -----------------------------')
    print('----------------------------- MENU -----------------------------------\n')
    print('1 - Impressão teste')
    print('2 - Listar os clientes de um advogado')
    print('3 - Listar os custos processuais de uma pessoa')
    print('0 - Sair do Sistema')
    print('----------------------------------------------------------------------\n')
    valorMenu = int(input('Informe o número corresponde ao que deseja realizar: '))
    if valorMenu == 1:
        imp_teste()
        valorMenu = int(input('Deseja voltar ao menu? Digite 1 para voltar ao Menu e 0 para encerrar: '))
    elif valorMenu == 2 :
        cod_adv = input('Informe o código do advogado (Ex: OAB-DF 222.222): ')
        adv = encontra_adv(cod_adv)
        print(adv.lista_clientes())
    elif valorMenu == 3 :
        cpf = input('Informe o CPF da Pessoa (Ex: 123.456.789-45): ')
        pessoa = encontra_pessoa(cpf)
        print(pessoa.custo_total())
    elif valorMenu == 0 :
        print('\n\nFinalizando o sistema! Até mais')
        print('SysJurídico v12.00\n\n')
        valorMenu = 0
    else:
        print('Erro! O valor informado é inválido !!! Tente outra vez\n')



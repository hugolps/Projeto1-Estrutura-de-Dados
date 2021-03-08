from advogado import Advogado
from processo import Processo
from pessoa import Pessoa
from audiencia import Audiencia
from custo import Custo

# CUSTOS
lista_custos = []

custo1 = Custo('01/01/2021', 'caro', 10000.00, 1)
custo2 = Custo('02/02/2022', 'barato', 500.00, 2)
custo3 = Custo('03/03/2023', 'medio', 5000.00, 3)
custo4 = Custo('04/04/2024', 'gratuito', 0.00, 4)
custo5 = Custo('05/05/2025', 'carissimo', 500000.00, 5)
custo6 = Custo('06/06/2026', 'gratuito', 0.00, 6)
custo7 = Custo('07/07/2027', 'carissimo', 1000000.00, 7)
custo8 = Custo('08/08/2028', 'barato', 800.00, 8)
custo9 = Custo('09/09/2029', 'gratuito', 0.00, 9)
custo10 = Custo('10/10/2030', 'caro', 15000.00, 10)
custo11 = Custo('11/11/2111', 'caro', 11300.00, 11)

lista_custos.extend([custo1, custo2, custo3, custo4, custo5, custo6, custo7, custo8, custo9, custo10, custo11])

#Pessoa
lista_pessoas = []
Jair = Pessoa('666.666.666-17', 'Jair Bolsonaro')
Ciro = Pessoa('202.020.202-12', 'Ciro Gomes')
Fernando = Pessoa('030.030.030-13','Fernando Haddad')
Marina = Pessoa('420.420.420-18', 'Marina Silva')
Joao = Pessoa('171.171.171-30', 'Joao Amoedo')
Geraldo = Pessoa('123.456.789-45', 'Geraldo Alckmin')
Benevenuto = Pessoa('777.777.777-51', 'Benevenuto Daciolo')


lista_pessoas.extend([Jair, Ciro, Fernando, Marina, Joao, Geraldo, Benevenuto])


# ADVOGADOS
lista_adv = []

Gilmar = Advogado('OAB-MA 111.111', 'Gilmar Mendes')
Carmem = Advogado('OAB-DF 222.222', 'Carmem Lucia')
Roberto = Advogado('OAB-RJ 333.333', 'Roberto Lewandowski')
Rosa = Advogado('OAB-SP 444.444', 'Rosa Weber')
Sandiego = Advogado('OAB-DF 777.777', 'Carmem Sandiego')

lista_adv.extend([Gilmar, Carmem, Roberto, Rosa, Sandiego])



# AUDIENCIAS

lista_audiencias = []

audiencia1 = Audiencia('01/01/2021', 'Acordo', 60, 1)
audiencia2 = Audiencia('02/02/2022', 'Litigio', 90, 2)
audiencia3 = Audiencia('03/03/2023', 'Acordo', 30, 3)
audiencia4 = Audiencia('04/04/2024', 'Litigio', 120, 4)
audiencia5 = Audiencia('05/05/2025', 'Acordo', 90, 5)
audiencia6 = Audiencia('06/06/2026', 'Litigio',120, 6)
audiencia7 = Audiencia('07/07/2027', 'Acordo', 60, 7)
audiencia8 = Audiencia('08/08/2028', 'Litigio', 30, 8)
audiencia9 = Audiencia('09/09/2029', 'Acordo', 90, 9)
audiencia10 = Audiencia('10/10/2030', 'Litigio', 60, 10)
audiencia11 = Audiencia('11/11/2031', 'Acordo', 180, 11)

lista_audiencias.extend([audiencia1, audiencia2, audiencia3, audiencia4, audiencia5, audiencia6, audiencia7, audiencia8, audiencia9, audiencia10, audiencia11])

#PROCESSOS

lista_processos = []


processo1 = Processo('Dano Morais', custo3, False, 'Transitado em julgado', Ciro, Carmem, 1)
processo2 = Processo('Divorcio Litigioso', custo5, True, 'Recurso', Jair, Gilmar, 2)
processo3 = Processo('Indenizacao por Danos Materiais', custo2, True, 'Em execucao',Marina , Carmem, 3)
processo4 = Processo('Execucao Contratual', custo9, False, 'Arquivado', Geraldo, Gilmar, 4)
processo5 = Processo('Habeas Corpus', custo4, False, 'Negado', Jair, Gilmar, 5)
processo6 = Processo('Habeas Data', custo6, True, 'Transitado em Julgado', Benevenuto, Rosa, 6)
processo7 = Processo('Pedido de Liminar', custo8, False, 'Arquivado', Fernando, Carmem, 7)
processo8 = Processo('Homicidio Duplamente Qualificado', custo7, True, 'Diligencia', Jair, Gilmar, 8)
processo9 = Processo('Recurso Extraordinario', custo10, False, 'Embargos Declaratorios', Joao, Roberto, 9)
processo10 = Processo('Dano Morais', custo3, True, 'Transitado em julgado', Ciro, Carmem, 10)
processo11 = Processo('Danos Morais', custo11, True, 'Arquivado', Ciro, Sandiego, 11)

lista_processos.extend([processo1, processo2, processo3, processo4, processo5, processo6, processo7, processo8, processo9, processo10, processo11])



#Inserindo audiências e processos iniciais
processo1.set_audiencia([audiencia1])
processo2.set_audiencia([audiencia2])
processo3.set_audiencia([audiencia3])
processo4.set_audiencia([audiencia4])
processo5.set_audiencia([audiencia5])
processo6.set_audiencia([audiencia6])
processo7.set_audiencia([audiencia7])
processo8.set_audiencia([audiencia8])
processo9.set_audiencia([audiencia9])
processo10.set_audiencia([audiencia10])
processo11.set_audiencia([audiencia11])

processo1.add_audiencia(audiencia2)
processo10.add_audiencia(audiencia9)
processo11.add_audiencia(audiencia6)

Jair.set_processos([processo2]) 
Ciro.set_processos([processo1])
Fernando.set_processos([processo7])
Marina.set_processos([processo3])
Joao.set_processos([processo9])
Geraldo.set_processos([processo4])
Benevenuto.set_processos([processo6])

Jair.add_processos(processo5)
Jair.add_processos(processo8)
Ciro.add_processos(processo10)
Ciro.add_processos(processo11)


Gilmar.set_processos([processo2])
Carmem.set_processos([processo1])
Rosa.set_processos([processo6])
Roberto.set_processos([processo9])

Carmem.add_processos(processo3)
Carmem.add_processos(processo7)
Carmem.add_processos(processo10)
# Gilmar.add_processos(processo11)
Gilmar.add_processos(processo4)
Gilmar.add_processos(processo5)
Gilmar.add_processos(processo8)

Sandiego.set_processos([processo11])



def encontra_pessoa(cpf_pessoa):
  retorno = ''
  for i in range(len(lista_pessoas)):
      if lista_pessoas[i].get_cpf() == cpf_pessoa:
          retorno = lista_pessoas[i]
          break
  if retorno == '':
    return 'CPF não encontrado'
  else:
    return retorno

def encontra_adv(cod_adv):
    retorno = ''
    for i in range(len(lista_adv)):
        if lista_adv[i].get_cod_oab() == cod_adv:
            retorno = lista_adv[i]
            break
    if retorno == '':
      return 'Código da OAB não encontrado'
    else:
      return retorno

def encontra_aud(cod_aud):
  retorno = ''
  for i in range(len(lista_audiencias)):
    if lista_audiencias[i].get_cod_aud() == cod_aud:
      retorno = lista_audiencias[i]
      break
  if retorno == '':
    return 'Código da Audiência não encontrado'
  else:
    return retorno

def encontra_custo(cod_custo):
  retorno = ''
  for i in range(len(lista_custos)):
    if lista_custos[i].get_cod_custo() == cod_custo:
      retorno = lista_custos[i]
      break
  if retorno == '':
    return 'Código do Custo não encontrado'
  else:
    return retorno

def encontra_proc(cod_proc):
  retorno = ''
  for i in range(len(lista_processos)):
    if lista_processos[i].get_cod_proc() == cod_proc:
      retorno = lista_processos[i]
      break
  if retorno == '':
    return 'Código do Processo não encontrado'
  else:
    return retorno


def cria_audiencia():
  cod_proc = int(input('Informe o código do processo em que vc deseja cadastrar uma audiência: '))
  processo = ''
  contador = 0
  for i in range (len(lista_processos)):
    if lista_processos[i].get_cod_proc() == cod_proc:
      contador += 1
      data = input('Informe a data da audiência a ser cadastada no formato dd/mm/aaaa: ')
      recomendacao = input('Digite se é a audiência será para Acordo ou Litígio: ')
      duracao = int(input('Informe o tempo da audiência em minutos: '))
      cod_aud = int(input('Informa o código da audiência a ser cadastrada: '))

      for i in range(len(lista_audiencias)):
        if lista_audiencias[i].get_cod_aud() == cod_aud:
          print('Código da Audiência já existente. Impossível cadastrar. Tente novamente com um código diferente')
        else:
          adicionado = lista_processos[i].add_audiencia(Audiencia(data, recomendacao, duracao, cod_aud))
          return lista_processos[i].mostra_audiencias()
  if contador == 0:
    return ('Código do Processo não encontrado. Tente novamente com um código diferente')


def compara_custo_adv():
  adv1 = input('informa a OAB do primeiro advogado: ')
  adv2 = input('informa a OAB do segundo advogado: ')

  soma_adv1 = 0
  soma_adv2 = 0

  for i in range(len(lista_processos)):
    if lista_processos[i].get_advogado().get_cod_oab() == adv1:
      soma_adv1 += lista_processos[i].get_custo().get_valor()
    elif lista_processos[i].get_advogado().get_cod_oab() == adv2:
      soma_adv2 += lista_processos[i].get_custo().get_valor()

  print(soma_adv1)
  print(soma_adv2)
  retorno = ''
  if soma_adv1 > soma_adv2:
    retorno = f'O(a) Advogado(a) {encontra_adv(adv1).get_nome()} tem o custo total de seus processos de R$ {soma_adv1 - soma_adv2} a mais do que o(a) Advogado(a) {encontra_adv(adv2).get_nome()}'
  elif soma_adv2 > soma_adv1:
    retorno = f'O(a) Advogado(a) {encontra_adv(adv2).get_nome()} tem o custo total de seus processos de R$ {soma_adv2 - soma_adv1} a mais do que o(a) Advogado(a) {encontra_adv(adv1).get_nome()}'
  else:
    print(f'Custo do(a) Advogado {encontra_adv(adv1).get_nome()}: R$ {soma_adv1}')
    print(f'Custo do(a) Advogado {encontra_adv(adv2).get_nome()}: R$ {soma_adv2}')
    retorno = 'Os dois advogados tem custos iguais'

  return retorno

  
def imp_teste():
    print('\n\n')
    print("         DEMONSTRAÇÃO")
    print(Ciro.get_processos()[0].get_custo().get_valor())
    print(Ciro.custo_total())
    print(Ciro.custo_total_adv('OAB-DF 222.222'))
    print(Ciro.num_decisoes(True))
    print(Carmem.lista_clientes())
    print(processo1.audiencias_temp(60) + "\n\n")


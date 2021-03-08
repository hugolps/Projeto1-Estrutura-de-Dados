class Pessoa:
  
  def __init__(self, cpf, nome, processo = []):
    self._cpf = cpf
    self._nome = nome
    self._processos = processo

    # GETTER AND SETTERS

  def __str__(self):
    processos = ''
    for i in range(len(self._processos)):
      processos += f'{self._processos[i]}\n'
    return f'CPF: {self._cpf}\nNome: {self._nome}\n\nProcessos: \n{processos}'

  def get_cpf(self):
    return self._cpf

  def set_cpf(self, novo_cpf):
    self._cpf = novo_cpf

  def get_nome(self):
    return self._nome

  def set_nome(self, novo_nome):
    self._nome = novo_nome

  def get_processos(self):
    return self._processos
  
  def lista_processos(self):
    processos = ''
    for i in range(len(self._processos)):
      processos += f'{self._processos[i]}\n'
    return processos
    
  def set_processos(self, novo_processo):
    self._processos = novo_processo

  def add_processos(self, nova_processos):
    self._processos.append(nova_processos)

  # OUTROS METODOS
  #   
  def num_decisoes(self, dec):
    total = 0
    decisao = ''

    if (dec == True):
      decisao = 'Deferidos'
    else:
      decisao = 'Indeferidos'

    for i in range(len(self._processos)):
      if self._processos[i].get_decisao() == dec:
        total += 1

    return 'O número de processos {} é igual a {}'.format(decisao, total)

  def custo_total(self):
    total = 0
    for i in range(len(self._processos)):
      total += self._processos[i].get_custo().get_valor()
    return f'Custo Total: R$ {total}'

  def custo_total_adv(self, cod_oab):
    # processos > advogado > get_cod_oab comparar com o cod_oab, se for = adicionar na variavel
    total = 0
    for i in range(len(self._processos)):
      if self._processos[i].get_advogado().get_cod_oab() == cod_oab:
        total += self._processos[i].get_custo().get_valor()

    return f'Custo Total do Advogado: R$ {total}'
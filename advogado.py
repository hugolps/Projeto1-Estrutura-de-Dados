class Advogado:

  def __init__(self, cod_oab, nome, processo = []):
    self._cod_oab = cod_oab
    self._nome = nome
    self._processos = processo


  # GETTER AND SETTERS

  def __str__(self):
    processos = ''
    for i in range(len(self._processos)):
      processos += f'{self._processos[i]}\n'
    return f'Inscrição OAB: {self._cod_oab}\nNome: {self._nome}\n\nProcessos: \n{processos}'

  def get_cod_oab(self):
    return self._cod_oab

  def set_cod_oab(self, novo_cod_oab):
    self._cod_oab = novo_cod_oab
    
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

  def lista_clientes(self):
    clientes = []
    for i in range(len(self._processos)):
      clientes.append(self._processos[i].get_pessoa().get_nome())
    return f'Lista de Clientes: {clientes}'

  def custo_total(self):
    total = 0
    for i in range(len(self._processos)):
      total += self._processos[i].get_custo().get_valor()
    return f'Custo Total: R$ {total}'

    
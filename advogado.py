class Advogado:

  def __init__(self, cod_oab, nome, processo = []):
    self._cod_oab = cod_oab
    self._nome = nome
    self._processos = processo


  # GETTER AND SETTERS
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
    
  def set_processos(self, novo_processo):
    self._processos.append(novo_processo)

  # OUTROS METODOS

  def lista_clientes(self):
    clientes = []
    for i in range(len(self._processos)):
      clientes.append(self._processos[i].get_pessoa().get_nome())
    return f'Lista de Clientes: {clientes}'

    
class Processo:
  
  def __init__(self, descricao, custo, decisao, status, pessoa, advogado, audiencia = []):
    self._descricao = descricao
    self._custo = custo
    self._decisao = decisao
    self._status = status
    self._pessoa = pessoa
    self._advogado = advogado
    self._audiencias = audiencia

    # GETTER AND SETTERS

  def get_descricao(self):
    return self._descricao

  def set_descricao(self, nova_descricao):
    self._descricao = nova_descricao

  def get_custo(self):
    return self._custo

  def set_custo(self, novo_custo):
    self._custo = novo_custo

  def get_decisao(self):
      return self._decisao

  def set_decisao(self, nova_decisao):
    self._decisao = nova_decisao

  def get_status(self):
    return self._status

  def set_status(self, novo_status):
    self._status = novo_status

  def get_pessoa(self):
    return self._pessoa

  def set_pessoa(self, nova_pessoa):
    self._pessoa = nova_pessoa

  def get_advogado(self):
    return self._advogado

  def set_advogado(self, novo_advogado):
    self._advogado = novo_advogado

  def get_audiencias(self):
    return self._audiencias

  def set_audiencia(self, nova_audiencia):
    self._audiencias.append(nova_audiencia)

  #OUTROS METODOS

  def audiencias_temp(self, tempo):
    
    for i in self._audiencias:
      lista = []
      if self._audiencias[i].get_duracao() >= tempo:
        lista.append(self._audiencias[i])

    return 'Data da audiencia: {} \nLista de Audiencia com tempo igual ou maior '.format(self.get_audiencias.get_data(), lista)


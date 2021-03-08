class Processo:
  
  def __init__(self, descricao, custo, decisao, status, pessoa, advogado, cod_proc, audiencia = []):
    self._descricao = descricao
    self._custo = custo
    self._decisao = decisao
    self._status = status
    self._pessoa = pessoa
    self._advogado = advogado
    self._cod_proc = cod_proc
    self._audiencias = audiencia



  def __str__(self):
    aud = ''
    for i in range(len(self._audiencias)):
      aud += f'  {self._audiencias[i]}\n'
    return f'Código do Processo: {self._cod_proc}\nDescrição: {self._descricao}\nCusto: R$ {self._custo.get_valor()}\nDecisão: {self._decisao}\nStatus: {self._status}\nPessoa: {self._pessoa.get_nome()}\n CPF: {self._pessoa.get_cpf()}\nAdvogado: {self._advogado.get_nome()}\n {self._advogado.get_cod_oab()}\nAudiencia: \n{aud}' 

    # GETTER AND SETTERS

  def get_cod_proc(self):
    return self._cod_proc
  
  def set_cod_proc(self, novo_cod_proc):
    self._cod_proc = novo_cod_proc

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
    self._audiencias = nova_audiencia

  def add_audiencia(self, nova_audiencia):
    self._audiencias.append(nova_audiencia)


  # def add_audiencia(self, audiencia):

  #OUTROS METODOS

  def audiencias_temp(self, tempo):
    lista = []
    for i in range(len(self._audiencias)):
      if self._audiencias[i].get_duracao() >= tempo:
        lista.append([self._audiencias[i].get_data(), self._audiencias[i].get_recomendacao()])
    
    # if len(lista) != 0:
    return f'Lista de Audiências com tempo igual ou maior: {lista} '

  def lista_audiencias(self):
    aud = ''
    for i in range(len(self._audiencias)):
      aud += f'  {self._audiencias[i]}\n'
    return aud
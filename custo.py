class Custo:
  
  def __init__(self, data, descricao, valor, cod_custo):
    self._data = data
    self._descricao = descricao
    self._valor = valor
    self._cod_custo = cod_custo

  def get_cod_custo(self):
      return self._cod_custo

  def set_cod_custo(self, novo_cod_custo):
    self._cod_custo = novo_cod_custo

  def __str__(self):
    return f'Data: {self._data} Descrição: {self._descricao} Valor: {self._valor}'
  
  def get_data(self):
    return self._data
	
  def set_data(self, nova_data):
    self._data = nova_data
    
  def get_descricao(self):
    return self._descricao
    
  def set_descricao(self, nova_descricao):
    self._descricao = nova_descricao
    
  def get_valor(self):
    return self._valor
    
  def set_valor(self, nova_valor):
    self._valor = nova_valor
  

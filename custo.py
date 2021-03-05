class Custo:
  
  def __init__(self, data, descricao, valor):
    self._data = data
    self._descricao = descricao
    self._valor = valor
  
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
class Audiencia:

  def __init__(self, data, recomendacao, duracao, cod_aud):
    self._data = data
    self._recomendacao = recomendacao
    self._duracao = duracao
    self._cod_aud = cod_aud
  

  # GETTER AND SETTERS

  def __str__(self):
    return f'Código da Audiência: {self._cod_aud}\nData: {self._data}\nRecomendação: {self._recomendacao}\nDuração: {self._duracao}'
  
  def get_data(self):
    return self._data
    
  def set_data(self, nova_data):
    self._data = nova_data
    
  def get_recomendacao(self):
    return self._recomendacao

  def set_recomendacao(self, nova_recomendacao):
    self._recomendacao = nova_recomendacao
    
  def get_duracao(self):
    return self._duracao
    
  def set_duracao(self, nova_duracao):
    self._duracao = nova_duracao

  def get_cod_aud(self):
    return self._cod_aud
      
  def set_cod_aud(self, nova_cod_aud):
    self._cod_aud = nova_cod_aud


#OUTRO METODOS


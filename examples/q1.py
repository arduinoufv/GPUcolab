from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import random 


def questao_aleatorio_lista(l,cabecalho=""):
  x = random.randrange(len(l))
  print(cabecalho+l[x][0]+"?")
 
  def op(resposta):
    if (resposta== l[x][1]):
      return "Correto !"
    else: 
      return "Tente novamente !"  

  interact(op,resposta="digite sua resposta")
cabecalho = "Na linguagem C, qual o símbolo para o operator "

# lista de pares questao/resposta
l = [ ["and","&"],["or","|"], ["xor","^"] ] 

questao_aleatorio_lista(l,cabecalho)

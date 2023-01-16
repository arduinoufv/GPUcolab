from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import random 


def random_quiz_list(l,head=""):
  x = random.randrange(len(l))
  print(head+l[x][0]+"?")
 
  def op(answer):
    if (answer== l[x][1]):
      return "Well done !"
    else: 
      return "Try again !"  

  interact(op,answer="^")

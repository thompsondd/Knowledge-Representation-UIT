from typing import *
import sys
sys.path.append(".")

from backend.parse_query import *
from backend.elements import *
import os

class Manage_Circuit:
  def __init__(self, input_rela, input_value):
    self.value_list = ParseValue(input_value)
    self.info_rela = ParseRela(input_rela)
    self.rela_list = None
    self.validation_condition = {
        "P":[("V"),("E")],
        "S":[("V"),("E")],
        "V":[("O","C")],
        "E":[("O","C")],
    }
    self. rules = {
        "S":self.create_Series,
        "OC":self.package,
        "P": self.create_Parallel
    }
    self.parse()

  def get_R(self) -> float:
    return self.rela_list.get_R()

  def get_draw(self) -> Tuple[schemdraw.Drawing,str]:
    s,e,l,d = self.rela_list.get_draw()
    m = schemdraw.Drawing()
    m+=elm.Dot()
    m+=elm.ElementDrawing(d)
    m+=elm.Dot()
    path = os.path.join(os.getcwd(),"frontend/images/plot_circuit.png")
    m.save(path)
    #print(f"path: {path}")
    return m, path

  def create_relation(self, type_relation:Union[Series,Parallel], label1:str, label2:str,*arg) -> Union[Series,Parallel,None]:
    temp = {}
    for i in self.value_list.data:
      #print(f"\t\t\t\t\tRi: {i.label}")
      if label1 == i.label:
        temp.update({"0":i})
      if label2 == i.label:
        temp.update({"1":i})
    #print(f"\t\t\t\ttemp: {temp}")
    #print(f"\t\t\t\trela_list: {self.rela_list}")
    if self.rela_list == None and len(list(temp.keys()))<2:
      print("Error 1")
    if len(list(temp.keys()))<2:
      if self.rela_list.label == label1:
        self.rela_list = type_relation(self.rela_list,*list(temp.values()))
        return self.rela_list
      elif self.rela_list.label == label2:
        self.rela_list = type_relation(*list(temp.values()),self.rela_list)
        return self.rela_list
      else:
         print("Error 2")
    if self.rela_list == None:
      #print(f"aaaaa: {type_relation.__name__}")
      self.rela_list = type_relation(*list(temp.values()))
      return self.rela_list
    else:
      tt = type_relation(*list(temp.values()))
      self.value_list.data.append(tt)
      return tt
      #print(f"Error 3:\n\trela_list:{self.rela_list}\n]\ttemp:{temp}")
  
  def create_Series(self,label1:str, label2:str,*arg) -> Union[Series,Parallel,None]:
    #print(f"\t\t\tcreate_Series:{[label1, label2,*arg]}")
    return self.create_relation(Series, label1, label2)

  def create_Parallel(self, label1:str, label2:str,*arg) -> Union[Series,Parallel,None]:
    #print(f"\t\t\tcreate_Parallel:{[label1, label2,*arg]}")
    return self.create_relation(Parallel,label1, label2)

  def package(self,*arg) -> Union[Series,Parallel,None]:
    #print(f"\t\t\tpackage:{[*arg]}")
    if self.rela_list.label == arg[-1]:
      return self.rela_list
    for i in self.value_list.data:
      if i.label==arg[-1]:
        return i

  def validate(self,list_ele:List[Tuple[str,str]]) -> Tuple[bool,Union[str,None]]:
    alpha = ["O","C"]
    beta = ["E","V"]
    a,b,c = list_ele
    if b[1] in ["P","S"]:
      return a[1] in beta and c[1] in beta,b[1]
    elif b[1] in ["V","E"]:
      return (a[1]==alpha[0] and c[1]==alpha[1],"OC")
    return False,None

  def identify_rela(self, list_ele:List[Tuple[str,str]])-> Union[Tuple[str,str],None]:
    #print(f"\t\tidentify_rela:{list_ele}")
    check, type_rela = self.validate(list_ele)
    #print(f"\t\tcheck:{check}")
    #print(f"\t\ttype_rela:{type_rela}")
    if check:
      a,b,c = list_ele
      d = self.rules[type_rela](a[0],c[0],b[0])
      #print(f"\t\t\td: {d}")
      if d!=None:
        return (d.label,"E")
    return None

  def parse(self) -> None:
    t = [i for i in self.info_rela.lex()]
    #print(f"Manage_Circuit parsed: {t}")
    if len(t)==1:
      for i in self.value_list.data:
        if i.label==t[0][0]:
          self.rela_list = i
          return 0
    index = 0
    while index < len(t):
      index+=1
      if index<3:
        continue
      #print(f"index: {index}")
      start = index-3
      while start>-1:
        #print(f"t: {t}")
        #print(f"\tparse:{t[start:start+3]} - start: {start}")
        a = self.identify_rela(t[start:start+3])
        if a!=None:
          for _ in range(3):
            t.pop(start)
            index -=1
          t.insert(start,a)
          start = index
        start -=1
    #print(f"t: {t}")

#circuit = "R1+R2+(R3*(R4+R5+R6))"
#value_circuit="R1=3,R2=4,R3=5,R4=6,R5=5,R6=7"
#print(Manage_Circuit(circuit,value_circuit).get_R())
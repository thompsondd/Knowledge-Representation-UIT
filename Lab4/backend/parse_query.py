import sys
sys.path.append("..")
from backend.elements import Resistor

class DATA:
  def __init__(self,data):
    self.__data=data
    self.__len=len(data)
    self.__index=-1
  
  def next_char(self):
    if self.__index+1<self.__len:
      return self.__data[self.__index+1]
    return None

  def getNextChar(self):
    self.__index+=1
    if self.__index>=self.__len:
      return None
    return self.__data[self.__index]
    
class ParseRela:
  def __init__(self,data):
      self.data = data
  def _lex(self):
    self.Dataset =  DATA(self.data)
    while self.Dataset.next_char() is not None:
      c=self.Dataset.getNextChar()
      if c==" ":
        continue
      elif c in ["(",")","+","*"]:
        dk = {"+":"S","*":"P","(":"O",")":"C"}
        yield((c,dk[c]))
      elif c=="R":
        id = ""
        check = self.Dataset.next_char()
        while check !=None and check.isalnum():
          id += self.Dataset.getNextChar()
          check =  self.Dataset.next_char()
        yield((c+id,"V"))
      else:
        raise Exception("Unrecognised character: '" + c + "'.")  
  def lex(self):
    tokens= [ i for i in self._lex()]
    return tokens

class ParseValue:
  def __init__(self, data):
    self.origin_data = data
    self.process()
  def process(self):
    temp_data = [i.split("=") for i in self.origin_data.split(",")]
    self.data=[]
    for label, value in temp_data:
      self.data.append(Resistor(label,float(value)))
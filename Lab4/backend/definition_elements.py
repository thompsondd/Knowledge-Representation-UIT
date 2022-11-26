import schemdraw
import schemdraw.elements as elm
elm.style(elm.STYLE_IEC)

class Resistor:
    def __init__(self, label, value):
        self.label = label
        self.value = value
    def get_R(self):
        return self.value
    def __str__(self):
      return self.label
    def __repr__(self):
      return self.label
    @property
    def __name__(self):
      return "Resistor"
    def get_draw(self):
      try:
        #print(f"{self.label}")
        d = schemdraw.Drawing(show=False)
        S = elm.Resistor(label=self.label)
        d += S
        u = S.end-S.start
        length = np.sqrt(np.sum(u.x*u.x+u.y*u.y))
        #d.here = S.start
        return S.start, S.end, length, d
      except Exception as e:
        print(f"Error: {self.label}")
        raise e


class AbsCircuit:
  def __init__(self, circuit1, circuit2):
    self.c1 = circuit1
    self.c2 = circuit2
    self.label = self.c1.label + self.c2.label
  def get_R(self):
    pass
  def __str__(self):
    return self.label 
  def __repr__(self):
    return self.label


class Series(AbsCircuit):
  @property
  def __name__(self):
      return "Series"
  def get_R(self):
      return self.c1.get_R()+self.c2.get_R()
  def get_draw(self):
    try:
      s1, e1, l1, d1 = self.c1.get_draw()
      s2, e2, l2, d2 = self.c2.get_draw()
      d = schemdraw.Drawing(show=False)

      d += elm.ElementDrawing(d1)
      x,y = d.here
      d.here = schemdraw.util.Point((x-s2.x,y-e2.y))
      d += elm.ElementDrawing(d2)
      u = d.here-s1
      length = np.sqrt(np.sum(u.x*u.x+u.y*u.y))
      return s1, d.here, length, d
    except Exception as e:
      print(f"Error: {self.label}")
      raise e

class Parallel(AbsCircuit):
  @property
  def __name__(self):
      return "Parallel"
  def get_R(self):
      return 1/(1/self.c1.get_R()+1/self.c2.get_R())
  def get_draw(self):
    try:
      s1, e1, l1, d1 = self.c1.get_draw()
      s2, e2, l2, d2 = self.c2.get_draw()
      if l2>l1:
        s3, e3, l3, d3 = s2, e2, l2, d2
        s2, e2, l2, d2 = s1, e1, l1, d1
        s1, e1, l1, d1 = s3, e3, l3, d3
      d = schemdraw.Drawing(show=False)
      S = elm.Line()
      d += S

      length_l = d.unit/4
      x1min,y1min,x1max,y1max = d1.get_bbox()
      x2min,y2min,x2max,y2max = d2.get_bbox()

      ul1 = elm.Line().up().length((y1max-y1min)/2+length_l)
      d+=ul1
      d += elm.ElementDrawing(d1).right()
      d += elm.Line().down().length((y1max-y1min)/2+length_l)

      E = elm.Line().right()
      d+=E
      d.here = E.start
      d+=elm.Line().down().length((y2max-y2min)/2+length_l)
      d += elm.ElementDrawing(d2).left()
      
      d+= elm.Line().tox(S.end)
      d += elm.Line().toy(S.end)

      d.here = E.end
      u = E.end - S.start
      length = np.sqrt(np.sum(u.x*u.x+u.y*u.y))

      return S.start, E.end, length, d
    except Exception as e:
      print(f"Error: {self.label}")
      raise e

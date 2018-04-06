from math import sin, cos, pi
class Figura():
    def __init__(self, dimension, lados, color, colorC, letra):
        self.colorF = color
        self.colorC = colorC
        self.letra = chr(letra)
        self.id=letra-65
        self.dimension = dimension
        self.lados = lados
        self.es = "d"+str(dimension)+"l"+str(lados)
        self.rot = (15*self.lados-15)*pi/180
        self.angulo = 2*pi/self.lados
        self.coord = [{'x':round(cos(x*self.angulo+self.rot),2),'y':round(sin(x*self.angulo+self.rot),2)} for x in range(1,self.lados+1)]
if __name__ == "__main__":
    figura = Figura(2,3,"lol","lol",1)
    print(figura.__dict__)

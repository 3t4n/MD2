from random import *
from core.Figura import *
import json
import boolean

class Mundo():
    def __init__(self,x,y,coloresC,coloresF, dimensiones,lados, porcentaje):
        self.algebra = boolean.BooleanAlgebra()
        self.tablero = []
        self.preguntas = []
        self.clases = []
        self.figuras = ['x']
        self.propiedades = ["colorF","colorC","es"]
        self.conectores = ["||","&&"]
        self.x = x
        self.y = y
        self.coloresC = coloresC
        self.coloresF = coloresF
        self.numero = self.x * self.y * porcentaje/100
        self.i = 65
        for i in range(0,x):
            temp = []
            for j in range(0,y):
                choicer = randrange(100)+1
                if(choicer<porcentaje):
                    d = randrange(2,dimensiones+1)
                    l = randrange(3,lados+1)
                    self.clases.append('d'+str(d)+'l'+str(l))
                    self.figuras.append(chr(self.i))
                    colorF = choice(coloresF)
                    colorC = choice(coloresC)
                    temp.append(Figura(d,l,colorF,colorC,self.i).__dict__)
                    self.i+=1
                    continue
                temp.append({})
            self.tablero.append(temp)

    def obtenerMundo(self):
        prejson = dict({'preguntas':self.preguntas,'mundo':self.tablero})
        return json.dumps(prejson)

    def valorPropiedad(self,x):
        return {"colorF":choice(self.coloresF),"colorC":choice(self.coloresC),"es":choice(self.clases)}[x]

    def valorCuantificador(self,x):
        return {True:"∀",False:"∃"}[x]
    
    def valorNegacion(self,x):
        return {True:"¬",False:""}[x]

    def generarEnunciados(self, cantidad, sub):
        tempEnunciados = []
        id = 0
        for i in range(0,cantidad):
            temp = ""
            tokenN = choice([True, False])
            tokenC = choice([True, False])
            tokenClase = choice(self.clases)
            tempEnunciado = self.valorNegacion(tokenN)+self.valorCuantificador(tokenC)+ "x,"
            subP = randrange(sub)
            valorEnunciado=not(tokenC)
            for j in range(0,subP+1):
                tokenNs = choice([True, False])
                tokenPropiedad= choice(self.propiedades)
                valorPropiedad = self.valorPropiedad(tokenPropiedad)
                tokensubclase = choice(self.figuras)
                conector = choice(self.conectores)
                tempEnunciado = tempEnunciado + self.valorNegacion(tokenNs)+ tokenPropiedad +"("+valorPropiedad+","+tokensubclase+")"+ ("" if j==subP else conector)
                valorsubEnunciado = tokenC 
                for row in self.tablero:
                    for figura in row:
                        if(any(figura)):
                            if(figura['letra']==tokensubclase):
                                valorsubEnunciado = (figura[tokenPropiedad]==valorPropiedad)
                                break
                            else: 
                                if('x'==tokensubclase):
                                    valorsubEnunciado =(figura[tokenPropiedad]==valorPropiedad) and valorsubEnunciado if tokenC else (figura[tokenPropiedad]==valorPropiedad) or valorsubEnunciado
                valorsubEnunciado = not(valorsubEnunciado) if tokenNs else valorsubEnunciado
                valorsubEnunciado = not(valorsubEnunciado) if tokenN else valorsubEnunciado
                temp = temp + str(valorsubEnunciado) + ("" if j==subP else conector)
            ##print(temp+"\n")
            valorEnunciado =  str(not(bool(self.algebra.parse(temp).simplify())) if 'x'==tokensubclase else bool(self.algebra.parse(temp).simplify())) 
                
                #print(str(tokenNs)+ " "+tokenPropiedad +" "+ valorPropiedad +" " + figura[tokenPropiedad]  + " " + figura['letra'] + " " + tokensubclase + " " + str(valorsubEnunciado))

            tempEnunciados.append({'id':id, 'string':tempEnunciado, 'res':str(valorEnunciado)})
            id+=1
            self.preguntas = tempEnunciados
                



#test = Mundo(2,2,["black","green"],["black","green"],2,8,70)
#test.generarEnunciados(4,5)
#test.obtenerMundo()

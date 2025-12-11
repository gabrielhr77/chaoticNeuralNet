'''
Docstring for sim2Body2D

o estado t da simulação será t=[x1,y1,dx1,dy1,x2,y2,dx2,dy2], sendo as posições e velocidades dos dois corpos 

vou usar primeiro RK4 para validar o modelo com dados reais, depois uso o Leapfrog para gerar a simulação de longo prazo

como expresso as leis da gravitação em EDOs de segunda ordem, vou reescrevê-las em primeira ordem e aplicar o RK4


'''

import numpy as np
import matplotlib.pyplot as plt


#definição das variáveis no SI

G = 6.6743e-11 # m³kg-¹s-²
Rt=6371000 # m
Rl=1737400 # m 

def plotar(fig,r=Rt):
	x = np.linspace(-1,1,1000)
	yp = np.sqrt(r**2 - x**2)
	yn = -1*np.sqrt(r**2 - x**2)
	fig.plot(x,yp,color="black")
	fig.plot(x,yn,color="black")

def colisao(x1,y1,x2,y2): # verifica se a terra bateu na lua, se colidiu retorna true
    return ((np.sqrt(x1**2+y1**2)+Rt)+(np.sqrt(x2**2+y2**2)+Rl)<=Rt+Rl)


import numpy as np
import matplotlib.pyplot as plt
import math as mt
import pylab as pl


# definição das variáveis no SI

G = 6.6743e-11 # m³kg-¹s-²
Rt=6371000 # m
Rl=1737400
Ms=1.989e30 # kg
Mt=5.972e24
posT_X=1.496e11 # m do centro (SOL)
posT_Y=0
velT_X=0 # m/s
velT_Y=2.97e4 # aqui a velocidade é tangencial à linha que conecta a Terra ao Sol para que o movimento seja de órbita real e não um afastamento descontrolado

# valores da simulação no início (variáveis)
xT0=posT_X
yT0=posT_Y
vxT0=velT_X
vyT0=velT_Y
xS0=0
yS0=0
vxS0=0
vyS0=0

# valores constantes durante a simulação (invariáveis)
ti=0 # início da simulação
tf=365 # final da simulação (dias)
passosMin=525600 # minutos EM UM ANO
passosHoras=8760
passosDias=365

"""
x # POSIÇÃO X

y # POSIÇÃO Y

dx/dt = vx # VELOCIDADE X

dy/dt = vy # VELOCIDADE Y

dvx/dt = -GMs(x/((x**2 + y**2)**3/2)) # ACELERAÇÃO X

dvy/dt = -GMs(y/((x**2 + y**2)**3/2)) # ACELERAÇÃO Y
"""
# S=[
#    xT,yT,vxT,vyT,
#    xS,yS,vxS,vyS
# ]
S0=np.array([xT0,yT0,vxT0,vyT0,xS0,yS0,vxS0,vyS0])

def f(S,t):
	xT,yT,vxT,vyT,xS,yS,vxS,vyS=S
	dx=xT-xS
	dy=yT-yS

	axT=-G*Ms(dx/((dx**2 + dy**2)**3/2))
	ayT=-G*Ms(dy/((dx**2 + dy**2)**3/2))

	axS=+G*Mt(dx/((dx**2 + dy**2)**3/2))
	ayS=+G*Mt(dy/((dx**2 + dy**2)**3/2))

	return np.array([
		vxT,vyT,axT,ayT,vxS,vyS,axS,ayS
	])

def rk4(f,S0,ti,tf,n):
	'''
	f é função derivada f(S,t)
	S0 é condição inicial
	ti e tf é intevalo de integração
	n é o número de passos
	'''
	S=np.zeros((n+1,len(S0)))  # cria uma matriz onde cada linha é o estado no instante k
	
	t=np.zeros(n+1) # guarda os tempos
	
	S[0]=S0
	t[0]=ti
	h=float(tf-ti)/n #passo da integração

	for k in range(n):
		t[k+1]=t[k]+h
		k1=h*f(S[k],t[k])
		k2=h*f(S[k]+0.5*h*k1,t[k]+0.5*h)
		k3=h*f(S[k]+0.5*h*k2,t[k]+0.5*h)
		k4=h*f(S[k]+h*k3,t[k]+h)
		S[k+1]=S[k]+h*(k1+2*k2+2*k3+k4)/6
	return S,t # entrega a matriz com soluções




'''


#definição do escopo da função
inicio=0.0
fim=10.0
N=1000
passo=(fim-inicio)/N
aux=0.0

#vetor dos pontos
v1=np.arange(inicio,fim,passo)

def funcao1(x,t):
    return -x**3 + mt.sin(t)

def plotar(fig,r=Rt):
	x = np.linspace(-1,1,1000)
	yp = np.sqrt(r**2 - x**2)
	yn = -1*np.sqrt(r**2 - x**2)
	fig.plot(x,yp,color="black")
	fig.plot(x,yn,color="black")

def colisao(x1,y1,x2,y2): # verifica se a terra bateu na lua, se colidiu retorna true
    return ((np.sqrt(x1**2+y1**2)+Rt)+(np.sqrt(x2**2+y2**2)+Rl)<=Rt+Rl)

def euler1(v1):
	v2=v1
	v3=[]
	for t in v2:
		v3.append(aux)
		aux+=passo*funcao1(aux,t)
	print("EULER")
	pl.plot(v2,v3)
	pl.xlabel("t")
	pl.ylabel("x(t)")
	pl.show()
    

"""
sistema de EDOs
dx/dt=fx(x,y,t)
dy/dt=fy(x,y,t)

aplicando o metodo de euler nas edos
xi+1=xi + h fx(xi,yi,ti)
yi+1=yi + h fy(xi,yi,ti)

resolvo essas equações em ti antes de procurar resolver para ti+1


"""

def euler2(f,S0,ti,tf,n):
	t=np.zeros(n+1)
	S=np.zeros((n+1,len(S0)))
	S[0]=S0
	t[0]=ti
	h=float(tf-ti)/n
	for k in range(n):
		t[k+1]=t[k]+h
		S[k+1]=S[k]+h*f(S[k],t[k])
	return S,t
def f(S,t):
	v0x=5.;v0y=10.;ax=2.
	return np.array([v0x-ax*t,v0y-S[0]*t])
ti=0.
tf=4.
S0=np.array([0,15])
n=10
S1,t1=euler2(f,S0,ti,tf,n)

"""
x # POSIÇÃO X

y # POSIÇÃO Y

dx/dt = vx # VELOCIDADE X

dy/dt = vy # VELOCIDADE Y

dvx/dt = -GMs(x/((x**2 + y**2)**2/3)) # ACELERAÇÃO X

dvy/dt = -GMs(y/((x**2 + y**2)**2/3)) # ACELERAÇÃO Y
"""
def atualizaVelocidade(posX,posY):
	



def rk4(v1):
	v2=v1
	v3=[]
	for t in v2:
		v3.append(aux)
		k1=passo*funcao1(aux,t)
		k2=passo*funcao1(aux+0.5*k1,t+0.5*passo)
		k3=passo*funcao1(aux+0.5*k2,t+0.5*passo)
		k4=passo*funcao1(aux+k3,t+passo)
		x+=(k1+2*k2+2*k3+k4)/6
	print("RK4")
	pl.plot(v2,v3)
	pl.xlabel("t")
	pl.ylabel("x(t)")
	pl.show()




	"""
	
	preciso ter posição e velocidade terra e lua iniciais
	
	atuaizar posição a partir da velocidade

	"""

'''

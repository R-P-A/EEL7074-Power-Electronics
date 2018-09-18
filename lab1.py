# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

Vp = 110*np.sqrt(2)
L = 0.5
R = 75
w = 2*np.pi*60
i0 = 0
phi = np.arctan(w*L/R)

def current_rl_diode(Vp, L, R, w, i0, t):
    if ((w*t) < np.pi):
        return (Vp*w/L)*((np.exp(-t*R/L)/((R/L)**2 + w**2)) + (np.sin(w*t-phi)/(w*np.sqrt((R/L)**2 + w**2)))) + i0*np.exp(-t*R/L)
    else:
        i0 = (Vp*w/L)*((np.exp(-(np.pi/w)*R/L)/((R/L)**2 + w**2)) + (np.sin(np.pi-phi)/(w*np.sqrt((R/L)**2 + w**2)))) + i0*np.exp(-(np.pi/w)*R/L)
        return i0*np.exp(-(t-np.pi/w)*R/L)

    
t = np.linspace(0.0, 3/60, 1200)
graph = np.zeros(len(t))
for i in range(0, 400):
    graph[i] = current_rl_diode(Vp, L, R, w, i0, t[i])
for i in range(0, 400):
    graph[i+400] = current_rl_diode(Vp, L, R, w, graph[399], t[i])
for i in range(0, 400):
    graph[i+800] = current_rl_diode(Vp, L, R, w, graph[799], t[i])
    
plt.rcParams['figure.figsize'] = [15, 10]
plt.plot(t, graph, label='Corrente na Carga')
plt.plot(t, 1.1*np.sqrt(2)*np.sin(w*t), label='Tensão na Entrada Dividido por 100')
plt.xlabel('t (s)')
plt.ylabel('Ic (A)                Vin/100 (V)')
plt.title("Retificador de Meia Onda com Carga RL e com Diodo de Roda-Livre")
plt.legend()
plt.grid(True)
plt.show()
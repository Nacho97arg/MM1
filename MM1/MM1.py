from Experimento import *

tamanioCola=99
tasaArribo = 1
tasaPartida = 1

experimentos=[]

for i in range(10):
    experimentos.append(experimento(0,0,tasaArribo,tasaPartida,tamanioCola))

for i in range(10):
    experimentos[i].ejecutar()


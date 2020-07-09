from Experimento import *
import matplotlib.pyplot as plt

tamanioCola=0
tasaArribo = 1
tasaPartida = 1

experimentos=[]

promClientesSistema=0
promClientesCola=0
tiempoPromEnSistema=0
tiempoPromEnCola=0
utilizacionServidorProm=0
promProbClientesCola=0
promProbDenegacionServ=0

for i in range(10):
    experimentos.append(experimento(0,0,tasaArribo,tasaPartida,tamanioCola,100))

for i in range(10):
    print("Ejecutando experimento",i)
    experimentos[i].ejecutar()
    promClientesSistema+=experimentos[i].get_PromClientesEnSistema()
    promClientesCola+=experimentos[i].get_PromClientesEnCola()
    tiempoPromEnSistema+=experimentos[i].get_TiempoPromEnSistema()
    tiempoPromEnCola+=experimentos[i].get_TiempoPromEnCola()
    utilizacionServidorProm+=experimentos[i].get_UtilizacionServidor()
    promProbClientesCola+=experimentos[i].get_ProbNClientesCola(0)
    promProbDenegacionServ+=experimentos[i].get_ProbDenegacionServicio()

    if i == 9:
        promClientesSistema=promClientesSistema/10
        promClientesCola=promClientesCola/10
        tiempoPromEnSistema=tiempoPromEnSistema/10
        tiempoPromEnCola=tiempoPromEnCola/10
        utilizacionServidorProm=utilizacionServidorProm/10
        promProbClientesCola=promProbClientesCola/10
        promProbDenegacionServ=promProbDenegacionServ/10








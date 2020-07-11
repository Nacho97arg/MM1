from Experimento import *
import matplotlib.pyplot as plt

tamanioCola=0
tasaArribo = 0.25
tasaPartida = 1

experimentos=[]

promClientesSistema=[0,0,0,0,0]
promClientesCola=[0,0,0,0,0]
tiempoPromEnSistema=[0,0,0,0,0]
tiempoPromEnCola=[0,0,0,0,0]
utilizacionServidorProm=[0,0,0,0,0]
promProbClientesCola=[0,0,0,0,0]
promProbDenegacionServ=[0,0,0,0,0]

def switch(i):
    switcher={
                0:0,
                1:2,
                2:5,
                3:10,
                4:50
             }
    return switcher.get(i)

def graficas(x1,y1,y1lim,y2,y2lim,y3,y3lim,suptitle,subt1,subt2,subt3,xlabel):
    fig=plt.figure(figsize=(9, 4))
    #plt.xlim(xlimMin,xlimMax)
    #plt.ylim(0,ylimMax)
    #plt.axis([xlimMin,xlimMax,ylimMin,ylimMax])
    ax1=plt.subplot(131)
    ax1.set_title(subt1)
    ax1.grid(True)
    ax1.set_ylim(0,y1lim)
    ax1.set_xlabel(xlabel)
    plt.bar(x1, y1)
    ax2=plt.subplot(132)
    ax2.set_title(subt2)
    ax2.grid(True)
    ax2.set_ylim(0,y2lim)
    ax2.set_xlabel(xlabel)
    plt.bar(x1, y2)
    ax3=plt.subplot(133)
    ax3.set_title(subt3)
    ax3.grid(True)
    ax3.set_ylim(0,y3lim)
    ax3.set_xlabel(xlabel)
    plt.bar(x1, y3)
    plt.suptitle(suptitle)
    plt.show()

for x in range(5):
    tamanioCola = switch(x)
    for i in range(10):
        experimentos.append(experimento(0,0,tasaArribo,tasaPartida,tamanioCola,100))
    for i in range(10):
        print("Ejecutando experimento",i)
        experimentos[i].ejecutar()
        promClientesSistema[x]+=experimentos[i].get_PromClientesEnSistema()
        promClientesCola[x]+=experimentos[i].get_PromClientesEnCola()
        tiempoPromEnSistema[x]+=experimentos[i].get_TiempoPromEnSistema()
        tiempoPromEnCola[x]+=experimentos[i].get_TiempoPromEnCola()
        utilizacionServidorProm[x]+=experimentos[i].get_UtilizacionServidor()
        promProbClientesCola[x]+=experimentos[i].get_ProbNClientesCola(0)
        promProbDenegacionServ[x]+=experimentos[i].get_ProbDenegacionServicio()
        if i == 9:
            promClientesSistema[x]=promClientesSistema[x]/10
            promClientesCola[x]=promClientesCola[x]/10
            tiempoPromEnSistema[x]=tiempoPromEnSistema[x]/10
            tiempoPromEnCola[x]=tiempoPromEnCola[x]/10
            utilizacionServidorProm[x]=utilizacionServidorProm[x]/10
            promProbClientesCola[x]=promProbClientesCola[x]/10
            promProbDenegacionServ[x]=promProbDenegacionServ[x]/10
    experimentos=[]

graficas(['0','2','5','10','50'],promProbDenegacionServ,1,tiempoPromEnCola,40,promClientesCola,35,'Variacion de longitud de la cola','Probabilidad Denegacion Servicio','Tiempo en cola','Nro clientes en cola','Tamaño cola')
graficas(['0','2','5','10','50'],promClientesSistema,10,tiempoPromEnSistema,10,utilizacionServidorProm,1,'Variacion de longitud de la cola','Nro Clientes en sistema','Tiempo promedio en sistema','Utilizacion del Servidor','Tamaño cola')    








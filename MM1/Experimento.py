from Cliente import *
from numpy import random
class experimento(object):
    """description of class"""

    clientesAProcesar=5

    def __init__(self, tiempo, estadoServidor, tasaArribo, tasaPartida, tamanioMaxCola):
        self.tiempo = 0
        self.lineaTemporal = [0]
        self.estadoServidor = [0]
        self.clienteSiendoAtendido = None
        self.tasaArribo=tasaArribo
        self.tasaPartida=tasaPartida
        self.tamanioMaxCola=tamanioMaxCola
        self.cola = []
        self.enCola = [0]
        self.clientePorArribar = None
        self.clientesProcesados = 0
        self.clientesRechazados = 0

    def ejecutar(self):
        #Llamadas a rutinas de arribo, partida, etc
        print("Ejecutado")
        while(self.clientesProcesados<self.clientesAProcesar):
            self.pasoTiempo()
    
    def pasoTiempo(self):
        if self.tiempo == 0:
            self.clientePorArribar=Cliente(random.exponential(scale=self.tasaArribo), random.exponential(scale=self.tasaPartida))
            self.tiempo=self.clientePorArribar.tiempoArribo
            self.lineaTemporal.append(self.tiempo)
            self.arribo()
        else:
            try:
                if (self.tiempo+self.clienteSiendoAtendido.tiempoPartida)<=(self.tiempo+self.clientePorArribar.tiempoArribo): #Partida
                    self.tiempo=self.clienteSiendoAtendido.tiempoPartida
                    self.lineaTemporal.append(self.tiempo)
                    self.partida()
                else: #Arribo
                    self.tiempo=self.clientePorArribar.tiempoArribo
                    self.lineaTemporal.append(self.tiempo)
                    self.arribo()
            except: #Si el servidor queda vacio y no hay clientes en cola (Arribo obligado)
                self.tiempo=self.clientePorArribar.tiempoArribo
                self.lineaTemporal.append(self.tiempo)
                self.arribo()


    def arribo(self):
        nuevoCliente = Cliente(self.tiempo+random.exponential(scale=self.tasaArribo), random.exponential(scale=self.tasaPartida))
        if self.estadoServidor[self.lineaTemporal.index(self.tiempo)-1]==1: #Si el estado del servidor es ocupado en el tiempo actual
            if len(self.cola)<=self.tamanioMaxCola:
                self.cola.append(self.clientePorArribar)
                self.enCola.append(len(self.cola))
            else:
                self.clientesRechazados+=1
        else: #Si el servidor esta libre
            self.clientePorArribar.demoraCola=0
            self.clienteSiendoAtendido=self.clientePorArribar
            self.estadoServidor.append(1)
            self.enCola.append(0)
        self.clientePorArribar=nuevoCliente

    def partida(self):
        if len(self.cola) == 0:
            self.estadoServidor.append(0)
            self.clienteSiendoAtendido=None
            self.enCola.append(0)
            self.clientesProcesados+=1
        else:
            self.clienteSiendoAtendido=self.cola[0]
            self.cola.remove(self.cola[0])
            self.clientesProcesados+=1
            self.estadoServidor(1)
            self.enCola.append(len(self.cola))












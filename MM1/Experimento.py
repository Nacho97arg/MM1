from Cliente import *
from numpy import random
class experimento(object):
    """Instancia del experimento (corrida)"""

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
        self.clientesProcesados = []
        self.clientesRechazados = 0

    def ejecutar(self): #Llamadas a rutinas de paso de tiempo, analisis de datos, etc
        print("Ejecutado")
        #random.seed(6666)
        while(len(self.clientesProcesados)<self.clientesAProcesar):
            self.pasoTiempo()
    
    def pasoTiempo(self):
        if self.tiempo == 0:
            self.clientePorArribar=Cliente(random.exponential(scale=self.tasaArribo), random.exponential(scale=self.tasaPartida))
            self.tiempo=self.clientePorArribar.tiempoArribo
            self.lineaTemporal.append(self.tiempo)
            self.arribo()
        else:
            try:
                if (self.clienteSiendoAtendido.tiempoPartida)<=(self.clientePorArribar.tiempoArribo): #Partida "Borre self.tiempo+(tiempoPartida/Arribo)"
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
            self.estadoServidor.append(1)
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
        if len(self.cola) == 0: #Cola vacia, servidor pasa a idle
            self.estadoServidor.append(0)
            self.clientesProcesados.append(self.clienteSiendoAtendido)
            self.clienteSiendoAtendido=None
            self.enCola.append(0)            
        else: #Cola no vacia, pasa proximo cliente en cola
            self.clientesProcesados.append(self.clienteSiendoAtendido)
            self.clienteSiendoAtendido=self.cola[0]
            self.clienteSiendoAtendido.set_demoraCola(self.tiempo-self.clienteSiendoAtendido.tiempoArribo)
            self.cola.remove(self.cola[0])
            self.estadoServidor.append(1)
            self.enCola.append(len(self.cola))

    def get_PromClientesEnSistema(self):
        sum = 0
        for i in range(len(self.lineaTemporal)):
            sum += self.enCola[i]+self.estadoServidor[i]
        return sum/len(self.lineaTemporal)

    def get_PromClientesEnCola(self):
        sum = 0
        for c in self.enCola:
            sum += c
        return sum/len(self.enCola)

    def get_TiempoPromEnSistema(self):
        sum = 0
        for c in self.clientesProcesados:
            sum += (c.tiempoPartida-c.tiempoArribo)
        return sum/len(self.clientesProcesados)

    def get_TiempoPromEnCola(self):
        sum = 0
        for c in self.clientesProcesados:
            sum += c.demoraCola
        return sum/len(self.clientesProcesados)

    def get_UtilizacionServidor(self):
        sum = 0
        for e in self.estadoServidor:
            sum += e
        return sum/len(self.estadoServidor)

    def get_ProbNClientesCola(self, n):
        cant = self.enCola.count(n)
        return cant/len(self.clientesProcesados)

    def get_ProbDenegacionServicio(self):
        return self.clientesRechazados/(self.clientesProcesados+self.clientesRechazados)








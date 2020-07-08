class Cliente(object):
    """Entidad cliente del servidor"""
    def __init__(self, tiempoArribo, tiempoPartida):
        self.tiempoArribo=tiempoArribo
        self.tiempoPartida=tiempoArribo+tiempoPartida
        self.demoraCola=None

    def set_tiempoArribo(self, tiempoArribo):
        self.tiempoArribo=tiempoArribo
    def set_tiempoPartida(self, tiempoPartida):
        self.tiempoPartida=tiempoPartida
    def set_demoraCola(self, demoraCola):
        self.demoraCola=demoraCola
        self.tiempoPartida+=self.demoraCola







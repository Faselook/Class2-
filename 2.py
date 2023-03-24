class Transport():
    def __init__(self, speed, oil):
        self._speed = speed
        self._oil = oil

    def setSpeed(self):
        self._speed = input("Enter speed = ")

    def setOil(self):
        self._oil = input("Enter oil = ")

    def getSpeed(self):
        return self._speed
    
    def getOil(self):
        return self._oil
    
    speed = property(getSpeed, setSpeed)
    oil = property(getOil, setOil)

    def out(self):
        print(self.speed, self.oil)

class LandTr(Transport):
    def __init__(self, speed, oil, model):
        super().__init__(speed, oil)
        self._model = model

    def setModel(self):
        self._model = input("Enter model = ")
    
    def getModel(self):
        return self._model

    model = property(getModel, setModel)

    def out(self):
        print(self.speed, self.oil, self.model)

class AirTr(Transport):
    def __init__(self, speed, oil, marka):
        super().__init__(speed, oil)
        self._marka = marka

    def setMarka(self):
        self._marka = input("Enter marka = ")
    
    def getMarka(self):
        return self._marka

    marka = property(getMarka, setMarka)

    def out(self):
        print(self.speed, self.oil, self.marka)

class WTr(Transport):
    def __init__(self, speed, oil, tonage):
        super().__init__(speed, oil)
        self._tonage = tonage

    def setTonage(self):
        self._marka = input("Enter tonage = ")
    
    def getTonage(self):
        return self._tonage

    tonage = property(getTonage, setTonage)

    def out(self):
        print(self.speed, self.oil, self.tonage)

class Auto(LandTr):
    def __init__(self, speed, oil, model, color):
        super().__init__(speed, oil, model)
        self._color = color

    def setColor(self):
        self._color = input("Enter color = ")
    
    def getColor(self):
        return self._color

    color = property(getColor, setColor)

    def out(self):
        print(self.speed, self.oil, self.model, self.color)

class Airplane(AirTr):
    def __init__(self, speed, oil, marka, pas):
        super().__init__(speed, oil, marka)
        self._pas = pas

    def setPas(self):
        self._pas = input("Enter pas = ")
    
    def getPas(self):
        return self._pas

    pas = property(getPas, setPas)

    def out(self):
        print(self.speed, self.oil, self.marka, self.pas)

class Ship(WTr):
    def __init__(self, speed, oil, tonage, type):
        super().__init__(speed, oil, tonage)
        self._type = type

    def setType(self):
        self._type = input("Enter type = ")
    
    def getType(self):
        return self._type

    type = property(getType, setType)

    def out(self):
        print(self.speed, self.oil, self.tonage, self.type)

# listTr = [Transport(speed, oil), LandTr(56, "92", "E54"), AirTr(304, "90", "R72MU"), WTr(678, "8732", "fyjhfd"), Auto(34, "78", "YB56", "red"), Airplane(567, "7834", "KD*^TDK", "86"), Ship(923, "978", "LGV^", "jlfl")]

# def out(Transport):
#     for t in Transport:
#         t.out()

# out(listTr)









#listTr = [Transport(50, "92"), LandTr(56, "92", "E54"), AirTr(304, "90", "R72MU"), WTr(678, "8732", "fyjhfd"), Auto(34, "78", "YB56", "red"), Airplane(567, "7834", "KD*^TDK", "86"), Ship(923, "978", "LGV^", "jlfl")]
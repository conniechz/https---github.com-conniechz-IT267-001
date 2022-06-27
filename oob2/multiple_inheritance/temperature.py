class Temperature:
    def setcelsuls(self,celsuls:float):
        self.celuls = celsuls
    def getfahrenheit(self):
        return self.celuls * 1.8 + 32
    def getcelclus(self):
        return self.celuls
    def getweather(self):
        if self.celuls <= 0:
            return 'freezing'
        elif self.celuls <= 18:
            return 'cold'
        elif self.celuls <= 28:
            return 'warm'
        else:
            return 'hot'
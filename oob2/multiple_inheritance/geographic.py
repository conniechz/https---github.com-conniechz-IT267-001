class Geographic:
    def setcordinate(self,lat:float,long:float):
        self.lattitude = lat
        self.longitude = long
    def getcordinate(self):
        return f'lattitude : {self.lattitude} longitude : {self.longitude}'
    def gettimezone(self):
        timezone = round(self.longitude/12 - 1)
        if timezone > 0:
            return f'+{timezone}'
        else:
            return f'{timezone}'
    def getclimate(self):
        if self.lattitude <= -66.5 or self.lattitude >= 66.5:
            return f'Polar Zone'
        elif self.lattitude <= -23.5 or self.lattitude >= 23.5:
            return f'Temerate Zone'
        else:
            return f'Tropical Zone'
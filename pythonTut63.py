class Electronics:
    hardware="Android 11"
    camera="Sony IMX Sensor"
    Dispaly="Oled"
    processor="Exynous 2100"

class Pocketgadget(Electronics):
    buds="Apple Ear pods pro"
    charger="Wireless 20w"
    build="Glass"
    def isgadjet(self):
        return f"This gadgets are made by {self.build}"

class Phone(Pocketgadget):
    def __init__(self,givenName):
        self.name=givenName
    def isphone(self):
        return f"What a good device is {self.name}!"\
                f"This {self.name}'s camera is really good"

device=Electronics()
gadgets=Pocketgadget()
samrtphone=Phone("Samsung")

print(samrtphone.isphone())
print(samrtphone.isgadjet())
print(samrtphone.hardware)
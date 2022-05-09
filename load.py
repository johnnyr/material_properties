static = 'static'
drop = 'drop'
g = 9.81 # Gravity m/s**2

class Load(object):
    def __init__(
        self,
        W = 250, # Weigth lbs
        drop_height_m = 0,
        d = 0.004 # Distance traveled after impact m
    ):
        self.W = W
        self.type = type
        self.drop_height_m = drop_height_m
        self.d = d
    
    @property
    def m(self):
        return self.W / 2.2

    @property
    def fN(self):
        return (self.m * g * self.drop_height_m) / self.d
    
    @property
    def fkg(self):
        return self.fN * 0.1019716213 # force kg
    
    @property
    def flb(self):
        return self.fN * 0.224809 # force lb

    @property
    def force(self):
        if self.drop_height_m:
            print("Impact force " + str(self.flb) + "lbs")
            return self.flb
        return self.W

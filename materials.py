class Material(object):
    def __init__(
        self,
        name,
        E = 29.5*10**6, # Modulus Elasticity PSI Steel Cold rolled
        Ys = 40*10**3, # Yeild Strength PSI Steel 1020
    ):
        self.name = name
        self.E = E
        self.Ys = Ys

steel_1020 = Material('steel_1020', 29.5*10**6, 40*10**3) #  # Modulus Elasticity PSI, Yeild Strength PSI Steel 1020
a500 = Material('carbon_steel', 31.5*10**6, 60*10**3) #  # Modulus Elasticity PSI, Yeild Strength PSI Steel 1020
stainless_304 = Material('stainless_304', 28*10**6, 31.2*10**3)
aluminum_6061 = Material('aluminum_6061', 10.2*10**6, 35*10**3)

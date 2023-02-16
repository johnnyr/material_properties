from math import sqrt, pi


class RectangleBeam(object):
    def __init__(
        self,
        name,
        material,
        width, # Width inches
        thickness, # Thickness (diameter) inches
        length, # Length inches
        core_width = 0, # core width
        core_thickness = 0, # core thickness (diameter)
    ):
        self.name = name
        self.b = width
        self.d = thickness
        self.h = core_width
        self.t = core_thickness
        self.l = length
        self.material = material
        print(str(name) + " Material = " + material.name + ". Modulus Elasticity " + str(material.E) + " PSI. Yield Strength " + str(material.Ys) + " PSI")
        msg = "Rectangle Beam " + str(width) + "in Wide " + str(thickness) + "in Thick " + str(length) + "in Long "
        if self.h:
            msg += str(self.h) + "x" + str(self.t) + "in Hollow Core"
        print(msg)

    @property
    def y(self):
        return self.d / 2 # Center of thickness
    
    @property
    def A(self): # Area
        if self.h:
            return self.b * self.d - self.h * self.t
        return self.b * self.d
    @property
    def I(self): # Moment of Inertia in Inches
        if self.h:
            return ( (self.b * self.d**3) - (self.h * self.t**3) ) / 12
        return (self.b * self.d**3) / 12

    @property
    def Z(self): # Section Modulus
        return self.I / self.y

    @property
    def k(self): # Radius of Gyration
        if self.h:
            return sqrt( (self.b * self.d**3 - self.h * self.t**3) / (12 * (self.b * self.d - self.h * self.t) ) )
        return self.d / (sqrt(12))


class CircleBeam(object):
    def __init__(
        self,
        name,
        material,
        D, # Thickness (diameter) inches
        l, # Length inches
        d = 0, # core thickness (diameter)
    ):
        self.name = name
        self.D = D
        self.d = d
        self.l = l
        self.material = material
        print(str(name) + " Material = " + material.name + ". Modulus Elasticity " + str(material.E) + " PSI. yield Strength " + str(material.Ys) + " PSI")
        msg = "Circle Beam " + str(D) + "in Diameter " + str(l) + "in Long "
        if self.d:
            msg + str(d) + "in Hollow Core"
        print(msg)
        msg = "Area of Section " + str(self.A) + ". Moment of Inertia " + str(self.I) + ". Section Modulus " + str(self.Z) + ". Radius pf Gyration " + str(self.k)
        print(msg)

    @property
    def y(self):
        return self.D / 2 # Distance from Neutral Axis to Extreme Fiber
    
    @property
    def A(self): # Area of Section
        if self.d:
            return (pi * (self.D^2 - self.d**2))/4
        return (pi * self.D**2)/4

    @property
    def I(self): # Moment of Inertia
        if self.d:
            return (pi * (self.D**4 - self.d**4))/64
        return (pi * self.D**4) / 64
    
    @property
    def Z(self): # Section Modulus
        return self.I / self.y
    
    @property
    def k(self): # Radius of Gyration
        if self.d:
            return sqrt( (self.D**2 + self.d**2) / 4 )
        return self.D / 4

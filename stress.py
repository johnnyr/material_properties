from math import sqrt, pi

circle = 'circle'
rectangle = 'rectangle'
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
            return self.flb
        return self.W

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
        print(str(name) + " Material = " + material.name + ". Modulus Elasticity " + str(material.E) + " PSI. Yeild Strength " + str(material.Ys) + " PSI")
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
    def I(self): # Moment of Inertia
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
        print(str(name) + " Material = " + material.name + ". Modulus Elasticity " + str(material.E) + " PSI. Yeild Strength " + str(material.Ys) + " PSI")
        msg = "Circle Beam " + str(D) + "in Diameter " + str(l) + "in Long "
        if self.d:
            msg + str(d) + "in Hollow Core"
        print(msg)
        print("Material = " + material.name)

    @property
    def y(self):
        if self.d:
            return self.D / 2
        return self.D / 2 # Distance from Neutral Axis to Extreme Fiber
    
    @property
    def A(self): # Area of Section
        if self.D:
            return (pi * (self.D^2 - self.d**2))/4
        return (pi * self.D**2)/4

    @property
    def I(self): # Moment of Inertia
        if self.tube:
            return (pi * (self.D**4 - self.d**4))/64
        return (pi * self.D**4) / 64
    
    @property
    def Z(self): # Section Modulus
        return self.I / self.y
    
    @property
    def k(self): # Radius of Gyration
        if self.tube:
            return sqrt( (self.D**2 + self.d**2) / 4 )
        return self.D / 4

class Object(object):
    def __init__(
        self,
        name
    ):
        self.name = name

one_end_fixed = Object('one_end_fixed') # other end load
supported_both_ends = Object('supported_both_ends')

class Stress(object):
    def __init__(
        self,
        beam,
        load,
        support,
        x = None # ratio of length for extra calculation point
    ):
        self.beam = beam
        self.load = load
        self.support = support
        self.x = x
        if not self.x:
            self.x = 0.5 * beam.l
        msg = "Beam " + beam.name + " Load = " + str(load.W) + "lbs"
        if load.drop_height_m:
            msg += ". Drop Height " + str(load.drop_height_m) + "m. Distance after impact " + str(load.d)
        print(msg)
        print("Support = " + support.name)
        print("Stress Max " + str(self.stress_max) + " lbs/in^2")
        print("Maximum deflection " + str(self.deflection_max) + "in")
        print("Stress at " + str(self.x) + "in from support " + str(self.stress_max) + " lbs/in^2")
        print("Deflection at " + str(self.x) + "in from support = " + str(self.stress_at_x) + " lbs/in^2")
        print("Safety Margin " + str(self.margin))
    
    @property
    def stress_at_x(self): # s
        if self.support == one_end_fixed:
            return (self.load.force / self.beam.Z) * (self.beam.l - self.x)

    @property
    def deflection_at_x(self): # y
        if self.support == one_end_fixed:
            return ( (self.load.force * self.x**2) / (6 * self.beam.material.E * self.beam.I) ) * (3 * self.beam.l - self.x)
    
    @property
    def stress_max(self): # stress at critical points
        if self.support == one_end_fixed: # at support
            return (self.load.force * self.beam.l) / self.beam.Z
    
    @property
    def deflection_max(self): # d
        if self.support == one_end_fixed: # at end
            return (self.load.W * self.beam.l**3) / (3 * self.beam.material.E * self.beam.I)
    
    @property
    def margin(self): # Safety Margin
        return self.beam.material.Ys / self.stress_max

steel_1020 = Material('steel_1020', 29.5*10**6, 40*10**3) #  # Modulus Elasticity PSI, Yeild Strength PSI Steel 1020
stainless_304 = Material('stainless_304', 28*10**6, 31.2*10**3)
aluminum_6061 = Material('aluminum_6061', 10.2*10**6, 35*10**3)

rocker = RectangleBeam(
    'Rocker',
    material = steel_1020,
    width = 2,
    thickness = 2,
    length = 12,
    core_width = 1.76,
    core_thickness = 1.76
)
rocker_load = Load(300)
rocker_static = Stress(rocker, rocker_load, one_end_fixed)
print()
drop_load = Load(10, 1)
rocker_drop = Stress(rocker, drop_load, one_end_fixed)
print()
knuckle_flat = RectangleBeam(
    'Knuckle Flat',
    material = steel_1020,
    width = 2,
    thickness = 3/8,
    length = 1.5
)
knuckle_flat_static = Stress(knuckle_flat, rocker_load, one_end_fixed)
print()
knuckle_drop = Stress(knuckle_flat, drop_load, one_end_fixed)
print(str(knuckle_flat.A))
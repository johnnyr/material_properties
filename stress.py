
class Object(object):
    def __init__(
        self,
        name
    ):
        self.name = name

one_end_fixed = Object('one_end_fixed') # other end load
supported_both_ends = Object('supported_both_ends') # supported both ends, load at center
direct_compression = Object('direct_compression')
support_options = [direct_compression, one_end_fixed, supported_both_ends]

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
            msg += ". Drop Height " + str(load.drop_height_m) + "m. Distance after impact " + str(load.d) + ". Impact force " + str(self.load.flb) + "lbs"
        print(msg)
        if support not in support_options:
            print("No Support selected")
            return 
        print("Support = " + support.name)
        print("Stress Max " + str(self.stress_max) + " lbs/in^2")
        print("Maximum deflection " + str(self.deflection_max) + "in")
        print("Stress at " + str(self.x) + "in from support = " + str(self.stress_at_x) + " lbs/in^2")
        print("Safety Margin " + str(self.margin))
    
    @property
    def stress_at_x(self): # s
        if self.support == one_end_fixed:
            return (self.load.force / self.beam.Z) * (self.beam.l - self.x)
        if self.support == supported_both_ends:
            return (self.load.force * self.x) / (2 * self.beam.Z)
        return None


    @property
    def deflection_at_x(self): # y
        if self.support == one_end_fixed:
            return ( (self.load.force * self.x**2) / (6 * self.beam.material.E * self.beam.I) ) * (3 * self.beam.l - self.x)
        if self.support == supported_both_ends:
            return ( (self.load.force * self.x) / (48 * self.beam.material.E * self.beam.I) ) * (3 * self.beam.l**2 - 4 * self.x**2)
        return None
    
    @property
    def stress_max(self): # stress at critical points
        if self.support == one_end_fixed: # at support
            return (self.load.force * self.beam.l) / self.beam.Z
        if self.support == supported_both_ends: # at center
            return -(self.load.force * self.beam.l) / (4 * self.beam.Z)
        if self.support == direct_compression:
            return self.load.force / self.beam.A
        return None
    
    @property
    def deflection_max(self): # d
        if self.support == one_end_fixed: # at end
            return (self.load.force * self.beam.l**3) / (3 * self.beam.material.E * self.beam.I)
        if self.support == supported_both_ends: # at load / center
            return (self.load.force * self.beam.l**3) / (48 * self.beam.material.E * self.beam.I)
        if self.support == direct_compression:
            return (self.load.force * self.beam.l) / (self.beam.A * self.beam.material.E)
        return None
    
    @property
    def margin(self): # Safety Margin
        return self.beam.material.Ys / self.stress_max


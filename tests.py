from cross_sections import (
    RectangleBeam,
    CircleBeam
)
from materials import (
    steel_1020,
    stainless_304,
    aluminum_6061
)
from load import(
    Load
)
from stress import(
    Stress,
    one_end_fixed,
    supported_both_ends
)

rocker_half = RectangleBeam( # One half of rocker calculated from pivot to knuckle
    'Rocker_half',
    material = steel_1020,
    width = 2,
    thickness = 2,
    length = 12,
    core_width = 1.76,
    core_thickness = 1.76
)
rocker_load = Load(300)
rocker_half_static = Stress(rocker_half, rocker_load, one_end_fixed)
print()
drop_load = Load(10, 1, 0.006)
rocker_half_drop = Stress(rocker_half, drop_load, one_end_fixed)
print()
rocker = RectangleBeam(
    'Rocker',
    material = steel_1020,
    width = 2,
    thickness = 2,
    length = 24,
    core_width = 1.76,
    core_thickness = 1.76
)
rocker_static = Stress(rocker, rocker_load, supported_both_ends)
print()
rocker_drop = Stress(rocker, drop_load, supported_both_ends)
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
print()
solid_circle = CircleBeam(
    'solid_circle',
    steel_1020,
    9/16,
    2.5
)
solid_circle_static = Stress(solid_circle, rocker_load, one_end_fixed)
print()
from cross_sections import (
    RectangleBeam,
    CircleBeam
)
from materials import (
    steel_1020,
    stainless_304,
    aluminum_6061,
    a500
)
from load import(
    Load
)
from stress import(
    Stress,
    direct_compression,
    one_end_fixed,
    supported_both_ends
)
#
#rocker_tractor = 160/25.4
#
#rocker_half = RectangleBeam( # One half of rocker calculated from pivot to knuckle
#    'Rocker_half',
#    material = steel_1020,
#    width = 2,
#    thickness = 2,
#    length = rocker_tractor,
#    core_width = 1.76,
#    core_thickness = 1.76
#)
#rocker_load = Load(300)
#rocker_half_static = Stress(rocker_half, rocker_load, one_end_fixed)
#print()
#drop_load = Load(10, 1, 0.006)
#rocker_half_drop = Stress(rocker_half, drop_load, one_end_fixed)
#print()
#rocker = RectangleBeam(
#    'Rocker',
#    material = steel_1020,
#    width = 2,
#    thickness = 2,
#    length = rocker_tractor * 2,
#    core_width = 1.76,
#    core_thickness = 1.76
#)
#rocker_static = Stress(rocker, rocker_load, supported_both_ends)
#print()
#rocker_drop = Stress(rocker, drop_load, supported_both_ends)
#print()

# Front wheel mount
sheet_thickness = .0598 # 15guage
width = 5.8
thickness = 1.61

rocker_frame = RectangleBeam( # 16
    'rocker_frame',
    material = aluminum_6061,
    width = width,
    thickness = thickness,
    length = 3,
    core_width = width - (2 * sheet_thickness),
    core_thickness = thickness - (2*sheet_thickness)
)
rocker_load = Load(300)
table_half_static = Stress(rocker_frame, rocker_load, one_end_fixed)
drop_load = Load(30, 1, 0.006)
table_half_drop = Stress(rocker_frame, drop_load, one_end_fixed)
print()


width = 1
thickness = 2
# Bed Frame
sheet_thickness = 0.125 # 15guage
table_half = RectangleBeam( # 16
    'table_half',
    material = aluminum_6061,
    width = width,
    thickness = thickness,
    length = 166.143 / 25.4,
    core_width = width - (2 * sheet_thickness),
    core_thickness = thickness - (2*sheet_thickness)
)
rocker_load = Load(300)
table_half_static = Stress(table_half, rocker_load, one_end_fixed)
drop_load = Load(100, 0.2, 0.006)
table_half_drop = Stress(table_half, drop_load, one_end_fixed)
print()


#table_half = RectangleBeam( # 16 gauge
#    'table_half',
#    material = steel_1020,
#    width = 1,
#    thickness = 2,
#    length = 10,
#    core_width = 0.875,
#    core_thickness = 1.875
#)
#rocker_load = Load(300)
#table_half_static = Stress(table_half, rocker_load, one_end_fixed)
#print()
#drop_load = Load(10, 1, 0.006)
#table_half_drop = Stress(table_half, drop_load, one_end_fixed)
#print()
#knuckle_flat = RectangleBeam(
#    'Knuckle Flat',
#    material = steel_1020,
#    width = 2,
#    thickness = 3/8,
#    length = 1.5
#)
#knuckle_flat_static = Stress(knuckle_flat, rocker_load, one_end_fixed)
#print()
#knuckle_drop = Stress(knuckle_flat, drop_load, one_end_fixed)
#print()
#solid_circle = CircleBeam(
#    'solid_circle',
#    steel_1020,
#    16/25.4,
#    2.5
#)
#solid_circle_static = Stress(solid_circle, rocker_load, one_end_fixed)
#print()
#solid_circle_drop = Stress(solid_circle, drop_load, one_end_fixed)
#
#print()
#differential = RectangleBeam(
#    'Differential',
#    material = a500,
#    width = 0.75,
#    thickness = 1.5,
#    length = 225 / 25.4,
#    core_width = 0.75 - (0.065 * 2),
#    core_thickness = 1.5 - (0.065 * 2)
#)
#differential_load = Load(300)
#rocker_static = Stress(differential, differential_load, supported_both_ends)
#
#print()
#differential_aluminum = RectangleBeam(
#    'Differential Aluminum',
#    material = aluminum_6061,
#    width = 0.5,
#    thickness = 1,
#    length = 225 / 25.4,
#    core_width = 0.5 - (0.065 * 2),
#    core_thickness = 1 - (0.065 * 2)
#)
#rocker_static = Stress(differential_aluminum, differential_load, supported_both_ends)
#
#print()
#linkage = CircleBeam(
#    'linkage',
#    steel_1020,
#    0.367,
#    130/25.4
#)
#rocker_static = Stress(linkage, differential_load, direct_compression)
#
#print()
#bolt_shear = CircleBeam(
#    'bolt_shear',
#    steel_1020,
#    0.367,
#    1/16
#)
#bolt_shear_static = Stress(bolt_shear, Load(abs(rocker_static.stress_max)), one_end_fixed)
#
##print()
##curtain = RectangleBeam(
##    'Rocker',
##    material = a500,
##    width = 2,
##    thickness = 2,
##    length = 155,
##    core_width = 1.76,
##    core_thickness = 1.76
##)
##curtain_load = Load(500)
##rocker_static = Stress(curtain, curtain_load, supported_both_ends)
#
#
#frame_half = RectangleBeam( # One half of rocker calculated from pivot to knuckle
#    'Frame_half',
#    material = steel_1020,
#    width = 2,
#    thickness = 2,
#    length = 12,
#    core_width = 1.904,
#    core_thickness = 1.904
#)
#frame_half_static = Stress(frame_half, rocker_load, one_end_fixed)
#print()
#drop_load = Load(10, 1, 0.006)
#rocker_half_drop = Stress(rocker_half, drop_load, one_end_fixed)
#print()
#
#
#frame_half_alum = RectangleBeam( # One half of rocker calculated from pivot to knuckle
#    'Frame_half_alum',
#    material = aluminum_6061,
#    width = 2,
#    thickness = 2,
#    length = 12,
#    core_width = 1.904,
#    core_thickness = 1.904
#)
#frame_half_static = Stress(frame_half, rocker_load, one_end_fixed)
#print()
#drop_load = Load(10, 1, 0.006)
#rocker_half_drop = Stress(rocker_half, drop_load, one_end_fixed)
#print()
#
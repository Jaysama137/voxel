from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1)
scene.set_directional_light((1, 1, 1), 0.1, (1, 1, 1))
scene.set_background_color((0.3, 0.4, 0.6))
scene.set_floor(-0.85, (1.0, 1.0, 1.0))

red = vec3(172, 35, 43) / 255.0
blue = vec3(10, 0, 175) / 255.0
orange = vec3(179, 69, 42) / 255.0
grey = vec3(229,229,229) / 255.0
white = vec3(248,248,248) / 255.0

z_coord = 1;

@ti.func
def setblock(begin, end, color):
    for i, j in ti.ndrange((begin.x, end.x), (begin.y, end.y)):
        scene.set_voxel(ivec3(i, j, z_coord), 1, color)

@ti.func
def setblock_bysize(begin, size, color):
    end = begin + size
    setblock(begin, end, color)

@ti.kernel
def initialize_voxels():
    setblock(ivec2(-60, -30), ivec2(60, 30), white)
    setblock(ivec2(-60, 25), ivec2(60, 30), orange)
    setblock(ivec2(-60, -25), ivec2(60, 20), grey)

    setblock(ivec2(-30, -22), ivec2(45, 19), white)
    setblock_bysize(ivec2(-10, 8), 4 * ivec2(6, 1), red)
    setblock_bysize(ivec2(-10, 3), 4 * ivec2(5, 1), blue)
    setblock_bysize(ivec2(-10, -2), 4 * ivec2(4, 1), red)
    setblock_bysize(ivec2(-10, -7), 4 * ivec2(7, 1), blue)
    setblock_bysize(ivec2(-10, -12), 4 * ivec2(2, 1), red)

    setblock_bysize(ivec2(-58, 8), ivec2(14, 7), white)
    setblock_bysize(ivec2(-54, 13), ivec2(6, 1), red)
    setblock_bysize(ivec2(-54, 12), ivec2(5, 1), blue)
    setblock_bysize(ivec2(-54, 11), ivec2(4, 1), red)
    setblock_bysize(ivec2(-54, 10), ivec2(7, 1), blue)
    setblock_bysize(ivec2(-54, 9), ivec2(2, 1), red)

initialize_voxels()

scene.finish()
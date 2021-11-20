#!/usr/bin/env python
# coding: utf-8



import numpy as np
import vpython as vp


E_radius = 6400
min_height = 7000
max_height = 10000
angle_low = np.deg2rad(10)
angle_high = np.deg2rad(75)
ra = np.deg2rad(90)


def draw_cones(theta, phi):
    # theta = lat 
    # phi = lon
    sp = np.sin(phi)
    st = np.sin(theta)
    cp = np.cos(phi)
    ct = np.cos(theta)
    orientation = vp.vector(ct*cp, ct*sp, st)
    tip = E_radius*orientation
    base = tip + max_height*orientation
    vp.cone(pos=base,axis=-orientation,
        radius=max_height*np.tan(ra-angle_high),
        length=max_height,
        color=vp.color.red,
        opacity=0.3)
    vp.cone(pos=base,axis=-orientation,
        radius=max_height*np.tan(ra-angle_low),
        length=max_height,
        color=vp.color.green,
        opacity=0.3)


vp.scene.title = "My first VPython"
vp.scene.width = 640
vp.scene.height = 400
#scene.range = 5
#vp.scene.background = vp.color.gray(0.7)
#vp.scene.center = vp.vector(0,0.5,0)
#vp.scene.forward = vp.vector(-.3,0,-1)
ball = vp.sphere(pos=vp.vector(0,0,0), radius=E_radius, color=vp.color.cyan)
vp.sphere(pos=vp.vector(0,0,0), radius=E_radius+min_height, color=vp.color.yellow,opacity=0.4)
vp.arrow(pos=vp.vector(0,0,0), axis=vp.vector(E_radius+min_height,0,0), color=vp.color.red)
vp.arrow(pos=vp.vector(0,0,0), axis=vp.vector(0,E_radius+min_height,0), color=vp.color.green )
vp.arrow(pos=vp.vector(0,0,0), axis=vp.vector(0,0,E_radius+min_height), color=vp.color.blue )


alpha = np.pi/9
draw_cones(alpha, 0)
draw_cones(-alpha, 0)
draw_cones(alpha,alpha)
draw_cones(-alpha,alpha)


vp.scene.autoscale = True






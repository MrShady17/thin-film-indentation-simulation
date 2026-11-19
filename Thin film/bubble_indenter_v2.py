#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bubble_indenter_v2.py  (based on bubble_indentor_V1.py, @author: gparry)

Generator for buckle delamination simulations -- MESH ONLY.

v2 changes with respect to v1 (see "NEW" / "FIXED" tags below):
  - NEW   : *Element blocks (C3D8R substrate, S4R film) are now written
  - NEW   : *Elset SUBSTRATE, ALLFILM, FILM_BONDED, FILM_DEBOND, SUB_TOP
  - FIXED : *Nset RP_INDENTER is written BEFORE *Rigid Body
  - FIXED : indenter surface is a TYPE=REVOLUTION surface (START + CIRCL)
  - FIXED : SURF_SUB uses the elset SUB_TOP instead of 57600 lines
  - FIXED : the output file is closed at the end (f.close())
  - print statements use print() so the script runs with python 2 and 3

Units:

length  : mm
force   : mN
stress  : MPa
energy  : mN/mm
"""

from __future__ import print_function
from math import *

#########################################################################
# OUTPUT FILE
#########################################################################

inp_name = 'bubble_indenter_v2.inp'

f = open(inp_name, 'w')

#########################################################################
# GEOMETRY
#########################################################################

#
# Film
#

hf = 45.e-6                 # 45 nm

#
# Substrate
#

hs = 0.045                  # 45 µm

#
# In-plane dimensions
#

Lx = 0.120                  # 120 µm
Ly = 0.120

#########################################################################
# MESH
#########################################################################

mesh_size = 0.0005          # 0.5 µm

nx = int(round(Lx/mesh_size))
ny = int(round(Ly/mesh_size))

dx = Lx/nx
dy = Ly/ny

#
# substrate
#

nz = 5

bias_ratio = 30.0

#########################################################################
# MATERIALS (not written to the .inp yet -- mesh only)
#########################################################################

#
# Tantalum
#

E_film = 186.e3
nu_film = 0.34

alpha_film = 6.5e-6

rho_film = 0.008

#
# Soda-lime glass
#

E_sub = 70.e3
nu_sub = 0.22

alpha_sub = 9.e-6

rho_sub = 0.002

#########################################################################
# RESIDUAL STRESS
#########################################################################

sigma0 = 800.0          # MPa

dT = -sigma0/(E_film*alpha_film)

#########################################################################
# COHESIVE LAW
#########################################################################

Kn = 1.e7
Kt = Kn

Tnmax = 2000.
Ttmax = 2000.

Gc = 1.e-3

#########################################################################
# INITIAL DEBOND
#########################################################################

#
# Circular blister
#

a0 = 0.004

r0 = 0.5*a0

#
# Position
#

xmid_debond = 0.25*Lx
ymid_debond = 0.5*Ly

#########################################################################
# INITIAL IMPERFECTION
#########################################################################

delta = hf

#########################################################################
# INDENTER
#########################################################################

#
# Analytical rigid sphere
#

R_ind = 0.50          # mm

x_ind = 0.5*Lx
y_ind = 0.5*Ly

#
# Initial sphere center
#

z_ind0 = hs + hf + R_ind

#
# Half opening angle of the spherical cap that is described
# (must stay < 89.87 deg : Abaqus limits one CIRCL to < 179.74 deg)
#

theta_max = 0.35*pi

#
# Prescribed indentation depth
#

indent_depth = 0.004      # 4 µm

#########################################################################
# ANALYSIS (not written yet)
#########################################################################

step_time = 0.10

#########################################################################
# VISCOUS DAMPING (not written yet)
#########################################################################

vp_coeff = 0.488

#########################################################################
# OUTPUT FREQUENCY (not written yet)
#########################################################################

field_interval = 2.5e-5

#########################################################################
# HELPER : write a list of ids, 16 per line (Abaqus limit)
#########################################################################

def write_id_list(fh, ids):

    for k in range(0, len(ids), 16):

        fh.write(', '.join('%d' % v for v in ids[k:k+16]) + '\n')

#########################################################################
# PRINT PARAMETERS
#########################################################################

print()
print('----------------------------')
print('MODEL')
print('----------------------------')
print()

print('Lx             =', Lx, 'mm')
print('Ly             =', Ly, 'mm')

print('hf             =', hf, 'mm')
print('hs             =', hs, 'mm')

print('mesh           =', mesh_size, 'mm')

print('nx             =', nx)
print('ny             =', ny)
print('nz             =', nz)

print()


#########################################################################
# BIASED SUBSTRATE MESH
#########################################################################

z = [0.0]

r = bias_ratio**(1.0/float(nz-1))

a = hs*(r-1.0)/(r**nz-1.0)

zz = 0.0
h = a*r**(nz-1)

for k in range(nz):

    zz += h
    z.append(zz)

    h /= r

z[-1] = hs

print()
print('Substrate layers')

for k in range(nz):
    print('%2d : %10.6e mm' % (k+1, z[k+1]-z[k]))

print()


#########################################################################
# SUBSTRATE NODES
#########################################################################

nodes_sub = []
node_sub = {}

nid = 1

for k in range(nz+1):

    zz = z[k]

    for j in range(ny+1):

        yy = j*dy

        for i in range(nx+1):

            xx = i*dx

            nodes_sub.append(
                (nid, xx, yy, zz)
            )

            node_sub[(i, j, k)] = nid

            nid += 1

print('Substrate nodes :', len(nodes_sub))


#########################################################################
# FILM NODES
#########################################################################

nodes_film = []
node_film = {}

for j in range(ny+1):

    yy = j*dy

    for i in range(nx+1):

        xx = i*dx

        #
        # Shell mid-surface
        #

        zz = hs + 0.5*hf

        #
        # Initial blister
        #

        dx0 = xx-xmid_debond
        dy0 = yy-ymid_debond

        rr = sqrt(dx0*dx0+dy0*dy0)

        if rr <= r0:

            xi = rr/r0

            zz += 0.5*delta*(1.+cos(pi*xi))

        nodes_film.append(
            (nid, xx, yy, zz)
        )

        node_film[(i, j)] = nid

        nid += 1

print('Film nodes :', len(nodes_film))



#########################################################################
# INDENTER REFERENCE NODE
#########################################################################

RP_IND = nid

nodes_ind = [
    (
        RP_IND,
        x_ind,
        y_ind,
        z_ind0
    )
]

nid += 1

print('Reference point :', RP_IND)


#########################################################################
# ALL NODES
#########################################################################

nodes = []

nodes.extend(nodes_sub)
nodes.extend(nodes_film)
nodes.extend(nodes_ind)

print()
print('TOTAL NODES =', len(nodes))


f.write('*Node\n')

for n in nodes:
    f.write(
        '%d, %.8e, %.8e, %.8e\n' % n
    )


#########################################################################
# SUBSTRATE ELEMENTS                                              (NEW)
#########################################################################
#
# C3D8R : 8-node brick, reduced integration.
# Node order : bottom face counter-clockwise (n1..n4), then the top face
# directly above it (n5..n8)  ->  positive volume, face S2 = top (+z).
#

elems_sub = []
elem_sub = {}

eid = 1

for k in range(nz):

    for j in range(ny):

        for i in range(nx):

            n1 = node_sub[(i, j, k)]
            n2 = node_sub[(i+1, j, k)]
            n3 = node_sub[(i+1, j+1, k)]
            n4 = node_sub[(i, j+1, k)]

            n5 = node_sub[(i, j, k+1)]
            n6 = node_sub[(i+1, j, k+1)]
            n7 = node_sub[(i+1, j+1, k+1)]
            n8 = node_sub[(i, j+1, k+1)]

            elems_sub.append(
                (eid,
                 n1, n2, n3, n4,
                 n5, n6, n7, n8)
            )

            elem_sub[(i, j, k)] = eid

            eid += 1

print('Substrate elements =', len(elems_sub))

# NEW : write them (and create the elset SUBSTRATE through elset=)
f.write('*Element, type=C3D8R, elset=SUBSTRATE\n')

for e in elems_sub:
    f.write('%d, %d, %d, %d, %d, %d, %d, %d, %d\n' % e)


#########################################################################
# FILM ELEMENTS                                                   (NEW)
#########################################################################
#
# S4R : 4-node shell, reduced integration.
# Node order counter-clockwise seen from +z -> normal = +z,
# so SPOS = top face, SNEG = bottom face (facing the substrate).
#

elems_film = []
elem_film = {}

for j in range(ny):

    for i in range(nx):

        n1 = node_film[(i, j)]
        n2 = node_film[(i+1, j)]
        n3 = node_film[(i+1, j+1)]
        n4 = node_film[(i, j+1)]

        elems_film.append(
            (eid, n1, n2, n3, n4)
        )

        elem_film[(i, j)] = eid

        eid += 1

print('Film elements =', len(elems_film))

# NEW : write them (and create the elset ALLFILM through elset=)
f.write('*Element, type=S4R, elset=ALLFILM\n')

for e in elems_film:
    f.write('%d, %d, %d, %d, %d\n' % e)


#########################################################################
# FILM REGIONS                                                    (NEW)
#########################################################################

film_bonded = []
film_debond = []

for j in range(ny):

    for i in range(nx):

        xc = (i+0.5)*dx
        yc = (j+0.5)*dy

        rr = sqrt(
            (xc-xmid_debond)**2 +
            (yc-ymid_debond)**2
        )

        e_id = elem_film[(i, j)]

        if rr <= r0:

            film_debond.append(e_id)

        else:

            film_bonded.append(e_id)

print('Film bonded elements =', len(film_bonded))
print('Film debond elements =', len(film_debond))

assert len(film_bonded) + len(film_debond) == len(elems_film)
assert len(film_debond) > 0, 'r0 is too small for the mesh : no debonded element'

f.write('*Elset, elset=FILM_BONDED\n')
write_id_list(f, film_bonded)

f.write('*Elset, elset=FILM_DEBOND\n')
write_id_list(f, film_debond)


#########################################################################
# TOP LAYER OF THE SUBSTRATE                                      (NEW)
#########################################################################

sub_top = []

for j in range(ny):

    for i in range(nx):

        sub_top.append(
            elem_sub[(i, j, nz-1)]
        )

f.write('*Elset, elset=SUB_TOP\n')
write_id_list(f, sub_top)


#########################################################################
# REFERENCE POINT SET                        (FIXED : now before *Rigid Body)
#########################################################################

f.write('*Nset, nset=RP_INDENTER\n')
f.write('%d\n' % RP_IND)


#########################################################################
# SURFACES
#########################################################################

f.write('*Surface, type=ELEMENT, name=SURF_FILM_TOP\n')
f.write('ALLFILM, SPOS\n')

f.write('*Surface, type=ELEMENT, name=SURF_FILM_BONDED\n')
f.write('FILM_BONDED, SNEG\n')

f.write('*Surface, type=ELEMENT, name=SURF_FILM_DEBOND\n')
f.write('FILM_DEBOND, SNEG\n')

# FIXED : face S2 of the top layer of C3D8R = top face (+z)
f.write('*Surface, type=ELEMENT, name=SURF_SUB\n')
f.write('SUB_TOP, S2\n')


#########################################################################
# ANALYTICAL RIGID SPHERE                                      (FIXED)
#########################################################################
#
# Surface of revolution.
#  - 1st data line : two points a and b (global coordinates) :
#      a = local origin = sphere centre (= reference node)
#      b = a + 1 in z  -> the axis of revolution is vertical
#  - profile in the local (r, z) plane, origin at the sphere centre :
#      START at the outer end of the cap, then ONE circular arc
#      (CIRCL = end point r,z + centre r,z) down to the pole (0,-R).
#    The direction START -> pole is what makes the normal point OUT of
#    the sphere (towards the film).  CHECK it visually in Abaqus/CAE.
#

f.write('*Surface, type=REVOLUTION, name=INDENTER\n')

f.write('%.8e, %.8e, %.8e, %.8e, %.8e, %.8e\n' %
        (x_ind, y_ind, z_ind0,
         x_ind, y_ind, z_ind0 + 1.0))

f.write('START, %.8e, %.8e\n' % (R_ind*sin(theta_max),
                                 -R_ind*cos(theta_max)))

f.write('CIRCL, %.8e, %.8e, %.8e, %.8e\n' % (0.0, -R_ind,
                                             0.0, 0.0))


#########################################################################
# RIGID BODY
#########################################################################

f.write('*Rigid Body, analytical surface=INDENTER, ref node=RP_INDENTER\n')


#########################################################################
# CLOSE FILE                                                   (FIXED)
#########################################################################

f.close()

print()
print('Written :', inp_name)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:48:12 2026

@author: gparry
"""
# -*- coding: mbcs -*-
from __future__ import division
from math import pi, tan, sin, cos



#########################################################################
# MATERIAL PARAMETERS
#########################################################################

# Film (MPa)
E_film  = 186.e3   # MPa
nu_film = 0.34

# Substrate (MPa)
E_sub  = 70.e3     # MPa
nu_sub = 0.22

# Densities
rho_film = 0.008
rho_sub = 0.002

#########################################################################
# THERMAL EXPANSION (1/°C)
#########################################################################

alpha_film = 5.0e-5
alpha_sub = 0.0

#########################################################################
# COHESIVE PARAMETERS
#########################################################################

Tn_max = 8.
Tt_max = 10.
Ts_max = 10.

GIc = 0.1E-3
eta = 0.9

#########################################################################
# EXPLICIT PARAMETERS
#########################################################################

step_time = 0.1
mass_dt = 1.e-6
#visc = 0.488 -- on ne voit pas les cordons 
visc = 0.1 #-- on voit les cordons
#visc = 0.025 -- trop de vibrations

#########################################################################
# TARGET RESIDUAL STRESS (MPa)
#########################################################################

sigma0 = 1200.0
#sigma0 = 800.


# Geometry (mm)
hf = 45.E-6
hs = 45.E-3            # 100 µm substrate thickness


#Lx = 50.0e-3
#Ly = 50.0e-3
Lx = 0.08 
Ly = Lx

# Mesh
#mesh_size_xy = 1.0e-3 #vu cloque longiligne
mesh_size_xy = 1.0e-3

bias_ratio = 20.0
nz = 5


#########################################################################
# INDENTER
#########################################################################

R_ind = 0.2          # mm

x_ind = 0.5*Lx
y_ind = 0.5*Ly

#
# Initial position of reference point
#

z_ind = hs + hf + R_ind + 0.001

#indent = 0.003       # mm
indent = 0.0015   


#########################################################################
# INITIAL SQUARE DEBOND size
#########################################################################

#a0 = 5.0e-3
#a0 = 8.0e-3
#a0 = 0.004           # 4 µm blister width
a0 = 0.008           

#########################################################################
# INITIAL SQUARE DEBOND LOCATION
#########################################################################

xmid_debond = 0.25 * Lx
ymid_debond = 0.50 * Ly
#xmid_debond = x_ind - a_hertz
#ymid_debond = y_ind


#automatic calculation of parameters-----
#########################################################################
# INITIAL CIRCULAR DEBOND
#########################################################################

r0 = 0.5 * a0

# Initial imperfection amplitude (mm)
#delta = 1.E-3* hf
delta = 0.1* hf




#########################################################################
# WRITE INDENTER REFERENCE NODE
#########################################################################

def writeRigidSphereNode(f, RP, x0, y0, z0):

    f.write('%d, %e, %e, %e\n' %
            (RP, x0, y0, z0))


#########################################################################
# WRITE INDENTER NODE SET
#########################################################################

def writeRigidSphereSet(f, RP):

    f.write('*Nset, nset=RP_INDENTER\n')
    f.write('%d,\n' % RP)


#########################################################################
# WRITE ANALYTICAL RIGID SURFACE
#########################################################################

def writeRigidSphereSurface(f, R):

   f.write('*Surface, type=REVOLUTION, name=INDENTER\n')

#
# Local z-axis = global Z
#

   f.write('%e,%e,%e,%e,%e,%e\n' %
        (x_ind,
         y_ind,
         z_ind,
         x_ind,
         y_ind,
         z_ind + 1.0))
#
# Start point
#

   f.write('START,%e,%e\n' % (R,0.))

#
# Quarter circle
#

   f.write('CIRCL,%e,%e,%e,%e\n'
           % (0.,
              -R,
              0.,
              0.))


   f.write('*Rigid Body, ref node=RP_INDENTER, analytical surface=INDENTER\n')







#########################################################################
# NUMBER OF ELEMENTS
#########################################################################

nx = max(2, int(round(Lx / mesh_size_xy)))
ny = max(2, int(round(Ly / mesh_size_xy)))
#nz = max(3, int(round(hs / mesh_size_xy)))

print ('nx =', nx)
print ('ny =', ny)
#print 'nz =', nz

dx = Lx / nx
dy = Ly / ny

##########################################################################
# SUBSTRATE THICKNESS DISCRETIZATION
#########################################################################

#########################################################################
# BIASED Z COORDINATES
# Fine mesh near z = hs (film/substrate interface)
#########################################################################

z = [0.0]

r = bias_ratio**(1.0 / float(nz - 1))

a = hs * (r - 1.0) / (r**nz - 1.0)

zz = 0.0
h = a * r**(nz - 1)

for k in range(nz):

    zz += h
    z.append(zz)

    h /= r

z[-1] = hs

print 'nz =', nz
print 'layer thicknesses:'

for k in range(nz):
    print k+1, z[k+1] - z[k]

print 'first layer thickness =', z[1] - z[0]
print 'last layer thickness  =', z[-1] - z[-2]

#########################################################################
# SUBSTRATE NODES
#########################################################################

nodes_sub = []
node_sub = {}

nid = 1

for k in range(nz + 1):

    zz = z[k]

    for j in range(ny + 1):

        yy = j * dy

        for i in range(nx + 1):

            xx = i * dx

            nodes_sub.append((nid, xx, yy, zz))
            node_sub[(i, j, k)] = nid

            nid += 1

print 'substrate nodes =', len(nodes_sub)


        
    

#########################################################################
# FILM NODES
#########################################################################

nodes_film = []
node_film = {}

for j in range(ny + 1):

    yy = j * dy

    for i in range(nx + 1):

        xx = i * dx
        #take into account half plate thickness shift
        zz = hs + 0.5*hf
        #if plane is the bottom plane
#        zz = hs

        dx0 = xx - xmid_debond
        dy0 = yy - ymid_debond
        rr = (dx0**2 + dy0**2)**0.5
        
        if rr <= r0:
        
            xi = rr / r0
        
            zz += 0.5 * delta * (1.0 + cos(pi * xi))




        nodes_film.append((nid, xx, yy, zz))
        node_film[(i, j)] = nid

        nid += 1

print 'film nodes =', len(nodes_film)



#############################################################
# INDENTOR REFERENCE POINT
###############################################################

RP_IND = nid
nid += 1









#########################################################################
# SUBSTRATE ELEMENTS
#########################################################################

elems_sub = []
elem_sub = {}

eid = 1

for k in range(nz):

    for j in range(ny):

        for i in range(nx):

            n1 = node_sub[(i, j, k)]
            n2 = node_sub[(i + 1, j, k)]
            n3 = node_sub[(i + 1, j + 1, k)]
            n4 = node_sub[(i, j + 1, k)]

            n5 = node_sub[(i, j, k + 1)]
            n6 = node_sub[(i + 1, j, k + 1)]
            n7 = node_sub[(i + 1, j + 1, k + 1)]
            n8 = node_sub[(i, j + 1, k + 1)]

            elems_sub.append(
                (eid,
                 n1, n2, n3, n4,
                 n5, n6, n7, n8)
            )

            elem_sub[(i, j, k)] = eid
            eid += 1

print 'substrate elements =', len(elems_sub)

#########################################################################
# FILM ELEMENTS
#########################################################################

elems_film = []
elem_film = {}

for j in range(ny):

    for i in range(nx):

        n1 = node_film[(i, j)]
        n2 = node_film[(i + 1, j)]
        n3 = node_film[(i + 1, j + 1)]
        n4 = node_film[(i, j + 1)]

        elems_film.append(
            (eid, n1, n2, n3, n4)
        )

        elem_film[(i, j)] = eid
        eid += 1

print 'film elements =', len(elems_film)



#-----------------------------





#########################################################################
# NODE SETS
#########################################################################
eps = 1.0e-12

xmin = []
xmax = []
ymin = []
ymax = []
zmin = []

# --------------------------
# Substrate nodes
# --------------------------
for nid, x, y, z in nodes_sub:

    if abs(x) < eps:
        xmin.append(nid)

    if abs(x - Lx) < eps:
        xmax.append(nid)

    if abs(y) < eps:
        ymin.append(nid)

    if abs(y - Ly) < eps:
        ymax.append(nid)

    if abs(z) < eps:
        zmin.append(nid)

# --------------------------
# Film nodes
# --------------------------
for nid, x, y, z in nodes_film:

    if abs(x) < eps:
        xmin.append(nid)

    if abs(x - Lx) < eps:
        xmax.append(nid)

    if abs(y) < eps:
        ymin.append(nid)

    if abs(y - Ly) < eps:
        ymax.append(nid)


refnode = [node_sub[(0, 0, 0)]]



#########################################################################
# ELEMENT SETS
#########################################################################

allsub = [e[0] for e in elems_sub]
allfilm = [e[0] for e in elems_film]

#########################################################################
# SUBSTRATE TOP SURFACE
#########################################################################

surf_sub = []

for j in range(ny):

    for i in range(nx):

        surf_sub.append(
            elem_sub[(i, j, nz - 1)]
        )

#########################################################################
# FILM REGIONS
#########################################################################

film_coh = []
film_debond = []

#xmin_debond = 0.5 * (Lx - a0)
#xmax_debond = 0.5 * (Lx + a0)

for j in range(ny):

    for i in range(nx):

        xc = (i + 0.5) * dx
        yc = (j + 0.5) * dy

        eid = elem_film[(i, j)]
        
        
        dx0 = xc - xmid_debond
        dy0 = yc - ymid_debond
        rr = (dx0**2 + dy0**2)**0.5

        if rr <= r0:
            film_debond.append(eid)
        else:
            film_coh.append(eid)
        



#########################################################################
# WRITING FUNCTION
#########################################################################

def write_list(fid, values):

    n = len(values)

    for i in range(0, n, 16):

        block = values[i:i + 16]

        line = ''

        for v in block:
            line += '%d,' % v

        fid.write(line[:-1] + '\n')

#########################################################################
# WRITE INP
#########################################################################

f = open('test_mesh.inp', 'w')

f.write('*Heading\n')
f.write('Test mesh\n')

#########################################################################
# NODES
#########################################################################

f.write('*Node\n')

for n in nodes_sub:
    f.write('%d, %.8e, %.8e, %.8e\n' % n)

for n in nodes_film:
    f.write('%d, %.8e, %.8e, %.8e\n' % n)
    
    
writeRigidSphereNode(
        f,
        RP_IND,
        x_ind,
        y_ind,
        z_ind)

#########################################################################
# ELEMENTS
#########################################################################

f.write('*Element, type=C3D8R\n')

for e in elems_sub:
    f.write(
        '%d, %d, %d, %d, %d, %d, %d, %d, %d\n'
        % e
    )

f.write('*Element, type=S4R\n')

for e in elems_film:
    f.write(
        '%d, %d, %d, %d, %d\n'
        % e
    )

#########################################################################
# SETS
#########################################################################

f.write('*Nset, nset=XMIN\n')
write_list(f, xmin)

f.write('*Nset, nset=XMAX\n')
write_list(f, xmax)

f.write('*Nset, nset=YMIN\n')
write_list(f, ymin)

f.write('*Nset, nset=YMAX\n')
write_list(f, ymax)

f.write('*Nset, nset=REFNODE\n')
write_list(f, refnode)

f.write('*Nset, nset=ZMIN\n')
write_list(f, zmin)

writeRigidSphereSet(f, RP_IND)

f.write('*Elset, elset=ALLSUB\n')
write_list(f, allsub)

f.write('*Elset, elset=ALLFILM\n')
write_list(f, allfilm)

f.write('*Elset, elset=FILM_COH\n')
write_list(f, film_coh)

f.write('*Elset, elset=FILM_DEBOND\n')
write_list(f, film_debond)




f.write('*Surface, type=ELEMENT, name=SURF_FILM_COH\n')
f.write('FILM_COH, SNEG\n')

f.write('*Surface, type=ELEMENT, name=SURF_FILM_DEBOND\n')
f.write('FILM_DEBOND, SNEG\n')




f.write('*Surface, type=ELEMENT, name=SURF_SUB\n')

for eid in surf_sub:
    f.write('%d, S2\n' % eid)
    
    
f.write('*Surface, type=ELEMENT, name=SURF_FILM\n')
f.write('ALLFILM, SPOS\n')
    
writeRigidSphereSurface(f, R_ind)

#########################################################################
# FILM NODE SET
#########################################################################

film_nodes = [n[0] for n in nodes_film]

f.write('*Nset, nset=FILM\n')
write_list(f, film_nodes)

#########################################################################
# MATERIALS
#########################################################################

f.write('*Material, name=FILM_MAT\n')

f.write('*Density\n')
f.write('%e\n' % rho_film)

f.write('*Elastic\n')
f.write('%e, %f\n' % (E_film, nu_film))

f.write('*Expansion\n')
f.write('%e\n' % alpha_film)




f.write('*Material, name=SUB_MAT\n')

f.write('*Density\n')
f.write('%e\n' % rho_sub)

f.write('*Elastic\n')
f.write('%e, %f\n' % (E_sub, nu_sub))

f.write('*Expansion\n')
f.write('%e\n' % alpha_sub)

#########################################################################
# SECTIONS
#########################################################################

f.write('*Solid Section, elset=ALLSUB, material=SUB_MAT\n')
f.write(',\n')

#f.write('*Shell Section, elset=ALLFILM, OFFSET=-0.5, material=FILM_MAT\n')
f.write('*Shell Section, elset=ALLFILM, material=FILM_MAT\n')

f.write('%e, 5\n' % hf)

#########################################################################
# DELTA T
#########################################################################

def deltaT():

    da = alpha_film - alpha_sub

    return sigma0 * (1.0 - nu_film) / (E_film * da)

#########################################################################
# HUTCHINSON TABLE
#########################################################################

def hutchinson_table(npts=21):

    txt = ''

    for i in range(npts):

        phi = float(i) / float(npts - 1)
        psi = 0.5 * pi * phi

        value = eta * psi

        if abs(value - pi / 2.0) < 1.0e-8:
            value = pi / 2.0 - 1.0e-8

        Gc = GIc * (1.0 + tan(value) ** 2)

        txt += '%e, %f, 0.\n' % (Gc, phi)

    return txt

#########################################################################
# INTERACTION PROPERTIES
#########################################################################

f.write('*Surface Interaction, name=IntProp-1\n')
f.write('*Surface Behavior, pressure-overclosure=HARD\n')
f.write('*Cohesive Behavior\n')

f.write('*Damage Initiation, criterion=QUADS\n')
f.write('%e, %e, %e\n'
        % (Tn_max,
           Tt_max,
           Ts_max))

f.write('*Damage Evolution, type=ENERGY,mixed mode behavior=TABULAR,mode mix ratio=TRACTION\n')
f.write(hutchinson_table())

f.write('*Surface Interaction, name=IntProp-2\n')
f.write('*Surface Behavior, pressure-overclosure=HARD\n')
#f.write('*Surface Interaction, name=IntProp-1\n')
#f.write('*Cohesive Behavior\n')

#########################################################################
# CONTACT PAIRS
#########################################################################

#f.write('*Contact Pair, interaction=IntProp-1\n')
#f.write('SURF_FILM_COH, SURF_SUB\n')

#f.write('*Contact Pair, interaction=IntProp-2\n')
#f.write('SURF_FILM_DEBOND, SURF_SUB\n')


#########################################################################
# GENERAL CONTACT
#########################################################################

f.write('*Contact, op=NEW\n')

f.write('*Contact Inclusions\n')
f.write('INDENTER, SURF_FILM\n')
f.write('SURF_FILM_COH, SURF_SUB\n')
f.write('SURF_FILM_DEBOND, SURF_SUB\n')

f.write('*Contact Property Assignment\n')
f.write(', , IntProp-2\n')
f.write('SURF_FILM_COH, SURF_SUB, IntProp-1\n')


f.write('SURF_FILM_DEBOND, SURF_SUB, IntProp-2\n')



#########################################################################
# STEP
#########################################################################
#########################################################################
# AMPLITUDE
#########################################################################

f.write('*Amplitude, name=Amp-1, definition=SMOOTH STEP\n')
f.write('0., 0., 0.002, 1.\n')


f.write('*Amplitude, name=Amp-2, definition=SMOOTH STEP\n')
f.write('0., 0., 2.E-3, 1.\n')

f.write('*Amplitude, name=Amp-3, definition=SMOOTH STEP\n')
f.write('0., 0., 0.0025, 0., 0.004, 1.\n')



# =============================================================================
# t=0
# |
# |---- thermal ramp ----|
# 0                 0.002 s
# 
# σ = σ0
# ____________________________________
# 
# |------------------------|
# 0                    0.10 s
# 
# Hertz pressure = 0
# 
# |-- indentation ramp --|
# 0.0025            0.004 s
# 
# Hertz pressure
#          ________
#         /
# _______/
# 
# 0.0025                     0.100 s
# 
# =============================================================================




f.write('*Step, name=Loading, nlgeom=YES\n')

#f.write('*Dynamic, Explicit\n')
#f.write('%e\n' % step_time)
f.write('*Dynamic, Explicit\n')
f.write('0., %e\n' % step_time)

f.write('*Bulk Viscosity\n')
f.write('0.06, 1.2\n')



#########################################################################
# MASS SCALING
#########################################################################
f.write('*Variable Mass Scaling,frequency=10, type=BELOW MIN, dt=%e\n'
        % mass_dt)




#########################################################################
# TEMPERATURE
#########################################################################

f.write('*Temperature, amplitude=Amp-1\n')
f.write('FILM, %e\n' % deltaT())


#########################################################################
# VISCOUS PRESSURE
#########################################################################

f.write('*Dsload, amplitude=Amp-2\n')
f.write('SURF_FILM, VP, %e\n' % visc)


#########################################################################
# INDENTER DISPLACEMENT
#########################################################################


f.write('*Boundary, amplitude=Amp-3\n')
f.write('RP_INDENTER, 3, 3, -%e\n' % indent)




#########################################################################






#########################################################################
# BOUNDARY CONDITIONS
#########################################################################


f.write('*Boundary\n')

f.write('XMIN, XSYMM\n')
f.write('XMAX, XSYMM\n')

f.write('YMIN, YSYMM\n')
f.write('YMAX, YSYMM\n')

f.write('ZMIN, 1, 3\n')



#########################################################################
# INDENTER
#########################################################################

f.write('*Boundary\n')
f.write('RP_INDENTER, 1, 1\n')   # U1 = 0
f.write('RP_INDENTER, 2, 2\n')   # U2 = 0
f.write('RP_INDENTER, 4, 6\n')   # UR1, UR2, UR3 = 0




#########################################################################
# FIELD OUTPUT
#########################################################################

f.write('*Output, field, time interval=2.5e-5\n')

f.write('*Node Output\n')
f.write('A, RF, U, V\n')

f.write('*Element Output, directions=YES\n')
f.write('S\n')

f.write('*Contact Output\n')
f.write('CSTRESS, CDISP, CSDMG,CPRESS\n')

f.write('*Node Output, nset=RP_INDENTER\n')
f.write('U, RF\n')





f.write('*Output, history, variable=PRESELECT\n')

#########################################################################
# END STEP
#########################################################################

f.write('*End Step\n')

#########################################################################
# CLOSE FILE
#########################################################################

f.close()

print 'test_mesh.inp written'
print 'Delta T =', deltaT()







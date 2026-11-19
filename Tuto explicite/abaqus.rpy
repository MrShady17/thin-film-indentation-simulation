# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by maenhaua on Thu Nov 19 10:37:41 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=257.439575195312, 
    height=107.930557250977)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=20.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, 0.0), point2=(3.5, 0.0))
s.HorizontalConstraint(entity=g[2], addUndoState=False)
s.Line(point1=(0.0, 0.0), point2=(3.50537490844727, 0.0))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
s.CoincidentConstraint(entity1=v[1], entity2=g[2], addUndoState=False)
s.Line(point1=(0.0, 0.0), point2=(0.0, 2.5))
s.VerticalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.5849, 
    farPlane=20.1274, cameraPosition=(1.92455, 1.49686, 18.8562), 
    cameraTarget=(1.92455, 1.49686, 0))
s.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(-0.701839923858643, 
    1.82741022109985), value=3.0)
s.delete(objectList=(g[2], ))
s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(1.18739533424377, 
    -0.728842735290527), value=3.0)
s.Arc3Points(point1=(0.0, 3.0), point2=(3.0, 0.0), point3=(2.5, 1.625))
p = mdb.models['Model-1'].Part(name='Disque', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Disque']
p.BaseSolidExtrude(sketch=s, depth=0.5)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Disque']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.41362, 
    farPlane=11.3738, width=3.39906, height=2.94553, cameraPosition=(6.60614, 
    -4.02183, 4.99819), cameraUpVector=(-0.494793, 0.618877, 0.610058), 
    cameraTarget=(1.5825, 1.47912, 0.18838))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.337, 
    farPlane=11.5219, width=3.35845, height=2.91034, cameraPosition=(6.0414, 
    -6.18673, 0.435097), cameraUpVector=(-0.194641, 0.304229, 0.932502), 
    cameraTarget=(1.58083, 1.47273, 0.174907))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.92015, 
    farPlane=10.8093, width=3.66751, height=3.17816, cameraPosition=(1.92291, 
    -5.64548, 5.47984), cameraUpVector=(-0.196551, 0.811737, 0.549955), 
    cameraTarget=(1.55224, 1.47649, 0.209933))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.43277, 
    farPlane=11.3277, width=3.40921, height=2.95432, cameraPosition=(-0.853317, 
    -6.97231, -0.992975), cameraUpVector=(0.0378936, 0.199403, 0.979185), 
    cameraTarget=(1.55309, 1.4769, 0.211927))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.56171, 
    farPlane=11.1808, width=3.47754, height=3.01354, cameraPosition=(-0.129194, 
    -6.96875, 2.33072), cameraUpVector=(0.0663693, 0.545825, 0.835267), 
    cameraTarget=(1.55413, 1.47691, 0.21671))
p = mdb.models['Model-1'].parts['Disque']
p.features['Solid extrude-1'].setValues(depth=0.1)
p = mdb.models['Model-1'].parts['Disque']
p.regenerate()
p = mdb.models['Model-1'].parts['Disque']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.62232, 
    farPlane=11.1668, width=3.50966, height=3.04137, cameraPosition=(2.96868, 
    -7.26678, -0.307548), cameraUpVector=(-0.136449, 0.260666, 0.955738), 
    cameraTarget=(1.572, 1.47519, 0.201488))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.49523, 
    farPlane=11.4814, width=4.766, height=2.983, cameraPosition=(6.36141, 
    -5.16979, 3.61219), cameraUpVector=(-0.353296, 0.569712, 0.742031), 
    cameraTarget=(1.58234, 1.48158, 0.213433))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.95664, 
    farPlane=10.8741, width=5.10457, height=3.19491, cameraPosition=(-6.46257, 
    1.0462, -3.93609), cameraUpVector=(-0.000328004, -0.591096, 0.806601), 
    cameraTarget=(1.40991, 1.56516, 0.111938))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.73607, 
    farPlane=11.1222, width=4.94272, height=3.09361, cameraPosition=(-1.93874, 
    7.74205, -5.33102), cameraUpVector=(-0.71894, -0.643365, 0.263071), 
    cameraTarget=(1.43422, 1.60115, 0.104441))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.76347, 
    farPlane=10.8877, width=4.96283, height=3.10619, cameraPosition=(2.87878, 
    -5.95397, -4.47009), cameraUpVector=(-0.811131, -0.109932, 0.57444), 
    cameraTarget=(1.4675, 1.50654, 0.110388))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.67816, 
    farPlane=11.0722, width=4.90024, height=3.06701, cameraPosition=(-0.810434, 
    -5.86206, 4.43539), cameraUpVector=(-0.527112, 0.773701, 0.351482), 
    cameraTarget=(1.485, 1.5061, 0.0681428))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.80362, 
    farPlane=10.9605, width=4.9923, height=3.12463, cameraPosition=(6.90602, 
    5.04707, 6.13969), cameraUpVector=(-0.810693, 0.576956, -0.0994983), 
    cameraTarget=(1.49172, 1.5156, 0.0696278))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.68319, 
    farPlane=11.0645, width=4.90393, height=3.06932, cameraPosition=(6.14079, 
    -3.4094, 5.80381), cameraUpVector=(-0.0156128, 0.950272, 0.311031), 
    cameraTarget=(1.49046, 1.50169, 0.0690751))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((210000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
    material='Steel', thickness=None)
p = mdb.models['Model-1'].parts['Disque']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['Model-1'].parts['Disque']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Disque']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=20.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.ConstructionLine(point1=(0.0, -10.0), point2=(0.0, 10.0))
s1.FixedConstraint(entity=g[2])
s1.Line(point1=(0.0, 0.0), point2=(4.0, 0.0))
s1.HorizontalConstraint(entity=g[3], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
#: Warning: Coincident point selected.
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.8842, 
    farPlane=19.8282, width=8.79109, height=5.50228, cameraPosition=(0.681409, 
    0.258891, 18.8562), cameraTarget=(0.681409, 0.258891, 0))
s1.Line(point1=(0.0, 0.0), point2=(0.0, 2.49542808532715))
s1.VerticalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1686, 
    farPlane=20.5438, width=15.2637, height=9.55345, cameraPosition=(-0.725874, 
    -0.414738, 18.8562), cameraTarget=(-0.725874, -0.414738, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(4.22421, 
    3.65178, 18.8562), cameraTarget=(4.22421, 3.65178, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2023, 
    farPlane=20.5101, cameraPosition=(4.40797, 2.11681, 18.8562), 
    cameraTarget=(4.40797, 2.11681, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2017, 
    farPlane=20.5107, width=14.9647, height=9.36629, cameraPosition=(4.34244, 
    2.42765, 18.8562), cameraTarget=(4.34244, 2.42765, 0))
s1.Line(point1=(4.0, 0.0), point2=(4.0, 2.5))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
#: Warning: Same line was selected.
s1.delete(objectList=(g[2], ))
s1.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(-0.70772123336792, 
    1.50674867630005), value=5.0)
s1.Arc3Points(point1=(0.0, 5.0), point2=(4.0, 2.5), point3=(3.25, 3.625))
s1.ObliqueDimension(vertex1=v[1], vertex2=v[3], textPoint=(5.5754246711731, 
    1.25967621803284), value=1.5)
s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(2.52393198013306, 
    -0.7842857837677), value=2.0)
s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(0.868695259094238, 
    -0.705672025680542), value=3.0)
s1.delete(objectList=(d[2], d[3]))
s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(0.643492937088013, 
    -0.582135915756226), value=4.0)
s1.delete(objectList=(d[0], ))
s1.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(-0.70772123336792, 
    2.95549130439758), value=7.0)
s1.undo()
s1.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(-0.493778705596924, 
    2.50626873970032), value=5.0)
s1.RadialDimension(curve=g[6], textPoint=(4.15664958953857, 4.04485607147217), 
    radius=4.0)
s1.autoConstrain(objectList=(g[3], g[4], g[5], g[6]))
#: 0 constraints added
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=20.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -10.0), point2=(0.0, 10.0))
s.FixedConstraint(entity=g[2])
s.delete(objectList=(g[2], c[2]))
s.rectangle(point1=(0.0, 0.0), point2=(1.0, 3.0))
s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-0.610114097595215, 
    1.41007161140442), value=3.0)
s.ObliqueDimension(vertex1=v[3], vertex2=v[0], textPoint=(0.189346313476562, 
    -0.553956985473633), value=1.0)
s.ConstructionLine(point1=(0.0, 3.25), point2=(0.0, -1.0))
s.VerticalConstraint(entity=g[7], addUndoState=False)
s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(2.20903587341309, 
    0.956834077835083), value=3.0)
s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(0.298746109008789, 
    3.2314145565033), value=1.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.37, 
    farPlane=20.3424, width=13.9964, height=8.76024, cameraPosition=(
    -0.0610723, -0.0756621, 18.8562), cameraTarget=(-0.0610723, -0.0756621, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1181, 
    farPlane=21.2517, cameraPosition=(16.246, 1.41097, 9.76959), 
    cameraUpVector=(0.187778, 0.860353, -0.473848), cameraTarget=(-0.432057, 
    0.248211, 1.04916))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1003, 
    farPlane=20.676, cameraPosition=(0.777385, 1.71807, 18.9571), 
    cameraUpVector=(7.4774e-05, 0.995505, -0.0947042), cameraTarget=(
    -0.0611827, -0.065856, 0.204256))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(3.81808, 
    2.94937, 18.704), cameraTarget=(2.97951, 1.16544, -0.0488456))
s.delete(objectList=(d[2], ))
s.delete(objectList=(d[3], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.831, 
    farPlane=20.0375, width=7.96289, height=4.98392, cameraPosition=(2.51778, 
    2.89123, 18.7677), cameraTarget=(1.67921, 1.1073, 0.0148312))
s.Spot(point=(0.0, 0.0))
s.CoincidentConstraint(entity1=v[4], entity2=g[3], addUndoState=False)
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseSolidRevolve(sketch=s, angle=90.0, flipRevolveDirection=OFF)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.92659, 
    farPlane=10.2371, width=4.62317, height=2.89361, cameraPosition=(5.12971, 
    6.23872, 5.12971), cameraUpVector=(-0.661832, 0.570639, -0.486157))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.49993, 
    farPlane=9.59628, width=5.07042, height=3.17354, cameraPosition=(7.20803, 
    3.2561, 4.58623), cameraUpVector=(-0.454012, 0.852565, -0.258858), 
    cameraTarget=(0.463664, 1.57267, 0.463659))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.30679, 
    farPlane=9.84454, width=4.91976, height=3.07924, cameraPosition=(7.13423, 
    4.14521, -3.26991), cameraUpVector=(-0.693204, 0.720475, -0.0195852), 
    cameraTarget=(0.463973, 1.56894, 0.496581))
p = mdb.models['Model-1'].parts['Part-2']
s1 = p.features['Solid revolve-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid revolve-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.45655, 
    farPlane=9.25284, width=8.63451, height=5.40427, cameraPosition=(0.458371, 
    1.10263, 8.3547), cameraTarget=(0.458371, 1.10263, 0))
s2.delete(objectList=(g[3], g[4], g[5], g[6], g[7], v[4], d[0], d[1], c[19], 
    c[20], c[21], c[22], c[23], c[24], c[25]))
s2.Line(point1=(0.0, 0.0), point2=(2.0, 0.0))
s2.HorizontalConstraint(entity=g[8], addUndoState=False)
s2.Line(point1=(2.0, 0.0), point2=(2.0, 1.0))
s2.VerticalConstraint(entity=g[9], addUndoState=False)
s2.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.4664, 
    farPlane=10.243, width=18.1536, height=11.3622, cameraPosition=(0.947502, 
    -1.57541, 8.3547), cameraTarget=(0.947502, -1.57541, 0))
s2.Line(point1=(0.0, 0.0), point2=(0.0, 4.0))
s2.VerticalConstraint(entity=g[10], addUndoState=False)
s2.PerpendicularConstraint(entity1=g[8], entity2=g[10], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(4.14384, 
    2.30735, 8.3547), cameraTarget=(4.14384, 2.30735, 0))
s2.Arc3Points(point1=(0.0, 4.0), point2=(2.0, 1.0), point3=(1.5, 2.75))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.25959, 
    farPlane=10.4498, width=18.9494, height=11.8603, cameraPosition=(4.50447, 
    2.09882, 8.3547), cameraTarget=(4.50447, 2.09882, 0))
s2.Spot(point=(0.0, 0.0))
s2.CoincidentConstraint(entity1=v[10], entity2=g[8], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.21416, 
    farPlane=10.4952, width=20.5786, height=12.88, cameraPosition=(4.72224, 
    1.99522, 8.3547), cameraTarget=(4.72224, 1.99522, 0))
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['Disque']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=20.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -10.0), point2=(0.0, 10.0))
s.FixedConstraint(entity=g[2])
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.346, 
    farPlane=21.3663, width=24.6452, height=15.4253, cameraPosition=(-0.561641, 
    -1.68251, 18.8562), cameraTarget=(-0.561641, -1.68251, 0))
s.Line(point1=(0.0, 4.0), point2=(0.0, 0.0190777778625488))
s.VerticalConstraint(entity=g[3], addUndoState=False)
s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
s.CoincidentConstraint(entity1=v[1], entity2=g[2], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.992, 
    farPlane=20.7203, width=16.8604, height=10.5528, cameraPosition=(0.724269, 
    0.199898, 18.8562), cameraTarget=(0.724269, 0.199898, 0))
s.Line(point1=(0.0, 0.0190777778625488), point2=(3.5, 0.0190777778625488))
s.HorizontalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(3.5, 0.0190777778625488), point2=(2.5, 3.0))
s.Arc3Points(point1=(0.0, 4.0), point2=(2.5, 3.0), point3=(1.875, 3.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.302, 
    farPlane=20.4104, width=14.0574, height=8.7984, cameraPosition=(0.612835, 
    0.195564, 18.8562), cameraTarget=(0.612835, 0.195564, 0))
s.Spot(point=(3.5, 0.0190777778625488))
s.CoincidentConstraint(entity1=v[5], entity2=g[4], addUndoState=False)
p = mdb.models['Model-1'].Part(name='Indent', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Indent']
p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Indent']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.8337, 
    farPlane=30.2852, width=11.5556, height=7.23258, cameraPosition=(13.7838, 
    15.249, 13.7838), cameraUpVector=(-0.83871, 0.492903, -0.231543), 
    cameraTarget=(0.181741, 1.647, 0.181741))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.5354, 
    farPlane=30.0616, width=12.0373, height=7.53406, cameraPosition=(18.7507, 
    2.66918, 14.6453), cameraUpVector=(-0.40083, 0.911443, -0.092775), 
    cameraTarget=(0.181747, 1.64699, 0.181742))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.4518, 
    farPlane=30.2476, width=11.9799, height=7.49815, cameraPosition=(19.2312, 
    -0.675887, 13.8525), cameraUpVector=(-0.256162, 0.965013, -0.0559624), 
    cameraTarget=(0.186575, 1.61338, 0.173777))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2994, 
    farPlane=30.1625, width=11.8753, height=7.43267, cameraPosition=(20.5452, 
    6.78776, 10.8792), cameraUpVector=(-0.517739, 0.842415, -0.149275), 
    cameraTarget=(0.202568, 1.70422, 0.137587))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.7684, 
    farPlane=29.1923, width=12.1972, height=7.63417, cameraPosition=(12.1105, 
    21.649, 4.36492), cameraUpVector=(-0.976094, 0.207193, -0.0656546), 
    cameraTarget=(0.141608, 1.81163, 0.0905071))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.4113, 
    farPlane=28.8834, width=12.6385, height=7.9104, cameraPosition=(23.4784, 
    1.92653, -2.82616), cameraUpVector=(-0.344252, 0.937524, -0.0504004), 
    cameraTarget=(0.103327, 1.87805, 0.114723))
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.5708, 
    farPlane=29.881, width=12.0615, height=7.54927, cameraPosition=(22.0923, 
    -2.67955, 7.27178), cameraUpVector=(-0.142444, 0.989282, -0.032094), 
    cameraTarget=(0.0981716, 1.86092, 0.152281))
p1 = mdb.models['Model-1'].parts['Disque']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['Indent']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Indent']
p.features['Solid revolve-1'].setValues(angle=90.0)
p = mdb.models['Model-1'].parts['Indent']
p.regenerate()
p = mdb.models['Model-1'].parts['Indent']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.2502, 
    farPlane=26.4418, width=8.70426, height=5.44793, cameraPosition=(21.6394, 
    -1.33224, -9.03503), cameraUpVector=(-0.224341, 0.973728, -0.0390653), 
    cameraTarget=(0.28276, 2.38205, 1.29482))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.4458, 
    farPlane=26.7578, width=8.34052, height=5.22027, cameraPosition=(14.007, 
    20.8071, 4.64352), cameraUpVector=(-0.834112, 0.045681, 0.5497), 
    cameraTarget=(0.672521, 1.25148, 0.596308))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0517, 
    farPlane=27.4146, width=8.61448, height=5.39174, cameraPosition=(14.4718, 
    12.5736, -14.5912), cameraUpVector=(-0.359953, 0.683246, 0.635301), 
    cameraTarget=(0.643505, 1.76546, 1.79703))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3539, 
    farPlane=25.7652, width=8.75111, height=5.47725, cameraPosition=(8.59995, 
    1.61981, 23.2461), cameraUpVector=(-0.294446, 0.927377, -0.230811), 
    cameraTarget=(0.840536, 2.13302, 0.527398))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.5853, 
    farPlane=27.3061, width=8.40356, height=5.25972, cameraPosition=(-11.1521, 
    15.5995, 14.9959), cameraUpVector=(0.483179, 0.549887, -0.681294), 
    cameraTarget=(2.11287, 1.23252, 1.05884))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.6025, 
    farPlane=26.5904, width=8.86351, height=5.5476, cameraPosition=(-19.4997, 
    11.0602, 1.97959), cameraUpVector=(0.668859, 0.705542, -0.234175), 
    cameraTarget=(2.50105, 1.44361, 1.66413))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0138, 
    farPlane=27.2466, width=8.59734, height=5.38101, cameraPosition=(-15.5097, 
    10.2781, -11.2426), cameraUpVector=(0.670746, 0.720362, 0.176573), 
    cameraTarget=(2.34276, 1.47464, 2.18868))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3514, 
    farPlane=26.8495, width=8.75, height=5.47656, cameraPosition=(-18.9222, 
    11.9151, -1.12091), cameraUpVector=(0.724784, 0.671949, -0.152224), 
    cameraTarget=(2.47296, 1.41218, 1.80249))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.4864, 
    farPlane=26.7604, width=8.81104, height=5.51476, cameraPosition=(-19.0416, 
    5.6985, 11.1759), cameraUpVector=(0.412075, 0.870468, -0.269222), 
    cameraTarget=(2.47768, 1.65768, 1.31687))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3239, 
    farPlane=26.7653, width=8.73754, height=5.46876, cameraPosition=(-7.21806, 
    6.87257, 22.4147), cameraUpVector=(0.236737, 0.846441, -0.476963), 
    cameraTarget=(2.02298, 1.61253, 0.884656))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.1023, 
    farPlane=26.7966, width=8.63735, height=5.40605, cameraPosition=(14.9398, 
    6.75673, 19.9219), cameraUpVector=(-0.0828015, 0.80907, -0.581851), 
    cameraTarget=(1.09218, 1.6174, 0.989374))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7228, 
    farPlane=26.3293, width=8.91794, height=5.58167, cameraPosition=(-19.4711, 
    1.07022, 10.6387), cameraUpVector=(0.216191, 0.939408, -0.266035), 
    cameraTarget=(2.68644, 1.88086, 1.41947))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3507, 
    farPlane=26.6967, width=8.74971, height=5.47638, cameraPosition=(-14.7815, 
    4.2138, 17.6238), cameraUpVector=(0.213383, 0.893406, -0.395339), 
    cameraTarget=(2.4855, 1.74616, 1.12017))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.2896, 
    farPlane=26.7548, width=8.7221, height=5.4591, cameraPosition=(-13.0236, 
    5.15083, 19.1262), cameraUpVector=(0.208742, 0.877414, -0.431939), 
    cameraTarget=(2.40999, 1.70591, 1.05563))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.9423, 
    farPlane=26.079, width=9.01722, height=5.64381, cameraPosition=(-20.6067, 
    1.96138, 7.1992), cameraUpVector=(0.293388, 0.929186, -0.224804), 
    cameraTarget=(2.73624, 1.84313, 1.56876))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.46, 
    farPlane=26.4337, width=8.79912, height=5.5073, cameraPosition=(9.86229, 
    4.42467, -19.5794), cameraUpVector=(-0.255672, 0.893362, 0.369508), 
    cameraTarget=(1.40943, 1.73586, 2.73487))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0049, 
    farPlane=26.8577, width=8.59334, height=5.3785, cameraPosition=(18.7849, 
    7.43125, 16.113), cameraUpVector=(-0.482732, 0.828834, -0.28285), 
    cameraTarget=(0.995007, 1.59622, 1.07709))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.4784, 
    farPlane=26.3313, width=8.80745, height=5.51251, cameraPosition=(-8.52697, 
    3.28554, 22.1807), cameraUpVector=(0.00785258, 0.901268, -0.433191), 
    cameraTarget=(2.28291, 1.79171, 0.790965))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3803, 
    farPlane=26.3961, width=8.76309, height=5.48475, cameraPosition=(-16.373, 
    2.83992, 15.7057), cameraUpVector=(0.167411, 0.903954, -0.393499), 
    cameraTarget=(2.66237, 1.81326, 1.10412))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.2938, 
    farPlane=26.3995, width=8.72399, height=5.46028, cameraPosition=(-19.8189, 
    6.68549, 7.65913), cameraUpVector=(0.416812, 0.802787, -0.426381), 
    cameraTarget=(2.83166, 1.62434, 1.49942))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3765, 
    farPlane=26.2725, width=8.7614, height=5.48369, cameraPosition=(-20.2185, 
    7.05292, -1.84731), cameraUpVector=(0.578838, 0.737811, -0.347248), 
    cameraTarget=(2.85205, 1.60559, 1.98457))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.8723, 
    farPlane=26.8347, width=8.53343, height=5.341, cameraPosition=(-12.4455, 
    -4.45015, -14.9549), cameraUpVector=(-0.062362, 0.989095, 0.133424), 
    cameraTarget=(2.44742, 2.20439, 2.66689))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3834, 
    farPlane=26.2698, width=8.76454, height=5.48565, cameraPosition=(-19.5701, 
    10.164, 1.5324), cameraUpVector=(0.645793, 0.733815, -0.210874), 
    cameraTarget=(2.8088, 1.46312, 1.83061))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.8247, 
    farPlane=26.8722, width=8.5119, height=5.32752, cameraPosition=(-17.2079, 
    10.4607, 11.3031), cameraUpVector=(0.606205, 0.748285, -0.269417), 
    cameraTarget=(2.68606, 1.4477, 1.32291))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0003, 
    farPlane=26.5991, width=8.59129, height=5.37721, cameraPosition=(-12.7098, 
    6.25425, -15.3599), cameraUpVector=(0.617241, 0.777164, 0.122595), 
    cameraTarget=(2.45686, 1.66203, 2.68149))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.7782, 
    farPlane=26.784, width=8.49088, height=5.31437, cameraPosition=(-16.9391, 
    14.2213, -2.78963), cameraUpVector=(0.78735, 0.608957, 0.0961876), 
    cameraTarget=(2.68186, 1.23818, 2.01274))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0043, 
    farPlane=26.5964, width=8.59312, height=5.37836, cameraPosition=(-18.6234, 
    11.3094, -2.53106), cameraUpVector=(0.700279, 0.713561, 0.0209775), 
    cameraTarget=(2.77291, 1.39559, 1.99876))
session.viewports['Viewport: 1'].view.setValues(nearPlane=18.8699, 
    farPlane=26.7211, width=8.53233, height=5.34031, cameraPosition=(-17.624, 
    13.2695, 5.93734), cameraUpVector=(0.773182, 0.633402, 0.0314769), 
    cameraTarget=(2.71977, 1.29137, 1.54851))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.4223, 
    farPlane=26.2403, width=8.78211, height=5.49665, cameraPosition=(-20.2506, 
    7.23106, 4.91283), cameraUpVector=(0.565406, 0.810214, 0.154498), 
    cameraTarget=(2.86001, 1.61378, 1.60321))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Indent']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Set-1')
p = mdb.models['Model-1'].parts['Indent']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Disque']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Indent']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Indent']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Disque']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Disque']
p.seedPart(size=0.21, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Disque']
p.generateMesh()
p = mdb.models['Model-1'].parts['Disque']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Disque']
p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Disque']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.84283, 
    farPlane=10.2144, width=4.02575, height=2.52729, cameraPosition=(3.64383, 
    -3.27253, 6.78528), cameraUpVector=(-0.459267, 0.831089, 0.313632))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.05895, 
    farPlane=10.9886, width=3.56458, height=2.23778, cameraPosition=(6.85115, 
    -4.57811, 2.71022), cameraUpVector=(-0.429062, 0.435421, 0.7914), 
    cameraTarget=(1.49158, 1.49605, 0.0533062))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.63126, 
    farPlane=10.4192, width=3.90128, height=2.44915, cameraPosition=(5.68585, 
    -2.66802, 6.19703), cameraUpVector=(-0.546651, 0.731977, 0.406673), 
    cameraTarget=(1.49178, 1.49572, 0.0527096))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.82328, 
    farPlane=10.2268, width=4.01425, height=2.52007, cameraPosition=(5.5183, 
    -1.51045, 6.93964), cameraUpVector=(-0.588883, 0.763552, 0.264964), 
    cameraTarget=(1.49178, 1.49572, 0.0527092))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.05101, 
    farPlane=9.9994, width=4.14823, height=2.60418, cameraPosition=(5.06465, 
    -0.58198, 7.50908), cameraUpVector=(-0.596454, 0.792761, 0.125587), 
    cameraTarget=(1.49179, 1.4957, 0.0526958))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.16717, 
    farPlane=10.8777, width=3.62825, height=2.27775, cameraPosition=(7.85337, 
    -2.84477, 3.70923), cameraUpVector=(-0.698313, 0.208163, 0.684855), 
    cameraTarget=(1.49178, 1.49571, 0.0527119))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.08357, 
    farPlane=10.956, width=3.57907, height=2.24687, cameraPosition=(8.92888, 
    -2.66321, -0.206563), cameraUpVector=(-0.533644, -0.320087, 0.782795), 
    cameraTarget=(1.49143, 1.49565, 0.0540007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.4186, 
    farPlane=9.60945, width=4.36449, height=2.73994, cameraPosition=(4.0199, 
    2.71365, -7.99151), cameraUpVector=(0.232516, -0.929951, 0.28483), 
    cameraTarget=(1.49457, 1.49221, 0.058983))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.93504, 
    farPlane=11.1, width=3.49169, height=2.19201, cameraPosition=(6.94647, 
    -4.9961, -0.777799), cameraUpVector=(-0.777655, -0.286807, 0.559459), 
    cameraTarget=(1.49072, 1.50236, 0.0494843))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.67191, 
    farPlane=10.3536, width=3.9252, height=2.46416, cameraPosition=(7.52679, 
    3.57536, 5.69248), cameraUpVector=(-0.785218, -0.391065, 0.480105), 
    cameraTarget=(1.49019, 1.4946, 0.0436261))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.14281, 
    farPlane=9.88444, width=4.20224, height=2.63808, cameraPosition=(5.23774, 
    2.86677, 7.57616), cameraUpVector=(-0.87668, -0.459603, 0.14212), 
    cameraTarget=(1.49355, 1.49564, 0.0408642))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.60257, 
    farPlane=9.42603, width=4.47272, height=2.80788, cameraPosition=(3.35354, 
    1.94871, 8.34797), cameraUpVector=(-0.876601, -0.465827, -0.120728), 
    cameraTarget=(1.49612, 1.49689, 0.0398116))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.06558, 
    farPlane=10.9666, width=3.56849, height=2.24022, cameraPosition=(4.81176, 
    -6.31743, 0.716015), cameraUpVector=(-0.668853, 0.141739, 0.729758), 
    cameraTarget=(1.49425, 1.50751, 0.0496137))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.43644, 
    farPlane=10.5989, width=3.78667, height=2.37719, cameraPosition=(-1.32367, 
    -5.14288, 4.57216), cameraUpVector=(-0.416289, 0.840428, 0.346963), 
    cameraTarget=(1.50084, 1.50625, 0.0454725))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.20925, 
    farPlane=9.82391, width=4.24132, height=2.66261, cameraPosition=(4.27654, 
    -0.548627, 7.83627), cameraUpVector=(-0.592845, 0.803207, 0.0582538), 
    cameraTarget=(1.49586, 1.50217, 0.0425723))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.4574, 
    farPlane=9.57586, width=4.38731, height=2.75426, cameraPosition=(4.11052, 
    0.984688, 8.14028), cameraUpVector=(-0.635051, 0.766348, -0.0970608), 
    cameraTarget=(1.49603, 1.50061, 0.0422633))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.45159, 
    farPlane=10.5801, width=3.79558, height=2.38278, cameraPosition=(8.01503, 
    -0.831187, 5.01382), cameraUpVector=(-0.60228, 0.615788, 0.508001), 
    cameraTarget=(1.49209, 1.50244, 0.0454214))
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.63382, 
    farPlane=10.3979, width=2.65871, height=1.66909, viewOffsetX=-0.404766, 
    viewOffsetY=-0.0395564)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.50288, 
    farPlane=11.025, width=2.60623, height=1.63615, cameraPosition=(6.06618, 
    -5.20384, 3.38329), cameraUpVector=(-0.6658, 0.285134, 0.689499), 
    cameraTarget=(1.56118, 1.40089, 0.423219), viewOffsetX=-0.396777, 
    viewOffsetY=-0.0387757)
p = mdb.models['Model-1'].parts['Disque']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Disque']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Disque']
p.generateMesh()
p = mdb.models['Model-1'].parts['Disque']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Disque']
p.seedPart(size=0.005, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Disque']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.50833, 
    farPlane=11.0195, width=2.60843, height=1.63752, cameraPosition=(6.13126, 
    -5.20941, 3.27182), cameraUpVector=(-0.500495, 0.426518, 0.753384), 
    cameraTarget=(1.62626, 1.39532, 0.31175), viewOffsetX=-0.39711, 
    viewOffsetY=-0.0388082)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.20253, 
    farPlane=10.4661, width=2.88666, height=1.81218, cameraPosition=(3.90068, 
    -3.62392, 6.83745), cameraUpVector=(-0.65747, 0.675257, 0.334306), 
    cameraTarget=(1.53944, 1.46384, 0.417274), viewOffsetX=-0.439467, 
    viewOffsetY=-0.0429476)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.15699, 
    farPlane=10.8069, width=2.86841, height=1.80072, cameraPosition=(2.1125, 
    -6.44295, 4.22272), cameraUpVector=(-0.851712, 0.426133, 0.304955), 
    cameraTarget=(1.32374, 1.23694, 0.606567), viewOffsetX=-0.436689, 
    viewOffsetY=-0.0426761)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.33934, 
    farPlane=10.6246, width=1.18507, height=0.743962, viewOffsetX=-1.03885, 
    viewOffsetY=0.352608)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.34192, 
    farPlane=10.622, width=1.18548, height=0.744224, cameraPosition=(2.03405, 
    -6.41553, 4.29806), cameraUpVector=(-0.886867, 0.393182, 0.242643), 
    cameraTarget=(1.24529, 1.26436, 0.681903), viewOffsetX=-1.03922, 
    viewOffsetY=0.352732)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.41538, 
    farPlane=10.5486, width=1.01647, height=0.638124, viewOffsetX=-1.22372, 
    viewOffsetY=0.544321)
p = mdb.models['Model-1'].parts['Disque']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Disque']
p.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Disque']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.23218, 
    farPlane=10.7318, width=2.28486, height=1.43439, viewOffsetX=-1.36265, 
    viewOffsetY=0.397951)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.37921, 
    farPlane=8.85434, width=2.01538, height=1.26522, cameraPosition=(4.00849, 
    4.44881, 6.82946), cameraUpVector=(-0.959858, -0.235917, 0.151709), 
    cameraTarget=(0.265723, 2.81868, -0.654778), viewOffsetX=-1.20194, 
    viewOffsetY=0.351017)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.32653, 
    farPlane=8.90702, width=2.88252, height=1.80959, viewOffsetX=-1.06092, 
    viewOffsetY=0.312599)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.58215, 
    farPlane=9.11065, width=2.54336, height=1.59668, cameraPosition=(5.91855, 
    4.89147, 5.10767), cameraUpVector=(-0.891681, -0.0881481, 0.443998), 
    cameraTarget=(0.0640973, 2.69242, -0.68621), viewOffsetX=-0.936094, 
    viewOffsetY=0.275819)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.9794, 
    farPlane=8.85718, width=2.26873, height=1.42427, cameraPosition=(7.88619, 
    1.41391, 3.02492), cameraUpVector=(-0.628686, 0.293839, 0.720009), 
    cameraTarget=(0.261659, 3.12444, -0.383895), viewOffsetX=-0.835016, 
    viewOffsetY=0.246036)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.02116, 
    farPlane=8.65465, width=2.74338, height=1.72225, cameraPosition=(4.61896, 
    -0.31378, 6.53492), cameraUpVector=(-0.542022, 0.825123, 0.159327), 
    cameraTarget=(1.85084, 2.75185, -0.922887), viewOffsetX=-1.00971, 
    viewOffsetY=0.29751)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.74203, 
    farPlane=8.93379, width=4.72376, height=2.96549, viewOffsetX=-1.41144, 
    viewOffsetY=0.661056)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.10376, 
    farPlane=8.92946, width=4.19869, height=2.63586, cameraPosition=(5.99438, 
    -0.313962, 5.23163), cameraUpVector=(-0.502642, 0.806904, 0.310253), 
    cameraTarget=(1.3926, 2.82296, -1.22303), viewOffsetX=-1.25455, 
    viewOffsetY=0.587576)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.65362, 
    farPlane=8.72062, width=3.00571, height=1.88693, cameraPosition=(5.88289, 
    -3.0103, -0.304495), cameraUpVector=(-0.167092, 0.226507, 0.95957), 
    cameraTarget=(1.20386, 4.10074, 0.163567), viewOffsetX=-0.898093, 
    viewOffsetY=0.420627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.55154, 
    farPlane=6.56632, width=3.7444, height=2.35066, cameraPosition=(3.86426, 
    0.157421, -5.01364), cameraUpVector=(-0.234411, -0.816133, 0.528184), 
    cameraTarget=(2.44583, 2.3373, 3.10519), viewOffsetX=-1.11881, 
    viewOffsetY=0.524001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.75645, 
    farPlane=7.9783, width=3.0903, height=1.94003, cameraPosition=(3.80922, 
    -3.90366, -1.32773), cameraUpVector=(-0.1706, 0.123778, 0.977535), 
    cameraTarget=(2.43461, 4.35223, 0.293952), viewOffsetX=-0.923369, 
    viewOffsetY=0.432465)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.15538, 
    farPlane=7.77201, width=3.41848, height=2.14606, cameraPosition=(2.83042, 
    -4.39102, 1.0991), cameraUpVector=(-0.063845, 0.553253, 0.830563), 
    cameraTarget=(2.8629, 3.87578, -0.983707), viewOffsetX=-1.02143, 
    viewOffsetY=0.478392)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.11972, 
    farPlane=7.80768, width=3.38914, height=2.12764, cameraPosition=(2.55075, 
    -4.50444, 0.644581), cameraUpVector=(0.252329, 0.544318, 0.80003), 
    cameraTarget=(2.58323, 3.76236, -1.43823), viewOffsetX=-1.01266, 
    viewOffsetY=0.474286)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.54922, 
    farPlane=8.5281, width=2.91981, height=1.833, cameraPosition=(-1.74392, 
    -3.79601, -0.218701), cameraUpVector=(-0.0302902, 0.439804, 0.897583), 
    cameraTarget=(4.30062, 2.20033, 0.213043), viewOffsetX=-0.872425, 
    viewOffsetY=0.408606)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.41229, 
    farPlane=7.68989, width=3.62982, height=2.27873, cameraPosition=(2.64792, 
    -3.66049, 3.34279), cameraUpVector=(-0.0999334, 0.818645, 0.565538), 
    cameraTarget=(3.05885, 3.27443, -1.59856), viewOffsetX=-1.08457, 
    viewOffsetY=0.507967)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.33513, 
    farPlane=7.76705, width=3.56634, height=2.23888, cameraPosition=(2.7112, 
    -3.23048, 3.95155), cameraUpVector=(-0.502332, 0.74827, 0.433306), 
    cameraTarget=(3.12213, 3.70444, -0.989796), viewOffsetX=-1.0656, 
    viewOffsetY=0.499083)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.65339, 
    farPlane=8.154, width=3.0055, height=1.8868, cameraPosition=(4.44134, 
    -3.78924, 1.0425), cameraUpVector=(-0.843692, 0.0984262, 0.527728), 
    cameraTarget=(2.03285, 4.38866, 1.05144), viewOffsetX=-0.898025, 
    viewOffsetY=0.420598)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.03512, 
    farPlane=7.95767, width=3.31953, height=2.08394, cameraPosition=(4.55616, 
    -2.65726, 3.48631), cameraUpVector=(-0.669349, 0.534497, 0.516028), 
    cameraTarget=(2.23184, 4.15663, -1.07959), viewOffsetX=-0.991856, 
    viewOffsetY=0.464545)
p = mdb.models['Model-1'].parts['Indent']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=10.2194, 
    farPlane=18.7854, width=7.19631, height=4.51771, cameraPosition=(-8.02565, 
    10.701, 8.01727), cameraUpVector=(0.88991, 0.454779, -0.0351776), 
    cameraTarget=(1.69284, 1.90213, 1.53476))
p = mdb.models['Model-1'].parts['Indent']
p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Indent']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=10.7591, 
    farPlane=18.4686, width=7.57637, height=4.75631, cameraPosition=(-9.79702, 
    10.6833, -0.496699), cameraUpVector=(0.766484, 0.31498, -0.559723), 
    cameraTarget=(1.70782, 1.90228, 1.60674))
session.viewports['Viewport: 1'].view.setValues(nearPlane=10.9537, 
    farPlane=18.381, width=7.71339, height=4.84233, cameraPosition=(11.1863, 
    4.77078, -9.13569), cameraUpVector=(0.154133, 0.633286, 0.758414), 
    cameraTarget=(1.69174, 1.90681, 1.61336))
session.viewports['Viewport: 1'].view.setValues(nearPlane=10.3536, 
    farPlane=18.7887, width=7.29078, height=4.57703, cameraPosition=(9.34972, 
    13.3423, -3.36589), cameraUpVector=(-0.0608194, 0.050072, 0.996892), 
    cameraTarget=(1.68644, 1.93155, 1.63001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4566, 
    farPlane=17.9272, width=8.06746, height=5.06462, cameraPosition=(4.25194, 
    4.69455, -12.4766), cameraUpVector=(-0.161799, 0.861132, 0.481947), 
    cameraTarget=(1.70527, 1.9635, 1.66367))
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.7199, 
    farPlane=17.6838, width=8.25286, height=5.18101, cameraPosition=(4.00229, 
    2.58798, -12.7671), cameraUpVector=(-0.230652, 0.911265, 0.341168), 
    cameraTarget=(1.70413, 1.95391, 1.66235))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Indent']
a.Instance(name='Indent-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Indent']
a.Instance(name='Indent-2', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Disque']
a.Instance(name='Disque-1', part=p, dependent=ON)
p1 = a.instances['Disque-1']
p1.translate(vector=(3.8, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.0746, 
    farPlane=24.0443, width=9.9757, height=6.24372, cameraPosition=(-5.31958, 
    8.88469, 17.2391), cameraUpVector=(-0.48988, 0.280101, -0.825567), 
    cameraTarget=(3.63271, 1.77808, 1.74016))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.3382, 
    farPlane=24.4821, width=9.45378, height=5.91705, cameraPosition=(-11.2435, 
    12.5301, 7.43695), cameraUpVector=(0.270207, 0.259848, -0.927075), 
    cameraTarget=(3.69437, 1.74013, 1.84219))
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.0864, 
    farPlane=23.5209, width=9.98406, height=6.24895, cameraPosition=(-1.61442, 
    -9.92886, -11.8934), cameraUpVector=(0.725418, 0.605325, -0.327644), 
    cameraTarget=(3.51732, 2.15308, 2.19762))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.4427, 
    farPlane=23.8579, width=9.52784, height=5.96341, cameraPosition=(-5.16356, 
    12.8409, -10.7801), cameraUpVector=(0.965551, 0.252847, 0.0614743), 
    cameraTarget=(3.60305, 1.60308, 2.17073))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.7663, 
    farPlane=23.5371, width=9.75721, height=6.10697, cameraPosition=(-4.33676, 
    10.192, -13.1141), cameraUpVector=(0.93329, 0.33713, 0.123743), 
    cameraTarget=(3.57611, 1.68937, 2.24677))
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.8743, 
    farPlane=22.4279, width=10.5425, height=6.59848, cameraPosition=(-0.95573, 
    3.86068, -16.29), cameraUpVector=(0.771211, 0.595772, 0.224253), 
    cameraTarget=(3.46623, 1.89513, 2.34998))
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5168, 
    farPlane=21.7701, width=10.9979, height=6.88351, cameraPosition=(2.21592, 
    1.68438, -16.8533), cameraUpVector=(0.644738, 0.709248, 0.285097), 
    cameraTarget=(3.36305, 1.96593, 2.36831))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.023, 
    farPlane=24.3199, width=9.23038, height=5.77723, cameraPosition=(-9.06325, 
    11.9236, 11.4885), cameraUpVector=(0.604816, 0.618384, -0.501795), 
    cameraTarget=(3.73477, 1.62849, 1.43427))
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.3926, 
    farPlane=23.9625, width=9.49235, height=5.9412, cameraPosition=(-8.71933, 
    9.2707, 13.9619), cameraUpVector=(0.458539, 0.736042, -0.49798), 
    cameraTarget=(3.72397, 1.71181, 1.35659))
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.0459, 
    farPlane=23.2764, width=9.95539, height=6.23101, cameraPosition=(-3.21152, 
    8.83837, 17.8056), cameraUpVector=(0.375782, 0.743472, -0.553206), 
    cameraTarget=(3.55283, 1.72524, 1.23716))
a = mdb.models['Model-1'].rootAssembly
del a.features['Indent-2']
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.8189, 
    farPlane=23.4948, width=9.79453, height=6.13032, cameraPosition=(-3.57777, 
    10.3427, -13.4095), cameraUpVector=(0.805686, 0.499134, 0.31896), 
    cameraTarget=(3.56454, 1.67714, 2.23534))
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.154, 
    farPlane=23.1597, width=6.69747, height=4.1919, viewOffsetX=-0.834091, 
    viewOffsetY=-0.036944)
a1 = mdb.models['Model-1'].rootAssembly
a1.rotate(instanceList=('Disque-1', ), axisPoint=(3.8, 0.0, 0.0), 
    axisDirection=(10.0, 0.0, 0.0), angle=90.0)
#: The instance Disque-1 was rotated by 90. degrees about the axis defined by the point 3.8, 0., 0. and the vector 10., 0., 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.8297, 
    farPlane=22.9808, width=6.07081, height=3.79967, cameraPosition=(-8.45435, 
    15.0733, -1.28664), cameraUpVector=(0.448976, -0.196405, -0.871691), 
    cameraTarget=(5.11444, 1.66599, 1.35886), viewOffsetX=-0.756048, 
    viewOffsetY=-0.0334872)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.8335, 
    farPlane=22.3452, width=6.07259, height=3.80079, cameraPosition=(11.8709, 
    16.6628, 6.61155), cameraUpVector=(-0.432514, 0.179501, -0.883579), 
    cameraTarget=(3.75631, 0.484709, 0.0319972), viewOffsetX=-0.75627, 
    viewOffsetY=-0.033497)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.9729, 
    farPlane=21.1949, width=6.61171, height=4.13822, cameraPosition=(3.83301, 
    19.2786, 5.08095), cameraUpVector=(-0.249852, -0.113725, -0.961582), 
    cameraTarget=(4.64149, 0.615153, 0.402469), viewOffsetX=-0.823411, 
    viewOffsetY=-0.0364708)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.9174, 
    farPlane=21.2503, width=6.58545, height=4.12178, cameraPosition=(3.8433, 
    19.2713, 5.11202), cameraUpVector=(-0.220473, -0.110566, -0.969106), 
    cameraTarget=(4.65178, 0.607809, 0.433541), viewOffsetX=-0.82014, 
    viewOffsetY=-0.0363259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.655, 
    farPlane=22.4236, width=5.98809, height=3.7479, cameraPosition=(-6.33365, 
    16.6149, 2.37871), cameraUpVector=(-0.129266, -0.411648, -0.902129), 
    cameraTarget=(5.32778, 1.40048, 0.534525), viewOffsetX=-0.745745, 
    viewOffsetY=-0.0330308)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.0112, 
    farPlane=22.1695, width=6.62981, height=4.14955, cameraPosition=(2.15691, 
    14.6804, -11.1119), cameraUpVector=(0.0527662, -0.893324, -0.446305), 
    cameraTarget=(4.82724, 1.00884, 2.18571), viewOffsetX=-0.825664, 
    viewOffsetY=-0.0365706)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.741, 
    farPlane=21.9865, width=6.97516, height=4.3657, cameraPosition=(2.8684, 
    -5.19996, -15.2047), cameraUpVector=(0.295809, -0.709013, 0.640155), 
    cameraTarget=(4.7552, 2.4135, 2.38346), viewOffsetX=-0.868673, 
    viewOffsetY=-0.0384756)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.2267, 
    farPlane=22.5008, width=11.8331, height=7.40625, viewOffsetX=0.281646, 
    viewOffsetY=-0.315038)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.2256, 
    farPlane=23.7693, width=11.0004, height=6.88507, cameraPosition=(-1.81124, 
    16.045, -9.09359), cameraUpVector=(-0.440837, -0.854381, -0.275128), 
    cameraTarget=(4.69741, 1.63375, 1.89833), viewOffsetX=0.261826, 
    viewOffsetY=-0.292869)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.5507, 
    farPlane=23.4442, width=8.66752, height=5.42494, viewOffsetX=-0.286742, 
    viewOffsetY=0.192905)
a1 = mdb.models['Model-1'].rootAssembly
v11 = a1.instances['Disque-1'].vertices
v12 = a1.instances['Indent-1'].vertices
a1.CoincidentPoint(movablePoint=v11[4], fixedPoint=v12[5])
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.5005, 
    farPlane=22.2166, width=8.63539, height=5.40483, cameraPosition=(-2.1196, 
    15.714, -9.34494), cameraUpVector=(-0.732059, -0.315562, 0.603746), 
    cameraTarget=(4.38905, 1.30277, 1.64698), viewOffsetX=-0.285679, 
    viewOffsetY=0.19219)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.9739, 
    farPlane=23.8864, width=10.2175, height=6.39505, cameraPosition=(18.7834, 
    11.7496, -2.01708), cameraUpVector=(-0.723062, 0.616548, 0.311527), 
    cameraTarget=(2.63961, 1.69681, 1.014), viewOffsetX=-0.338018, 
    viewOffsetY=0.227401)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.1239, 
    farPlane=24.1657, width=10.3135, height=6.45511, cameraPosition=(17.7385, 
    5.40452, -10.0859), cameraUpVector=(-0.621417, 0.783271, 0.0180922), 
    cameraTarget=(2.49627, 1.25291, 0.928032), viewOffsetX=-0.341192, 
    viewOffsetY=0.229537)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.7723, 
    farPlane=24.2768, width=10.0886, height=6.31434, cameraPosition=(11.4898, 
    8.69253, -14.4578), cameraUpVector=(0.0393491, 0.660655, 0.749658), 
    cameraTarget=(1.91063, 1.74124, 0.73382), viewOffsetX=-0.333751, 
    viewOffsetY=0.224531)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.1686, 
    farPlane=24.0725, width=9.70245, height=6.07265, cameraPosition=(-3.70053, 
    17.1229, -9.59201), cameraUpVector=(0.690836, 0.283323, 0.665187), 
    cameraTarget=(1.26062, 2.05347, 1.32426), viewOffsetX=-0.320976, 
    viewOffsetY=0.215937)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.3422, 
    farPlane=23.5929, width=9.81346, height=6.14217, cameraPosition=(-14.0395, 
    13.1547, -0.860619), cameraUpVector=(0.794283, 0.559828, 0.236024), 
    cameraTarget=(1.29367, 1.78756, 1.69847), viewOffsetX=-0.324648, 
    viewOffsetY=0.218408)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.0191, 
    farPlane=22.8247, width=10.2465, height=6.41318, cameraPosition=(-17.2125, 
    4.15364, 5.40958), cameraUpVector=(0.427346, 0.889592, -0.161249), 
    cameraTarget=(1.5557, 1.70907, 1.85361), viewOffsetX=-0.338972, 
    viewOffsetY=0.228045)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.9415, 
    farPlane=22.9022, width=10.7146, height=6.70618, viewOffsetX=0.0389612, 
    viewOffsetY=0.170666)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.7231, 
    farPlane=23.0735, width=10.5678, height=6.61428, cameraPosition=(-16.9627, 
    6.42339, 4.4369), cameraUpVector=(0.554277, 0.831959, -0.024915), 
    cameraTarget=(1.53229, 1.73883, 1.8185), viewOffsetX=0.0384273, 
    viewOffsetY=0.168327)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.8327, 
    farPlane=23.1349, width=10.6414, height=6.66037, cameraPosition=(-13.5174, 
    1.31507, 13.8372), cameraUpVector=(0.272698, 0.948279, -0.162487), 
    cameraTarget=(1.5827, 1.6951, 1.89109), viewOffsetX=0.0386951, 
    viewOffsetY=0.1695)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5587, 
    farPlane=23.2813, width=10.4572, height=6.54509, cameraPosition=(-16.3894, 
    6.51077, 7.0799), cameraUpVector=(0.520778, 0.830377, -0.198154), 
    cameraTarget=(1.52127, 1.75748, 1.8378), viewOffsetX=0.0380254, 
    viewOffsetY=0.166566)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.9225, 
    farPlane=22.9174, width=7.14456, height=4.47172, viewOffsetX=-0.468339, 
    viewOffsetY=-0.39866)
i1 = mdb.models['Model-1'].rootAssembly.allInstances['Disque-1']
leaf = dgm.LeafFromInstance(instances=(i1, ))
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.7935, 
    farPlane=21.7349, width=11.0896, height=6.94092, viewOffsetX=0.549681, 
    viewOffsetY=-0.590487)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.6557, 
    farPlane=23.0855, width=10.2907, height=6.44087, cameraPosition=(-12.8089, 
    13.9555, 3.37841), cameraUpVector=(0.856921, 0.515425, -0.00486357), 
    cameraTarget=(2.01339, 1.75262, 1.87743), viewOffsetX=0.51008, 
    viewOffsetY=-0.547946)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.462, 
    farPlane=23.246, width=10.8568, height=6.7952, cameraPosition=(-15.9831, 
    7.14512, 7.60255), cameraUpVector=(0.572328, 0.815915, -0.081994), 
    cameraTarget=(1.66492, 2.05186, 1.81736), viewOffsetX=0.538141, 
    viewOffsetY=-0.57809)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.9311, 
    farPlane=23.7136, width=11.1862, height=7.00137, cameraPosition=(-14.7488, 
    -0.35507, 12.4713), cameraUpVector=(0.358564, 0.919307, 0.162194), 
    cameraTarget=(1.35472, 2.1564, 2.21308), viewOffsetX=0.554468, 
    viewOffsetY=-0.595629)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.5978, 
    farPlane=23.379, width=10.9521, height=6.85488, cameraPosition=(-16.0238, 
    5.68062, 8.87711), cameraUpVector=(0.515023, 0.855988, -0.0451236), 
    cameraTarget=(1.5523, 2.23176, 1.8026), viewOffsetX=0.542866, 
    viewOffsetY=-0.583166)
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.2803, 
    farPlane=22.7094, width=11.4314, height=7.15482, cameraPosition=(-17.6134, 
    1.24802, 3.9155), cameraUpVector=(0.256662, 0.863449, -0.434258), 
    cameraTarget=(1.47342, 1.74544, 1.4037), viewOffsetX=0.566619, 
    viewOffsetY=-0.608682)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.4305, 
    farPlane=22.945, width=10.8347, height=6.78134, cameraPosition=(-14.889, 
    1.25632, -7.77497), cameraUpVector=(0.0705127, 0.890383, 0.449718), 
    cameraTarget=(1.76727, 2.29266, 1.83529), viewOffsetX=0.537042, 
    viewOffsetY=-0.576909)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.581, 
    farPlane=22.1589, width=10.9404, height=6.84747, cameraPosition=(-1.60308, 
    1.70134, -16.8178), cameraUpVector=(-0.302665, 0.879258, 0.367831), 
    cameraTarget=(1.91495, 2.29609, 2.10658), viewOffsetX=0.542279, 
    viewOffsetY=-0.582535)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5513, 
    farPlane=22.3837, width=10.2174, height=6.39493, cameraPosition=(19.0055, 
    6.91141, -2.74053), cameraUpVector=(-0.549918, 0.825556, 0.126675), 
    cameraTarget=(1.16382, 1.98628, 2.57748), viewOffsetX=0.506441, 
    viewOffsetY=-0.544036)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.7884, 
    farPlane=22.649, width=9.68174, height=6.05967, cameraPosition=(15.0264, 
    13.7187, -2.77342), cameraUpVector=(-0.652442, 0.469247, 0.595085), 
    cameraTarget=(1.38426, 1.33208, 2.82384), viewOffsetX=0.47989, 
    viewOffsetY=-0.515514)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.9377, 
    farPlane=21.7259, width=9.78657, height=6.12528, cameraPosition=(1.42882, 
    19.6686, -1.19942), cameraUpVector=(-0.303521, -0.163579, 0.938678), 
    cameraTarget=(2.49176, 0.839996, 2.70162), viewOffsetX=0.485086, 
    viewOffsetY=-0.521096)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.6379, 
    farPlane=21.4404, width=10.2783, height=6.43302, cameraPosition=(5.70315, 
    5.11696, -15.6116), cameraUpVector=(-0.475982, 0.805951, 0.351971), 
    cameraTarget=(2.04084, 2.72823, 3.14333), viewOffsetX=0.509457, 
    viewOffsetY=-0.547276)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4984, 
    farPlane=21.7692, width=10.1803, height=6.37171, cameraPosition=(11.2873, 
    1.81212, -13.705), cameraUpVector=(-0.383471, 0.917465, 0.105869), 
    cameraTarget=(1.78419, 2.90811, 3.00896), viewOffsetX=0.504601, 
    viewOffsetY=-0.54206)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4878, 
    farPlane=22.1831, width=10.1729, height=6.36706, cameraPosition=(18.9827, 
    -4.07261, 0.0964723), cameraUpVector=(0.0378445, 0.999156, -0.0159844), 
    cameraTarget=(1.27234, 3.06294, 2.60499), viewOffsetX=0.504233, 
    viewOffsetY=-0.541665)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.0156, 
    farPlane=22.4999, width=9.84137, height=6.15956, cameraPosition=(14.0777, 
    8.45285, -10.1511), cameraUpVector=(-0.13032, 0.707254, 0.694844), 
    cameraTarget=(1.73405, 2.12852, 3.20943), viewOffsetX=0.4878, 
    viewOffsetY=-0.524012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4178, 
    farPlane=22.1323, width=10.1238, height=6.33631, cameraPosition=(17.0073, 
    5.30132, -7.83209), cameraUpVector=(-0.151375, 0.794928, 0.587517), 
    cameraTarget=(1.47597, 2.30105, 3.15168), viewOffsetX=0.501798, 
    viewOffsetY=-0.539049)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.2888, 
    farPlane=22.2961, width=10.0332, height=6.27961, cameraPosition=(-0.565938, 
    20.1629, 0.130033), cameraUpVector=(0.303999, -0.172045, 0.937009), 
    cameraTarget=(2.76857, 1.33736, 2.44237), viewOffsetX=0.497308, 
    viewOffsetY=-0.534226)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5143, 
    farPlane=21.8249, width=10.1915, height=6.37871, cameraPosition=(-5.88606, 
    4.45755, -14.5906), cameraUpVector=(0.162915, 0.907913, 0.386202), 
    cameraTarget=(2.83156, 2.6976, 2.49077), viewOffsetX=0.505156, 
    viewOffsetY=-0.542656)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.2303, 
    farPlane=22.1248, width=9.99211, height=6.25392, cameraPosition=(15.6655, 
    -0.572418, -9.68511), cameraUpVector=(0.135236, 0.892915, 0.429434), 
    cameraTarget=(1.5931, 2.61374, 3.06967), viewOffsetX=0.495273, 
    viewOffsetY=-0.53204)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4507, 
    farPlane=21.9026, width=10.1469, height=6.35078, cameraPosition=(-14.9705, 
    6.65566, -3.78319), cameraUpVector=(0.504335, 0.849738, 0.153593), 
    cameraTarget=(3.08977, 2.53879, 1.48427), viewOffsetX=0.502944, 
    viewOffsetY=-0.54028)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.9642, 
    farPlane=22.4344, width=9.80529, height=6.13697, cameraPosition=(-10.5561, 
    15.2855, -0.652282), cameraUpVector=(0.852283, 0.437469, 0.286766), 
    cameraTarget=(3.13749, 1.9077, 1.44279), viewOffsetX=0.486012, 
    viewOffsetY=-0.522091)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5137, 
    farPlane=21.8245, width=10.1911, height=6.37845, cameraPosition=(-15.4939, 
    -1.39, -2.91431), cameraUpVector=(0.128948, 0.990276, -0.0522123), 
    cameraTarget=(2.79781, 2.93166, 1.28166), viewOffsetX=0.505136, 
    viewOffsetY=-0.542634)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.6771, 
    farPlane=21.6585, width=10.3058, height=6.45025, cameraPosition=(1.90122, 
    -2.12951, -15.9526), cameraUpVector=(-0.0108923, 0.997581, 0.0686504), 
    cameraTarget=(2.392, 3.03436, 2.59362), viewOffsetX=0.510822, 
    viewOffsetY=-0.548742)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4182, 
    farPlane=21.9248, width=10.124, height=6.33649, cameraPosition=(12.9902, 
    4.17854, -12.401), cameraUpVector=(-0.186277, 0.910231, 0.369838), 
    cameraTarget=(1.62047, 2.62041, 3.06415), viewOffsetX=0.501813, 
    viewOffsetY=-0.539064)
session.viewports['Viewport: 1'].view.setValues(nearPlane=15.0942, 
    farPlane=21.2575, width=10.5987, height=6.6336, cameraPosition=(2.16948, 
    4.40214, -16.2938), cameraUpVector=(0.00582698, 0.908714, 0.417379), 
    cameraTarget=(2.39022, 2.65652, 2.8836), viewOffsetX=0.525342, 
    viewOffsetY=-0.56434)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.3427, 
    farPlane=22.0019, width=10.071, height=6.30331, cameraPosition=(13.8721, 
    4.38535, -11.6201), cameraUpVector=(-0.215979, 0.905418, 0.365473), 
    cameraTarget=(1.53454, 2.60675, 3.05949), viewOffsetX=0.499185, 
    viewOffsetY=-0.536242)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.9197, 
    farPlane=21.4293, width=10.4762, height=6.55691, cameraPosition=(4.45867, 
    4.47525, -16.0832), cameraUpVector=(-0.0510924, 0.907064, 0.41788), 
    cameraTarget=(2.24018, 2.6543, 2.95965), viewOffsetX=0.519268, 
    viewOffsetY=-0.557816)
session.viewports['Viewport: 1'].view.setValues(nearPlane=13.7114, 
    farPlane=22.6664, width=9.62778, height=6.0259, cameraPosition=(-2.35814, 
    16.1839, -8.98991), cameraUpVector=(-0.147482, 0.292506, 0.944823), 
    cameraTarget=(2.44248, 1.88288, 2.98101), viewOffsetX=0.477215, 
    viewOffsetY=-0.512641)
session.viewports['Viewport: 1'].view.setValues(nearPlane=14.3142, 
    farPlane=22.0769, width=10.051, height=6.2908, cameraPosition=(-0.0194902, 
    20.1264, 0.195493), cameraUpVector=(-0.430922, -0.267779, 0.861742), 
    cameraTarget=(2.07391, 1.16032, 2.79791), viewOffsetX=0.498194, 
    viewOffsetY=-0.535177)
mdb.saveAs(
    pathName='/net/etudiant/home/maenhaua/Documents/Calculs/Projet/thin-film-indentation-simulation/Tuto explicite/test tuto explicite ')
#: The model database has been saved to "/net/etudiant/home/maenhaua/Documents/Calculs/Projet/thin-film-indentation-simulation/Tuto explicite/test tuto explicite .cae".

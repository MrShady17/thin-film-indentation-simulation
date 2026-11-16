# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by maenhaua on Thu Nov 12 08:42:30 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=719.666625976562, 
    height=197.652786254883)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(width=1.05044, height=1.10914, 
    viewOffsetX=0.000149727, viewOffsetY=-0.000142038)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)   
session.viewports['Viewport: 1'].view.setValues(nearPlane=147.715, 
    farPlane=229.409, width=186.151, height=223.974, cameraPosition=(26.9176, 
    0.160023, 188.562), cameraTarget=(26.9176, 0.160023, 0))
s.rectangle(point1=(0.0, 0.0), point2=(100.0, 50.0))
s.CircleByCenterPerimeter(center=(50.0, 25.0), point1=(5.0, 0.0))
s.RadialDimension(curve=g[6], textPoint=(-3.2212085723877, 69.5252227783203), 
    radius=5.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=154.697, 
    farPlane=222.427, width=151.184, height=181.902, cameraPosition=(36.1011, 
    7.17744, 188.562), cameraTarget=(36.1011, 7.17744, 0))
p = mdb.models['Model-1'].Part(name='Plate', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Plate']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Elastic(table=((210000.0, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='PlateSection', 
    material='Steel', thickness=None)
p = mdb.models['Model-1'].parts['Plate']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['Plate']
p.SectionAssignment(region=region, sectionName='PlateSection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Plate']
a.Instance(name='Plate-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Plate']
a.Instance(name='Plate-2', part=p, dependent=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Tension', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Tension')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=199.325, 
    farPlane=247.888, width=107.906, height=129.489, viewOffsetX=3.33855, 
    viewOffsetY=-3.03532)
session.viewports['Viewport: 1'].view.setValues(nearPlane=198.99, 
    farPlane=248.224, width=107.725, height=129.271, cameraPosition=(51.5386, 
    25.682, 223.607), cameraTarget=(51.5386, 25.682, 0), viewOffsetX=3.33294, 
    viewOffsetY=-3.03021)
session.viewports['Viewport: 1'].view.setValues(nearPlane=170.268, 
    farPlane=283.839, width=92.1763, height=110.613, cameraPosition=(129.185, 
    -108.339, 165.843), cameraUpVector=(-0.260057, 0.687577, 0.677944), 
    cameraTarget=(51.0272, 23.0198, 2.63639), viewOffsetX=2.85187, 
    viewOffsetY=-2.59284)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.fitView()
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Plate-2'].edges
edges1 = e1.getSequenceFromMask(mask=('[#10 ]', ), )
region = a.Set(edges=edges1, name='Set-1')
mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Tension', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Plate-2'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = a.Set(edges=edges1, name='Set-2')
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Tension', 
    region=region, u1=0.1, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213.1, 
    farPlane=246.814, width=117.289, height=56.3455, viewOffsetX=1.38151, 
    viewOffsetY=0.619213)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
del mdb.models['Model-1'].boundaryConditions['BC-1']
mdb.models['Model-1'].boundaryConditions.changeKey(fromName='BC-2', 
    toName='Displacement')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Plate-2'].edges
edges1 = e1.getSequenceFromMask(mask=('[#10 ]', ), )
region = a.Set(edges=edges1, name='Set-3')
mdb.models['Model-1'].DisplacementBC(name='Clamp', createStepName='Tension', 
    region=region, u1=0.0, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=210.926, 
    farPlane=248.988, width=142.261, height=68.342, viewOffsetX=4.24724, 
    viewOffsetY=0.45452)
session.viewports['Viewport: 1'].view.setValues(nearPlane=210.716, 
    farPlane=249.198, width=142.12, height=68.2742, cameraPosition=(28.9709, 
    19.0873, 229.025), cameraUpVector=(0.262164, 0.963329, 0.0571561), 
    cameraTarget=(56.9744, 25.0039, 0.856095), viewOffsetX=4.24302, 
    viewOffsetY=0.454069)
session.viewports['Viewport: 1'].view.setValues(nearPlane=214.242, 
    farPlane=271.453, width=144.498, height=69.4167, cameraPosition=(45.0413, 
    -93.3605, 212.422), cameraUpVector=(0.448292, 0.759253, 0.471772), 
    cameraTarget=(62.2698, 20.2393, 13.2274), viewOffsetX=4.31402, 
    viewOffsetY=0.461667)
session.viewports['Viewport: 1'].view.setValues(nearPlane=201.33, 
    farPlane=258.358, width=135.789, height=65.2331, cameraPosition=(-6.81194, 
    16.5226, 222.95), cameraUpVector=(0.444639, 0.880062, 0.166695), 
    cameraTarget=(62.62, 22.9491, 3.81996), viewOffsetX=4.05402, 
    viewOffsetY=0.433843)
session.viewports['Viewport: 1'].view.setValues(nearPlane=188.49, 
    farPlane=287.165, width=127.129, height=61.0728, cameraPosition=(-76.5693, 
    -54.8211, 185.447), cameraUpVector=(0.236221, 0.804969, 0.544266), 
    cameraTarget=(57.2802, 21.3602, 14.6816), viewOffsetX=3.79547, 
    viewOffsetY=0.406174)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213.068, 
    farPlane=285.408, width=143.706, height=69.0362, cameraPosition=(16.7361, 
    -150.912, 173.706), cameraUpVector=(-0.0790967, 0.678109, 0.730693), 
    cameraTarget=(47.2722, 17.7901, 20.4504), viewOffsetX=4.29037, 
    viewOffsetY=0.459136)
session.viewports['Viewport: 1'].view.setValues(nearPlane=218.343, 
    farPlane=279.854, width=147.264, height=70.7454, cameraPosition=(47.3113, 
    -148.619, 178.895), cameraUpVector=(-0.0695392, 0.687914, 0.722453), 
    cameraTarget=(47.3043, 17.9173, 20.3204), viewOffsetX=4.39659, 
    viewOffsetY=0.470503)
session.viewports['Viewport: 1'].view.setValues(nearPlane=213.044, 
    farPlane=279.061, width=143.69, height=69.0284, cameraPosition=(71.8125, 
    -119.13, 198.36), cameraUpVector=(0.014418, 0.792495, 0.609709), 
    cameraTarget=(49.5242, 20.6862, 17.1556), viewOffsetX=4.28988, 
    viewOffsetY=0.459084)
session.viewports['Viewport: 1'].view.setValues(nearPlane=214.286, 
    farPlane=269.241, width=144.528, height=69.4308, cameraPosition=(68.6793, 
    -80.1431, 216.943), cameraUpVector=(0.108109, 0.890626, 0.441698), 
    cameraTarget=(52.229, 23.3654, 12.2581), viewOffsetX=4.31489, 
    viewOffsetY=0.46176)
session.viewports['Viewport: 1'].view.setValues(nearPlane=212.831, 
    farPlane=268.062, width=143.547, height=68.9595, cameraPosition=(31.6628, 
    -69.779, 220.288), cameraUpVector=(0.140772, 0.898271, 0.416285), 
    cameraTarget=(53.4455, 23.6581, 11.3009), viewOffsetX=4.2856, 
    viewOffsetY=0.458625)
session.viewports['Viewport: 1'].view.setValues(nearPlane=205.613, 
    farPlane=273.304, width=138.679, height=66.6209, cameraPosition=(-1.03874, 
    -62.4409, 217.102), cameraUpVector=(0.129556, 0.902112, 0.411594), 
    cameraTarget=(53.401, 23.7814, 10.9888), viewOffsetX=4.14026, 
    viewOffsetY=0.443072)
session.viewports['Viewport: 1'].view.setValues(nearPlane=206.042, 
    farPlane=293.431, width=138.968, height=66.7599, cameraPosition=(-15.045, 
    -157.032, 158.491), cameraUpVector=(-0.24959, 0.652573, 0.715439), 
    cameraTarget=(42.7156, 17.0838, 19.8261), viewOffsetX=4.1489, 
    viewOffsetY=0.443997)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.729, 
    farPlane=282.845, width=132.686, height=63.7423, cameraPosition=(-46.2495, 
    -67.0308, 199.502), cameraUpVector=(0.00113161, 0.900357, 0.43515), 
    cameraTarget=(50.149, 23.7208, 11.4802), viewOffsetX=3.96136, 
    viewOffsetY=0.423928)
session.viewports['Viewport: 1'].view.setValues(nearPlane=214.101, 
    farPlane=243.186, width=144.403, height=69.371, cameraPosition=(38.9948, 
    31.0679, 228.299), cameraUpVector=(0.00213815, 0.999713, -0.0238682), 
    cameraTarget=(49.4113, 25.5628, -1.35679), viewOffsetX=4.31116, 
    viewOffsetY=0.461362)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Plate']
p.seedPart(size=200.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Plate']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD)
p = mdb.models['Model-1'].parts['Plate']
p.generateMesh()
p = mdb.models['Model-1'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=TRI)
p = mdb.models['Model-1'].parts['Plate']
p.generateMesh()
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
p = mdb.models['Model-1'].parts['Plate']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p = mdb.models['Model-1'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Plate']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD)
p = mdb.models['Model-1'].parts['Plate']
p.generateMesh()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='PlateJob', model='Model-1', description='PlateModel', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.saveAs(
    pathName='/net/etudiant/home/maenhaua/Documents/Calculs/Projet/PlateModel')
#: The model database has been saved to "/net/etudiant/home/maenhaua/Documents/Calculs/Projet/PlateModel.cae".
cliCommand("""9+1""")
#: 10
cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)""")
import os
os.chdir(r"/net/etudiant/home/maenhaua/Documents/Calculs/Projet")
mdb.save()
#: The model database has been saved to "/net/etudiant/home/maenhaua/Documents/Calculs/Projet/PlateModel.cae".

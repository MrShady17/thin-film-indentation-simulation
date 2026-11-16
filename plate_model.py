from abaqus import*
from abaqusConstants import*
import regionToolset
import mesh 

#1. Model creation
Mdb()
model=mdb.Model(name='PlateModel')
s = mdb.models['PlateModel'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)

#2. Geometry 
s.rectangle(point1=(0.0, 0.0), point2=(100.0, 50.0))
s.CircleByCenterPerimeter(center=(50.0, 25.0), point1=(5.0, 0.0))
s.RadialDimension(curve=g[6], textPoint=(-3.2212085723877, 69.5252227783203), 
    radius=5.0)
p = mdb.models['PlateModel'].Part(name='Plate', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p = mdb.models['PlateModel'].parts['Plate']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()


#3. Material and section
mdb.models['PlateModel'].Material(name='Steel')
mdb.models['PlateModel'].materials['Steel'].Elastic(table=((210000.0, 0.3), ))
mdb.models['PlateModel'].HomogeneousSolidSection(name='PlateSection',material='Steel', thickness=None)
p = mdb.models['PlateModel'].parts['Plate']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['PlateModel'].parts['Plate']
p.SectionAssignment(region=region, sectionName='PlateSection', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)

#4. Assembly
a = mdb.models['PlateModel'].rootAssembly
a = mdb.models['PlateModel'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['PlateModel'].parts['Plate']
a.Instance(name='Plate-1', part=p, dependent=ON)
a = mdb.models['PlateModel'].rootAssembly
p = mdb.models['PlateModel'].parts['Plate']
a.Instance(name='Plate-2', part=p, dependent=ON)

#5. Analyse step 
mdb.models['PlateModel'].StaticStep(name='Tension', previous='Initial')

#6. BC
a = mdb.models['PlateModel'].rootAssembly
e1 = a.instances['Plate-2'].edges
edges1 = e1.getSequenceFromMask(mask=('[#4 ]', ), )
region = a.Set(edges=edges1, name='Set-2')
mdb.models['PlateModel'].DisplacementBC(name='BC-2', createStepName='Tension', 
    region=region, u1=0.1, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['PlateModel'].rootAssembly
e1 = a.instances['Plate-2'].edges
edges1 = e1.getSequenceFromMask(mask=('[#10 ]', ), )
region = a.Set(edges=edges1, name='Set-3')
mdb.models['PlateModel'].DisplacementBC(name='Clamp', createStepName='Tension', 
    region=region, u1=0.0, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)

#7. Mesh 

p = mdb.models['PlateModel'].parts['Plate']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT)
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD)
p = mdb.models['PlateModel'].parts['Plate']
p.generateMesh()
a1 = mdb.models['PlateModel'].rootAssembly
a1.regenerate()
a = mdb.models['PlateModel'].rootAssembly

#8. Job creation
mdb.Job(name='PlateJob', model='PlateModel', description='PlateModel', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)

mdb.saveAs(
    pathName='/net/etudiant/home/maenhaua/Documents/Calculs/Projet/PlateModel')
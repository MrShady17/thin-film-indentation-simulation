from abaqus import *
from abaqusConstants import *
from caeModules import *

# PARAMETRES
L = 100.0
h = 50.0
R = 10.0
E, NU = 210000.0, 0.3      
DEPLACEMENT = 0.1           
TAILLE_MAILLE = 2.0

# 1. CREATION DU MODELE
Mdb()
mdb.models.changeKey(fromName='Model-1', toName=MODEL_NAME)
model = mdb.models[MODEL_NAME]

# 2. GEOMETRIE
s = model.ConstrainedSketch(name='PlateSketch', sheetSize=200.0)
s.rectangle(point1=(0.0, 0.0), point2=(L, h))
s.CircleByCenterPerimeter(center=(L / 2, h / 2),point1=(L / 2 + R, h / 2))
 
p = model.Part(name='Plate', dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
p.BaseShell(sketch=s)

# 3. SECTION ET MATERIAU

model.Material(name='Steel')
model.materials['Steel'].Elastic(table=((E, NU),))
 
model.HomogeneousSolidSection(name='PlateSection', material='Steel',thickness=None)
 
region = p.Set(faces=p.faces[:], name='Set-1')
p.SectionAssignment(region=region, sectionName='PlateSection', offset=0.0,offsetType=MIDDLE_SURFACE, offsetField='',thicknessAssignment=FROM_SECTION)

# 4. ASSEMBLAGE
a = model.rootAssembly
a.DatumCsysByDefault(CARTESIAN)
inst = a.Instance(name='Plate-1', part=p, dependent=ON)

# 5. ETAPE D'ANALYSE
model.StaticStep(name='Tension', previous='Initial')

# 6. CONDITIONS AUX LIMITES
edge_gauche = inst.edges.findAt(((0.0, h / 2, 0.0),))
edge_droite = inst.edges.findAt(((L, h / 2, 0.0),))
 
set_gauche = a.Set(edges=edge_gauche, name='Set-1')
set_droite = a.Set(edges=edge_droite, name='Set-2')
 
model.DisplacementBC(name='Left edge', createStepName='Tension',region=set_gauche, u1=0.0, u2=0.0, ur3=UNSET,amplitude=UNSET, fixed=OFF,
    distributionType=UNIFORM,fieldName='', localCsys=None)
model.DisplacementBC(name='Right edge', createStepName='Tension',region=set_droite, u1=DEPLACEMENT, u2=UNSET, ur3=UNSET,amplitude=UNSET, fixed=OFF,
    distributionType=UNIFORM,fieldName='', localCsys=None)

# 7. MESH

p.seedPart(size=TAILLE_MAILLE, deviationFactor=0.1, minSizeFactor=0.1)
 
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD,secondOrderAccuracy=OFF, hourglassControl=DEFAULT,distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
p.setElementType(regions=(p.faces[:],), elemTypes=(elemType1, elemType2))
 
p.generateMesh()
a.regenerate()

# 8. JOB CREATION
job = mdb.Job(name='PlateJob', model=MODEL_NAME, description='', type=ANALYSIS,memory=90, memoryUnits=PERCENTAGE,
    getMemoryFromAnalysis=True,explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,echoPrint=OFF, modelPrint=OFF, contactPrint=OFF,
    historyPrint=OFF, userSubroutine='', scratch='',resultsFormat=ODB, multiprocessingMode=DEFAULT,numCpus=1, numGPUs=0)
 
mdb.saveAs(pathName='PlateModel.cae')
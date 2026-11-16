from abaqus import*
from abaqusConstants import*
import regionToolset
import mesh 


#0. Parameters
L=100.0
H=50.0
E=210000.0
nu=0.3
u0=0.1
mesh_size=2.0
hole_radius=[3.0,5.0,7.0,10.0]
Mdb()

#1. Model creation
for R in hole_radius:
    model_name = 'PlateModel_R' + str(int(R))
    model=mdb.Model(name=model_name)
    s = model.ConstrainedSketch(name='__profile__', sheetSize=200.0)



    #2. Geometry 
    s.rectangle(point1=(0.0, 0.0), point2=(L, H))
    s.CircleByCenterPerimeter(center=(L/2, H/2), point1=(L/2+R, H/2))
    p = model.Part(name='Plate', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p.BaseShell(sketch=s)



    #3. Material and section
    model.Material(name='Steel')
    model.materials['Steel'].Elastic(table=((E, nu), ))
    model.HomogeneousSolidSection(name='PlateSection',material='Steel', thickness=None)
    region = p.Set(faces=p.faces, name='Set-1')
    p.SectionAssignment(region=region, sectionName='PlateSection', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)

    #4. Assembly
    a = model.rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    instance=a.Instance(name=model_name, part=p, dependent=ON)

    #5. Analyse step 
    model.StaticStep(name='Tension', previous='Initial')

    #6. BC
    right=instance.edges.findAt(((L,H/2),))
    left=instance.edges.findAt(((0.0,H/2),))
    a.Set(edges=right, name='RightEdge')
    a.Set(edges=left, name='LeftEdge')
    model.DisplacementBC(name='Traction', createStepName='Tension', 
        region=a.sets['RightEdge'], u1=u0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    model.DisplacementBC(name='Clamp', createStepName='Tension', 
        region=a.sets['LeftEdge'], u1=0.0, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)

    #7. Mesh    
    p.seedPart(size=mesh_size, deviationFactor=0.1, minSizeFactor=0.1)
    p.setMeshControls(regions=p.faces, elemShape=QUAD)
    elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
        distortionControl=DEFAULT)
    p.setElementType(regions=(p.faces,), elemTypes=(elemType1,))
    p.generateMesh()
    a.regenerate()


    #8. Job creation
    mdb.Job(name='PlateJob_R' + str(int(R)), model=model_name, description='Plate with hole radius ' + str(R), 
        type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)

mdb.saveAs(pathName='/net/etudiant/home/maenhaua/Documents/Calculs/Projet/PlateModel')
print('Model creation completed successfully.')
# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by dosreise on Thu Nov 26 08:31:01 2026
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
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.ModelFromInputFile(name='test_mesh', 
    inputFileName='/net/etudiant/home/dosreise/Documents/Projet_modelisation/thin-film-indentation-simulation/Thin film/test_mesh.inp')
#: The model "test_mesh" has been created.
#: The part "PART-1" has been imported from the input file.
#: The interaction property "INTPROP-1" has been created.
#: The interaction property "INTPROP-2" has been created.
#: The interaction "general_contact" has been created.
#: AbaqusException: Invalid variables are specified in an output request.  An output request cannot be created in a step where some variables are invalid. This occurred while creating an output request for variables CSDMG, CSTRESS, CPRESS, CDISP in step Loading.  
#: The model "test_mesh" has been imported from an input file. 
#: Please scroll up to check for error and warning messages.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['test_mesh'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.JobFromInputFile(name='test_mesh', 
    inputFileName='/net/etudiant/home/dosreise/Documents/Projet_modelisation/thin-film-indentation-simulation/Thin film/test_mesh.inp', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.973016, 
    farPlane=1.71263, width=0.971246, height=0.466585, cameraPosition=(1.2483, 
    0.346364, -0.376535), cameraUpVector=(-0.676131, -0.0174825, -0.736574))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.995365, 
    farPlane=1.69782, width=0.993554, height=0.477302, cameraPosition=(1.19027, 
    -0.104094, -0.562292), cameraUpVector=(-0.776708, -0.0844187, -0.624178), 
    cameraTarget=(0.0498179, 0.0257329, 0.124866))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.05467, 
    farPlane=1.64382, width=1.05275, height=0.505742, cameraPosition=(1.38779, 
    0.0173523, 0.183356), cameraUpVector=(-0.299057, -0.285938, -0.910387), 
    cameraTarget=(0.0511096, 0.0265271, 0.129742))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.035, 
    farPlane=1.6481, width=1.03312, height=0.496311, cameraPosition=(-0.267863, 
    0.200861, -1.17284), cameraUpVector=(-0.832262, -0.207135, 0.514233), 
    cameraTarget=(0.0370491, 0.0280855, 0.118225))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.01997, 
    farPlane=1.67956, width=1.01812, height=0.489103, cameraPosition=(
    0.0229836, -0.75599, -0.966959), cameraUpVector=(-0.929314, 0.0911112, 
    0.357873), cameraTarget=(0.0378651, 0.025401, 0.118803))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.00993, 
    farPlane=1.69499, width=1.0081, height=0.484289, cameraPosition=(0.749925, 
    0.188801, 1.26455), cameraUpVector=(-0.903123, 0.414277, 0.112886), 
    cameraTarget=(0.0443164, 0.0337856, 0.138607))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.01932, 
    farPlane=1.69452, width=1.01748, height=0.488794, cameraPosition=(
    -0.862559, 0.0706673, 1.13582), cameraUpVector=(-0.352984, 0.515763, 
    -0.780635), cameraTarget=(0.0268165, 0.0325035, 0.13721))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.0219, 
    farPlane=1.6937, width=1.02005, height=0.49003, cameraPosition=(-1.2524, 
    -0.0467476, 0.530278), cameraUpVector=(0.0551661, 0.558859, -0.827425), 
    cameraTarget=(0.0213189, 0.0308477, 0.128671))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04137, 
    farPlane=1.67446, width=1.03949, height=0.499368, cameraPosition=(-1.30738, 
    -0.0575617, 0.261055), cameraUpVector=(0.216635, 0.579755, -0.785464), 
    cameraTarget=(0.0205085, 0.0306883, 0.124703))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.994284, 
    farPlane=1.72828, width=0.992489, height=0.476789, cameraPosition=(
    -1.15437, -0.611706, 0.0793558), cameraUpVector=(0.320875, 0.170226, 
    -0.931698), cameraTarget=(0.0227769, 0.0224734, 0.122009))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.969485, 
    farPlane=1.76441, width=0.967735, height=0.464897, cameraPosition=(
    0.686149, -0.790607, -0.749418), cameraUpVector=(-0.596169, 0.622366, 
    -0.507191), cameraTarget=(0.0545416, 0.0193859, 0.107706))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.971664, 
    farPlane=1.76223, width=0.96991, height=0.465942, cameraPosition=(0.686149, 
    -0.790607, -0.749418), cameraUpVector=(-0.013251, 0.9297, -0.368078), 
    cameraTarget=(0.0545416, 0.0193859, 0.107706))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.03684, 
    farPlane=1.70173, width=1.03496, height=0.497194, cameraPosition=(
    -0.180423, -1.30032, -0.049927), cameraUpVector=(0.294935, 0.405966, 
    -0.864988), cameraTarget=(0.0360566, 0.00851316, 0.122627))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.05743, 
    farPlane=1.6823, width=1.05551, height=0.507066, cameraPosition=(-0.10473, 
    -1.32212, 0.13758), cameraUpVector=(0.061246, 0.321131, -0.945052), 
    cameraTarget=(0.0377976, 0.0080117, 0.12694))
mdb.jobs['test_mesh'].submit(consistencyChecking=OFF)
#: The job input file "test_mesh.inp" has been submitted for analysis.
#: Error in job test_mesh: OUTPUT REQUEST CPRESS IS NOT AVAILABLE FOR THIS OPTION
#: Job test_mesh: Analysis Input File Processor aborted due to errors.
del mdb.jobs['test_mesh']
mdb.JobFromInputFile(name='test_mesh', 
    inputFileName='/net/etudiant/home/dosreise/Documents/Projet_modelisation/thin-film-indentation-simulation/Thin film/test_mesh.inp', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
mdb.jobs['test_mesh'].submit(consistencyChecking=OFF)
#: Abaqus Error: Detected lock file test_mesh.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Abaqus/Analysis exited with error(s).
#* Unable to start analysis job
#* Abaqus Error: Detected lock file test_mesh.lck. Please confirm that no other 
#* applications are attempting to write to the output database associated with 
#* this job before removing the lock file and resubmitting.
#* Abaqus/Analysis exited with error(s).
#* 
#* 
mdb.jobs['test_mesh'].submit(consistencyChecking=OFF)
#: Abaqus Error: Detected lock file test_mesh.lck. Please confirm that no other applications are attempting to write to the output database associated with this job before removing the lock file and resubmitting.
#: Abaqus/Analysis exited with error(s).
#* Unable to start analysis job
#* Abaqus Error: Detected lock file test_mesh.lck. Please confirm that no other 
#* applications are attempting to write to the output database associated with 
#* this job before removing the lock file and resubmitting.
#* Abaqus/Analysis exited with error(s).
#* 
#* 
mdb.Job(name='Job-2', model='test_mesh', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=1, 
    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=1)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Explicit Packager completed successfully.
#: Error in job Job-2: Abaqus/Explicit Analysis exited with an error - Please see the  status file for possible error messages if the file exists.
#: Job Job-2 aborted due to errors.
del mdb.jobs['Job-2']
del mdb.jobs['test_mesh']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.983274, 
    farPlane=1.76252, width=0.98149, height=0.471506, cameraPosition=(0.505211, 
    -0.82238, 1.08465), cameraUpVector=(-0.182149, -0.50546, -0.843405), 
    cameraTarget=(0.0520774, 0.0197115, 0.149113))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04761, 
    farPlane=1.70043, width=1.04571, height=0.502357, cameraPosition=(-0.69051, 
    -0.0183233, 1.2853), cameraUpVector=(0.53967, -0.836171, -0.0978534), 
    cameraTarget=(0.0214997, 0.0402733, 0.154244))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.993558, 
    farPlane=1.75111, width=0.991756, height=0.476438, cameraPosition=(
    -1.12424, -0.67729, 0.00750153), cameraUpVector=(0.698479, -0.565473, 
    0.438597), cameraTarget=(0.0100628, 0.0228972, 0.12055))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.99831, 
    farPlane=1.74636, width=0.996499, height=0.478716, cameraPosition=(
    -1.12424, -0.67729, 0.00750145), cameraUpVector=(0.375637, 0.175274, 
    -0.910042), cameraTarget=(0.0100628, 0.0228972, 0.12055))

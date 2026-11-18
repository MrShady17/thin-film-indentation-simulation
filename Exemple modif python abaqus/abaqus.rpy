# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by maenhaua on Wed Nov 18 14:51:30 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=195.637496948242, 
    height=155.228881835938)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile(
    '/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini /thin-film-indentation-simulation/Exemple modif python abaqus/plate_model.py', 
    __main__.__dict__)
#* SyntaxError: ("Non-ASCII character '\\xc2' in file 
#* /net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini 
#* /thin-film-indentation-simulation/Exemple modif python abaqus/plate_model.py 
#* on line 62, but no encoding declared; see 
#* http://python.org/dev/peps/pep-0263/ for details", 
#* ('/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini 
#* /thin-film-indentation-simulation/Exemple modif python 
#* abaqus/plate_model.py', 62, 0, None))
execfile(
    '/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini /thin-film-indentation-simulation/Exemple modif python abaqus/plate_model.py', 
    __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Creating model: PlateModel_R3_E210000_M4
#: The model "PlateModel_R3_E210000_M4" has been created.
#* TypeError: arg1[0]; not all required arguments specified; expected 3, got 2
#* File "/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini 
#* /thin-film-indentation-simulation/Exemple modif python 
#* abaqus/plate_model.py", line 49, in <module>
#*     right=instance.edges.findAt(((L,H/2),))
execfile(
    '/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini /thin-film-indentation-simulation/Exemple modif python abaqus/plate_model.py', 
    __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Creating model: PlateModel_R3_E210000_M4
#: The model "PlateModel_R3_E210000_M4" has been created.
#* TypeError: arg1[0]; not all required arguments specified; expected 3, got 2
#* File "/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini 
#* /thin-film-indentation-simulation/Exemple modif python 
#* abaqus/plate_model.py", line 49, in <module>
#*     right=instance.edges.findAt(((L,H/2),))
execfile(
    '/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini /thin-film-indentation-simulation/Exemple modif python abaqus/plate_model.py', 
    __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Creating model: PlateModel_R3_E210000_M4
#: The model "PlateModel_R3_E210000_M4" has been created.
#* AttributeError: 'GeomSequence' object has no attribute 'getEdges'
#* File "/net/etudiant/home/maenhaua/Documents/Calculs/Projet/Exemple/Code fini 
#* /thin-film-indentation-simulation/Exemple modif python 
#* abaqus/plate_model.py", line 62, in <module>
#*     p.seedEdgeBySize(edges=hole_face.getEdges(), size=M/2, 
#* deviationFactor=0.1, minSizeFactor=0.1)

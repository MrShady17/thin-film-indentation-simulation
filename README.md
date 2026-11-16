
# Modélisation de l'indentation de couches minces (Abaqus / Python)
 
Projet de modélisation du comportement mécanique de couches minces lors d'un essai d'indentation avec Abaqus.
 
---
 
## Sommaire
 
1. [Lancer Abaqus](#lancer-abaqus)
2. [Structure du script](#structure-du-script)
3. [Git](#travail-en-équipe-avec-git)
4. [Commandes Abaqus (terminal)](#commandes-abaqus-terminal)
5. [Commandes Python utiles dans Abaqus](#commandes-python-utiles-dans-abaqus)
6. [Commandes Linux utiles](#commandes-linux-utiles)
7. [Documentation utile](#documentation-utile)

---
 
## Lancer Abaqus
 
```bash
abaqus cae -mesa
```
 
---
 
## Structure du script
 
| Étape | Contenu |
|---|---|
| 0. Parameters | Paramètres géométriques, matériaux, chargement, maillage |
| 1. Model creation | Création du modèle |
| 2. Geometry | Croquis et création des parts |
| 3. Material and section | Matériaux, sections, affectations |
| 4. Assembly | Création des instances |
| 5. Analysis step | Définition des steps |
| 6. BC | Conditions aux limites et chargements |
| 7. Mesh | Taille, forme et type d'éléments, génération du maillage |
| 8. Job creation | Création des jobs |
 
---
 
## Git
 
Chacun code sa partie de son côté, puis on fusionne dans `main` quand le code est validé.
 
Intégration dans `main` :
 
1. Push sa branche.
2. Ouvrir une Pull Request sur GitHub (`branche -> main`).
3. L'autre membre relit et valide.
4. Merge dans `main`.

Commandes de base :
 
```bash
git clone <url-du-depot>              # cloner le dépôt
git checkout -b <ma-branche>          # créer sa branche et s'y placer
git checkout <branche>                # changer de branche
git status                            # état des fichiers modifiés
git add <fichier>                     # ajouter un fichier
git commit -m "Message clair"         # enregistrer les modifications
git push -u origin <ma-branche>       # pousser sa branche (première fois)
git push                              # pousser (ensuite)
git pull                              # récupérer les modifications distantes
git merge origin/main                 # intégrer main dans sa branche
```
 
---
 
## Commandes Abaqus (terminal)
 
```bash
abaqus cae -mesa                          # ouvrir CAE (mode logiciel de rendu)
abaqus cae script=mon_script.py           # ouvrir CAE et exécuter un script
abaqus cae noGUI=mon_script.py            # exécuter un script sans interface
abaqus python mon_script.py               # exécuter un script Python avec l'interpréteur d'Abaqus
abaqus job=NomJob input=NomJob.inp interactive   # lancer un calcul depuis un .inp
abaqus job=NomJob cpus=4 interactive      # lancer avec 4 cœurs
abaqus viewer odb=NomJob.odb              # ouvrir un résultat dans Abaqus/Viewer
abaqus help                               # aide générale
```
 
---
 
## Commandes Python utiles dans Abaqus
 
### Correspondance opération / commande
 
| Opération | Commande Python / objet typique |
|---|---|
| Create model | `mdb.Model(...)` |
| Create part | `model.Part(...)` |
| Create sketch | `model.ConstrainedSketch(...)` |
| Draw rectangle | `sketch.rectangle(...)` |
| Draw circle | `sketch.CircleByCenterPerimeter(...)` |
| Create material | `model.Material(...)` |
| Define elasticity | `material.Elastic(...)` |
| Create section | `model.HomogeneousSolidSection(...)` |
| Assign section | `part.SectionAssignment(...)` |
| Create instance | `assembly.Instance(...)` |
| Create analysis step | `model.StaticStep(...)` |
| Apply boundary condition | `model.DisplacementBC(...)` |
| Seed mesh | `part.seedPart(...)` |
| Generate mesh | `part.generateMesh()` |
| Create job | `mdb.Job(...)` |
 
### Explorer le modèle
 
```python
print(mdb.models.keys())                          # liste des modèles
print(mdb.models['NomModele'].parts.keys())       # liste des parts
print(mdb.jobs.keys())                            # liste des jobs
 
p = mdb.models['NomModele'].parts['NomPart']
print(len(p.faces), len(p.edges), len(p.vertices))   # nombre d'entités géométriques
 
for i, e in enumerate(p.edges):                   # repérer les arêtes par leurs coordonnées
    print(i, e.pointOn)
```
 
### Sélection par géométrie
 
```python
p.faces.findAt(((x, y, z),))                      # face contenant ce point
p.edges.findAt(((x, y, z),))                      # arête passant par ce point
p.edges.getByBoundingBox(xMin=0, xMax=1, yMin=-1, yMax=1, zMin=-1, zMax=1)   # arêtes dans une boîte
```
 
### Jobs
 
```python
job = mdb.jobs['NomJob']
job.submit()                                      # lancer le calcul
job.waitForCompletion()                           # attendre la fin avant de continuer
job.writeInput(consistencyChecking=OFF)           # écrire le .inp sans calculer
print(job.status)                                 # état du job (COMPLETED, ABORTED, ...)
```
 
---
 
## Commandes Linux utiles
 
### Navigation et fichiers
 
```bash
pwd                                   # dossier courant
ls -lh                                # lister avec tailles lisibles
ls *.odb                              # lister les résultats
cd <dossier>                          # changer de dossier
cd ..                                 # remonter d'un niveau
mkdir <dossier>                       # créer un dossier
cp <source> <destination>             # copier
cp -r <dossier> <destination>         # copier un dossier
mv <ancien> <nouveau>                 # déplacer / renommer
rm <fichier>                          # supprimer un fichier
rm -r <dossier>                       # supprimer un dossier
```
 
---

## Documentation utile

The official Abaqus Scripting User’s Guide is the primary reference. The following pages are
particularly relevant:


[Abaqus Scripting User’s Guide](https://docs.software.vt.edu/abaqusv2025/English/?show=SIMACAECMDRefMap%2Fsimacmd-c-ov.htm)

[Abaqus Scripting User’s Guide (pdf file)](http://abaqusdocs.eait.uq.edu.au/v6.11/pdf_books/SCRIPT_USER.pdf)

[Replaying an Abaqus/CAE session](https://docs.software.vt.edu/abaqusv2025/English/SIMACAECAERefMap/simacae-c-dbsfilesreplay.htm)

[Python Scripts for Abaqus](https://abaquspython.com/contents.html)

[Scripting in Abaqus with abapys](https://d-zo.github.io/abapys/abapysscripting.html)

---
from chimera import runCommand
from os import *

todo = []

for ligand in listdir("."):
    todo.append(ligand)


for ligand in todo:
    if ligand.__contains__(".pdb"):
        runCommand("open {}".format(ligand))
        runCommand("addh")
        runCommand("write 0 {}_withHs.pdb".format(ligand[0:-4]))
        runCommand("delete")

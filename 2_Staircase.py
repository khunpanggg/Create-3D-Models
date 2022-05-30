import maya.cmds as cmds
amount = 30
width = 5.0
height = 0.25
depth = 1
for i in range(amount):
    cmds.polyCube(w=width,h=height,d=depth)
    cmds.move(width/2, i * 0.5, 0)
    cmds.rotate(0, 12 * i, 0, p=[0,0,0])

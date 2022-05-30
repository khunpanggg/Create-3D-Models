import maya.cmds as cmds
amount = 18
width = 4.0
height = 0.5
depth = 4.0 / 3.0
for i in range(amount):
    cmds.polyCube(w=width,h=height,d=depth)
    cmds.move(0, (height / 2) + i * height, width/2 - depth/2)
    cmds.rotate(0, 90 * (i + 1), 0, p=[0,0,0])
    
    cmds.polyCube(w=width,h=height,d=depth)
    cmds.move(0, (height / 2) + i * height, -(width/2 - depth/2))
    cmds.rotate(0,90 * (i + 1), 0, p=[0,0,0])

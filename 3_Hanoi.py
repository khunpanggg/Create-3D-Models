import maya.cmds as cmds
cmds.polyCube(w=12.0, h=0.25, d=5.0, n='myCube#')
amount_pin = 3
for i in range(amount_pin):
    cmds.polyCylinder(r=0.1,h=4)
    cmds.move(12/4*i - 12/4,4/2,0)
amount_circle = 5
radius = 0.75
ax_y = 1.5
for i in range(amount_circle):
    cmds.polyCylinder(r=radius + 0.25 *i,h=0.25)
    cmds.move(0,ax_y/2 - 0.25 * i+0.5,0)
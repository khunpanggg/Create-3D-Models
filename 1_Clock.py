import maya.cmds as cmds
for i in range(12):
    cmds.polySphere(radius=1, name= 'mySphere#')
    cmds.move(0,0,6)
    cmds.rotate(360/12*i,0,0,p=[0,0,0])
cmds.polyCube(w=4.8, h=0.5, d=0.5, n='myCube#')
cmds.move(4.8/2,0,0)
cmds.rotate(0,0,90,p=[0,0,0])
cmds.polyCube(w=4, h=0.5, d=0.5, n='myCube#')
cmds.move((4.8/2)/(4.0/2)+0.55,0,0)
cmds.rotate(0,90,0,p=[0,0,0])
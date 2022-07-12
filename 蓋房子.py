from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z
寬=15
長=10
高=10
材質=57
air=0
mc.setBlocks(x,y,z,x+寬,y+高,z+長,材質)
mc.setBlocks(x+1,y+1,z+1,x+寬-1,y+高-1,z+長-1,air)
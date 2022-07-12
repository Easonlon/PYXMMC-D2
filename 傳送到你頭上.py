from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
time.sleep(5)

position=mc.player.getTilepos()
x=position.x
y=position.y
z=position.z

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+100
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
z=z+10
mc.player.setTilePos(x,y,z)
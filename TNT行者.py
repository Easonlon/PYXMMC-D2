
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x+1,y,z+1,x-1,y,z-1,133)
    time.sleep(0.2)
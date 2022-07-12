# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:32:45 2022

@author: Bacchus
"""
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
time.sleep(5)
x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,61)
mc.setBlock(x,y+1,z,61)
mc.setBlock(x,y+2,z,61)
mc.setBlock(x,y+3,z,61)
mc.setBlock(x,y+4,z,61)
mc.setBlock(x,y+5,z,61)
mc.setBlock(x,y+6,z,61)
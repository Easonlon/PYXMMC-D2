# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:06:26 2022

@author: Bacchus
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("  我的座標  ")

position=mc.player.getTilePos()
x=position.x
y=position.y
z=position.z

mc.postToChat("x"+str(x)+"    "+"y"+str(y)+"   "+"z"+str(z))



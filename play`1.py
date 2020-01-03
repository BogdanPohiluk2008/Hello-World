from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

time.sleep()
pos = mc.player.getPos()
blockAbove =  mc.getBlock(pos.x, pos.y + 2, pos.z)
score = score + 1
mc.postToChat("Текущий счет: " + str(score))

mc.postToChat("Окончательный счет: " + str(score))

if score > 6:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x -5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)


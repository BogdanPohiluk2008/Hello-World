import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
def elka():
    block.Block(17,1)
    mc.setBlocks(0,170,0,0,164,0,17)
    mc.setBlocks(0,171,0,0,173,0,41,29)
    mc.setBlock(1,172,-0,41,29)
    mc.setBlock(-1,172,-0,41,29)
    mc.setBlock(-1,170,-0,133,85)
    mc.setBlock(1,170,-0,133,85)
    mc.setBlock(0,170,-1,133,85)
    mc.setBlock(0,170,1,133,85)
    mc.setBlock(0,169,2,133,85)
    mc.setBlock(0,169,-2,133,85)
    mc.setBlock(2,169,0,133,85)
    mc.setBlock(-2,169,0,133,85)
    mc.setBlock(-3,168,0,133,85)
    mc.setBlock(0,168,-3,133,85)
    mc.setBlock(3,168,0,133,85)
    mc.setBlock(0,168,3,133,85)
    mc.setBlocks(50,163,0,0,163,50,2)
    while True:
        mc.setBlock(-2,169,0,57)
        time.sleep(2)
        mc.setBlock(-2,169,0,10)
        time.sleep(2)
    
    
    
elka()

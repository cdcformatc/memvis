from __future__ import division
from PIL import Image
from math import ceil

def colorblock(im,row,col,width,height,color,borders):
    for i in range(1,width):
        for j in range(height):
            im.putpixel((col*width + i, row*height + j), color)
            if borders:
                im.putpixel((col*width + 0, row*height + j), (0,0,0))
            
        if borders:
            im.putpixel((col*width + i, row*height + 0), (0,0,0))

def visualize(mem, fn, blocks_per_row=100, block_width=10, block_height=10, borders=True):
    red = (255,0,0)
    green = (0,255,0)
    black = (0,0,0)

    blocks = len(mem)
    rows = int(ceil(blocks / blocks_per_row))
    
    width = blocks_per_row * block_width
    height = rows * block_height
    
    size = width,height
    
    im = Image.new('RGBA',size,red)

    for row,i in enumerate(range(0,len(mem),blocks_per_row)):
        for col,x in enumerate(mem[i:i+blocks_per_row]):
            if x==0:
                color = red
            elif x==1:
                color = green
            else:
                color==black
        
            colorblock(im,row,col,block_width,block_height,color,borders)

    im.save(fn)

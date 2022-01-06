#!/usr/bin/env python



import stitchcode
import random


stitchlen = 20

#makes a simple pattern where a cell is colored if it has exactly one colored cell above it
def cellpattern1(pixels):
	pixels[size//2][size-1] = 1

	for y in range(size-2,0,-1):
		for x in range(1,size-1):
			pix1 = pixels[x-1][y+1]
			pix2 = pixels[x][y+1]
			pix3 = pixels[x+1][y+1]
			sumofpix = pix1 + pix2 + pix3
			if sumofpix == 1:
				pixels[x][y] = 1

#note: stitches define a point where the bobbin thread crosses the needle thread.  They are a single point on one end of a line, not a line with two end points

def makePixel(emb,x,y):
	#make a square
	emb.addStitch(stitchcode.Point(x*stitchlen,y*stitchlen))
	emb.addStitch(stitchcode.Point(x*stitchlen,(y+1)*stitchlen))
	emb.addStitch(stitchcode.Point((x+1)*stitchlen,(y+1)*stitchlen))
	emb.addStitch(stitchcode.Point((x+1)*stitchlen,y*stitchlen))
	emb.addStitch(stitchcode.Point(x*stitchlen,y*stitchlen))
	#make a cross
	emb.addStitch(stitchcode.Point((x+1)*stitchlen,(y+1)*stitchlen))
	emb.addStitch(stitchcode.Point((x+1)*stitchlen,y*stitchlen))
	emb.addStitch(stitchcode.Point(x*stitchlen,(y+1)*stitchlen))
	emb.addStitch(stitchcode.Point((x+1)*stitchlen,(y+1)*stitchlen))



def drawConnected(emb, pixels, x, y):

	makePixel(emb, x,y)

	if x+1 > len(pixels)-1:
		return
	if x == 0:
		return
	if y == 0:
		return

	#look at children
	pix1 = pixels[x-1][y-1]
	pix2 = pixels[x][y-1]
	pix3 = pixels[x+1][y-1]
	sumofpix = pix1 + pix2 + pix3

	if pix1 == 1:
		drawConnected(emb, pixels, x-1, y-1)
	if pix2 == 1:
		emb.addStitch(stitchcode.Point((x-1)*stitchlen, y*stitchlen))
		makePixel(emb, x, y-1)
	if pix3 == 1:
		drawConnected(emb, pixels, x+1, y-1)
		emb.addStitch(stitchcode.Point((x+1)*stitchlen, y*stitchlen))



if __name__ == "__main__":
	emb = stitchcode.Embroidery()

	size = 60

	pixels = []
	for i in range(size):
		pixels = pixels + [[0]*size]

	cellpattern1(pixels)

	drawConnected(emb, pixels, size//2, size-1)

	emb.translate_to_origin()
	emb.save_as_dst("pixels.dst")
	emb.save_as_png("pixels.png",True)

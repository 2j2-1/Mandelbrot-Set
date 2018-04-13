import pygame
import colorsys
import math

xoff = -1.786490521798148075303
yoff = 0
iteration = 50
def function(_x,_y,og=False):
	x = map(_x,[0,backgroundSize[0]],[-scale,scale])
	y = map(_y,[0,backgroundSize[1]],[-scale,scale])
	if not og:

		z = complex(x+xoff,y+yoff)
		
		c=z
		if (z.real+1)**2+z.imag**2>1/16:
			try:
				for i in range(iteration):
					if z.real*z.real+z.imag*z.imag>4:
						1/0
					# temp = z
					z = z**2+c
					if z == temp:
						return None
			except:
				return ((math.sin(i*0.0001)+1)/2)*255
		return None

def map(value,changed,og):
	return (value-changed[0])*(float(og[1]-og[0])/float(changed[1]-changed[0]))+og[0]


scale = 2
backgroundSize = [200,200]

pygame.init()
WHITE= [255, 255, 255]
MID = [backgroundSize[0]/2,backgroundSize[1]/2]
screen = pygame.display.set_mode(backgroundSize)
pygame.display.set_caption("Mandlebrot Set")
done = False
while not done:
	for x in xrange(backgroundSize[0]):
		for y in xrange(backgroundSize[1]):
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					done = True

			temp = function(x,y)
			if temp:
				v,h = 255, temp
			else:
				v,h = 0,0
			screen.set_at((x,y),colorsys.hsv_to_rgb(h,1,v))

	print "Done!"
	pygame.display.flip()
	scale*=0.5				
	iteration+=1
	print scale,iteration
	
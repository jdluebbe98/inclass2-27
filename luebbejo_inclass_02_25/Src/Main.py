'''
Created on Feb 25, 2020

@author: luebbejo
'''
from image_functions import *
im = Image.open("SiriusAndViolet.jpg")
print(im.width, im.height, im.mode, im.format) #Displays info about the image

#my_image = load_image("SiriusAndViolpet.jpg")
#my_image.show(my_image)


#make use of crop_image()
'''
im = Image.open("SiriusAndViolet.jpg")
im_cropped = crop_image(im, (200,300,400,500))
im_cropped.show()
'''

write_text_to_image("rhino.jpg", "This is a cool rhino")

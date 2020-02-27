'''
Created on Feb 25, 2020

@author: luebbejo
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import random
#import requests
from io import BytesIO 


"""
    Load an image file from disk
    :param filename: The file to load
    :return the image object
"""


def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        print("load_image(): Unable to load" + filename)
        return None # None is a keyword that represents a null pointer
    
    
    
def save_image( imageObject, outfilename ) :
    """
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    """
    try:
        imageObject.save( outfilename )
    except:
        print("save_image(): Unable to save" + outfilename)
        
        
def crop_image(imageObject, cropRegion): 
        im_c = imageObject.crop(cropRegion) # (left, top, right, bottom) it's a tuple!
        return im_c



def write_text_to_image(imageFile, text):
    """
    Write text onto an existing image. The result is written to sample-out.jpg
    :param imageFile: The image file name
    :param text: The text to write onto the image
    """
    #**************************************************
    #* Add text to an image
    #* https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    #* https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil
    #* Free fonts: https://www.fontsquirrel.com/fonts/list/classification/sans%20serif
    #**************************************************
    myImage = load_image(imageFile);
    draw = ImageDraw.Draw(myImage)
    # https://stackoverflow.com/questions/47694421/pil-issue-oserror-cannot-open-resource
    fontStyle = ImageFont.truetype("Aaargh.ttf", 48)     # font must be in the same folder as the .py file. 
    #Draw a random ellipse on the image. Be aware of size and fill settings
    '''
    from PIL import Image, ImageDraw
    image = Image.new("RGB", (100,200)) # It's new and it's all black
    Drawer.rectangle((50,50,75,75)) # One argument. It's a tuple.

    Drawer = ImageDraw.Draw(image) 
    Drawer.rectangle((60,60,90,90), fill=None, outline="red", width=10)

    image.show()
    '''
    # importing image object from PIL 
    import math
    for x in range (0,9):  
        w = random.randint(75, 95)
        h = random.randint(40, 55)
        shape = [(30, 30), (w - 10, h - 10)] 
      
        # creating new Image object 
        img = Image.new("RGB", (w, h)) 
      
        # create ellipse image 
        img1 = ImageDraw.Draw(img)   
        img1.ellipse(shape, fill = None , outline ="red") 
        img.show() 
    
    
    #Randomize the x,y of the text we are writing
    x = 30
    y = 20
    #Now randomize x and y. Research the random class. The text will clip if you're outside the picture
    #You can randomize based on myImage.width and myImage.height
    x = random.randrange(0, myImage.width - 250, 1)
    y = random.randrange(0, myImage.height - 250, 1)
    print(x)
    print(y)
    #create a loop step through the text letter by letter and print each letter randomly but make it look like the original text
    for letter in text:
        #Generate a random x,y for this letter. Make sure the new x,y is not too random from the previous x,y Here is my attempt
        '''
            letter = 0
            while letter < myImage.width:
                # Get random number in range 0 through 9.
                n = random.randint(0, myImage.width)
                print(n)
                letter += 1
        '''
        x = x + 30 + random.randint(-10, 10)
        y = y + random.randint(-10, 10)
        #print just the letter
        #print(letter)
        draw.text((x, y), letter, (255,255,255),font=fontStyle)    # Write in black
    myImage.save("sample-out.jpg")



        
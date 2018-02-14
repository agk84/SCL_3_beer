from PIL import Image

BLUR_D = 2

def blur(fptr):
    '''
    Blurring is an interesting problem with many issues involved.  Here we can
    simply follow an averaging value (by some pixel range) to find the blurred
    pixel value.

    For extra info:

        * https://www.youtube.com/watch?v=C_zFhWdM4ic
    '''

    # We can open IMG and img seperately, and only change img (thus, keeping
    # the original image unchanged for calculation purposes)
    IMG = Image.open(fptr)
    img = Image.open(fptr)
    # get image size
    width, height = img.size
    # set white to border pixels
    blur = tuple([255,255,255])
    for x in range(0,width):
      for i in range(0,BLUR_D):
        img.putpixel((x,i),blur)
        img.putpixel((x,height-1-i),blur)
    for y in range(0,height):
      for j in range(0,BLUR_D):
        img.putpixel((j,y),blur)
        img.putpixel((width-1-j,y),blur)
    # bluring image
    for x in range(BLUR_D,width-BLUR_D): 
        for y in range(BLUR_D,height-BLUR_D):
            #pxl = img.getpixel((x, y))
            blur = tuple(norm_pixels(img, IMG, x, y))
            img.putpixel((x, y), blur)
    # write back
    fptr_2 = fptr.split(".jpg")[0] + "_blurred.jpg"
    img.save(fptr_2)
    fptr_2 = fptr.split(".jpg")[0] + "_original.jpg"
    IMG.save(fptr_2)
# blur function
def norm_pixels(img, IMG, x, y):
  sum_l = []
  # build sum list
  for j in range(0,3):
    sum_l.append(0)
  # sum
  for x_blur in range(x-BLUR_D, x+1+BLUR_D):
    for y_blur in range (y-BLUR_D, y+1+BLUR_D):
      r, g, b = img.getpixel((x_blur,y_blur))
      sum_l[0] = sum_l[0]+r
      sum_l[1] = sum_l[1]+g
      sum_l[2] = sum_l[2]+b
  # average
  for i in range (0,3):
    sum_l[i] = sum_l[i]/((BLUR_D+2)**2)  
  # return pixels
  return sum_l

def set_luminance(fptr, l_val):
    '''
    CHALLENGE PROBLEM - For if you do blur.
    Luminance is a method of determining how "bright" the image is.  It can
    be easily calculated by per pixel as:

        l_pxl = 0.299 * R + 0.587 * G + 0.114 * B

    Now, for an entire image we can calculate either (1) the total luminance,
    or more scalable we can do (2) average luminance.  That is:

        l_avg = sum(l_pxl) / N_pxl

    This challenge is to set the luminance of an image to a user specified
    value, allowing us to essentially set how bright our image is.
    '''
    pass


blur("cat_1.jpg")


#!/usr/bin/python 
# usage: python resize.py filename 


import Image, os, sys

for filename in sys.argv[1:]: # sys.argv[1:] means taking commandline arguments one or more...
    img = Image.open(filename).resize( (200,200) ) # Resize image to 200 x 200 resolution
    out = file(os.path.splitext(filename)[0]+"_thumb.jpg", "w") # suffixing "_thumb.jpg" to an image so to keep original photos as it is
    try:
        img.save(out, "JPEG") # Save it in a JPEG format
    finally:
        out.close()


#!/usr/bin/env python3
from PIL import Image
import os, sys

path = "supplier-data/images/"
pictures = os.listdir(path)

for pic in pictures:
  #if file is tiff format
  if 'tiff' in pic:
    #split method off extension
    file_name = os.path.splitext(pic)[0]
    #specify destination and output name with desire extension
    outfile = "supplier-data/images/" + file_name + ".jpeg"
    try:
      #opens the file, resizes and saves as jpeg w/ basic rgb encoding
      Image.open(path + pic).convert("RGB").resize((600,400)).save(outfile,"JPEG")
    except IOError:
      #rgba files dont like to be converted and saved in the same operation, so I added io error handling
      print("cannot convert", pic)
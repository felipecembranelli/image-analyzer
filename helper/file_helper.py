import json
from types import SimpleNamespace
import os

from urllib import request as ulreq
from PIL import ImageFile

def load_original_data_mass_file(original_file):

    file_path = os.path.join(os.path.dirname(__file__), original_file)

    fin = open(file_path, "rt")
    
    # Using readlines()
    lines = fin.readlines()

    count = -1

    imagelist = []    

    # Strips the newline character
    for url in lines:
        count += 1
        print("Line{}: {}".format(count, url.strip()))

        try:
            ret = getsizes(url)

            imgSize = 0
            imgHeight = 0 
            imgWidth = 0

            if ret[0] is not None:
                    imgSize =  ret[0]
            if ret[1][0] is not None:
                    imgHeight =  ret[1][0]
            if ret[1][1] is not None:
                    imgWidth =  ret[1][1]

            newImageInfo = str(imgSize) + "," + str(imgHeight) + "," + str(imgWidth) + "," + url

            imagelist.append(newImageInfo)
        except:
            newImageInfo = str(imgSize) + "," + str(imgHeight) + "," + str(imgWidth) + "," + url
            
            imagelist.append(newImageInfo)

    return imagelist


def getsizes(uri):
    # get file size *and* image size (None if not known)
    file = ulreq.urlopen(uri)
    size = file.headers.get("content-length")
    if size: 
        size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size, p.image.size
            break
    file.close()
    return(size, None)

def saveList(filePath, imageListInfo):
        with open("output.txt", "w") as txt_file:
                for line in imageListInfo:
                        txt_file.write(line) # works with any number of elements in a line

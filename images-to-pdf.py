import os
import sys
import glob
import img2pdf 
from PIL import Image
from natsort import natsorted
import time

if __name__=="__main__":
	try:
		assert(len(sys.argv)==2)
	except AssertionError:
		print("Arguments must be 2\n1st Argument : the .py script\n2nd Argument : folder of images")
		sys.exit()
	try:
		assert(os.path.isdir(sys.argv[1])==True)
	except AssertionError:
		print(f"The {sys.argv[1]} does not exists or is not folder")
		sys.exit()
	try:
		imagelist = []
		imagelist.extend(glob.glob(sys.argv[1]+"/*.jpg"))
		imagelist.extend(glob.glob(sys.argv[1]+"/*.jpeg"))
		imagelist.extend(glob.glob(sys.argv[1]+"/*.jfif"))
		imagelist.extend(glob.glob(sys.argv[1]+"/*.png"))
		imagelist = natsorted(imagelist)
		#print(imagelist)
		print(f"{len(imagelist)} images found in the folder : {sys.argv[1]} (subfolders are not scanned)") 
		images=[]
		for image in imagelist:
			print(f"Adding {image}...")
			im = Image.open(image)
			im = im.convert("RGB")
			images.append(im)
		output_filename = sys.argv[1]+"/pdf_"+str(int(round(time.time() * 1000)))+".pdf"
		images[0].save(output_filename, save_all = True, quality=75, append_images = images[1:])
		print(f"\nPdf file has been created at : {output_filename}")
		print("Procedure finished successfully")
	except:
		print("An Error Occured ... Procedure finished unsuccessfully")
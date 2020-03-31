from pdf2image import convert_from_path
import os
import time
import sys
from pdf2image.exceptions import (PDFInfoNotInstalledError,PDFPageCountError,PDFSyntaxError)

if __name__ == "__main__":
	try:
		assert(len(sys.argv)==3)
		dpi = int(sys.argv[2])
	except ValueError:
		print("3rd Argument (dpi) must be integer")
		sys.exit()
	except AssertionError:
		print("Arguments must be 3")
		print("1st Argument : excecutable .py script")
		print("2nd Argument : .pdf file")
		print("3rd Argument : dpi")
		sys.exit()
	try:
		assert(sys.argv[1].endswith(".pdf") and os.path.exists(sys.argv[1]))
	except AssertionError:
		print("2nd Argument (file) must exist and be .pdf")
		sys.exit()

	initial_file_size = os.path.getsize(sys.argv[1])
	size_after_conversion = 0

	output_folder = os.path.splitext(sys.argv[1])[0]+"_images_"+str(int(round(time.time() * 1000)))+"_dpi_"+str(dpi)
	try:
		os.mkdir(output_folder)
		images = convert_from_path(sys.argv[1],dpi=dpi,fmt="jpeg",thread_count=1)
		for i, image in enumerate(images):
			print(f"Converting Page : {i+1}")
			fname = 'Page_'+str(i+1)+'.jpg'
			image.save(output_folder+"/"+fname)
			size_after_conversion += os.path.getsize(output_folder+"/"+fname)
		print(f"Program Finished Successfully... All images are saved at : {output_folder}")
	except:
		print("An Error Occurred. Posible Reasons :")
		print(f"Cannot create file {output_folder}")
		print("Cannot convert pdf pages into images")
		print(f"Cannot save the converted images to folder {output_folder}")

	print(f"Initial .pdf file : {initial_file_size} Bytes")
	print(f"Size after conversion : {size_after_conversion} Bytes")
	print(f"Rate : {round(((size_after_conversion/initial_file_size)*100),2)} %")
	if(round(((size_after_conversion/initial_file_size)*100),2)>100):
		print("\nNOTE !!!!!\nThe total file size of images after conversion is BIGGER than the initial .pdf (you may want exactly the opposite)")
	else:
		print("\nNOTE !!!!!\nThe total file size of images after conversion is SMALLER than the initial .pdf (you saved disk space)")

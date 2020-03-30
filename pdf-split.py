# install the PyPDF2 package before use the .py script
# pip install PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import os
import time

if __name__ == "__main__":
	if(len(sys.argv)!=4):
		print("Arguments must be 4")
		print("1st Argument : excecutable .py script")
		print("2nd Argument : .pdf file to be split")
		print("3rd Argument : page to start the split")
		print("4th Argument : page to stop the split")
		sys.exit()	
	try:
		start_page = int(sys.argv[2])
		stop_page = int(sys.argv[3])
		assert(stop_page>0 and start_page>0 and stop_page>=start_page)
	except ValueError:
		print("Start Page must be integer")
		print("Stop Page must be integer")
		sys.exit()
	except AssertionError:
		print("Start Page must be > 0")
		print("Stop Page must be > 0")
		print("Stop Page must be >= Start Page")
		sys.exit()
	try:
		assert(sys.argv[1].endswith(".pdf") and os.path.exists(sys.argv[1]) and not(PdfFileReader(open(sys.argv[1], 'rb')).isEncrypted))
	except AssertionError:
		print("The inserted file must exist")
		print("The inserted file must be .pdf")
		print("The inserted file must not be encrypted")
		sys.exit()
	total_pdf_pages = PdfFileReader(open(sys.argv[1], 'rb')).getNumPages()
	try:
		assert(start_page<=total_pdf_pages and stop_page<=total_pdf_pages)
	except AssertionError:
		print(f"The .pdf file you want has {total_pdf_pages} pages.")
		print("Start Page or Stop Page is above that value, please insert correct page numbers")
		sys.exit()
	# start split here
	try:
		# the new file will be saved to the folder of the first .pdf given
		output_filename_path = os.path.splitext(sys.argv[1])[0]+"_split_"+str(int(round(time.time() * 1000)))+".pdf"
		#print(output_filename_path)
		print("Splitting...")
		output_pdf = PdfFileWriter()
		with open(sys.argv[1], "rb") as in_file:
			input_pdf = PdfFileReader(in_file)
			for page in range(start_page-1,stop_page):
				pageObject = input_pdf.getPage(page)
				output_pdf.addPage(pageObject)
				with open(output_filename_path, "ab") as out_file:
					output_pdf.write(out_file)
		print(f"\nProgram Finished Successfully ... The new file has been created at {output_filename_path}")
	except:
		print("An Error Occurred While Splitting the File ... Program Finished Unsuccessfully")
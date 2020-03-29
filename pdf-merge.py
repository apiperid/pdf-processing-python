# install the PyPDF2 package before use the .py script
# pip install PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import os
import time

if __name__== "__main__":
	if(len(sys.argv)<3):
		print("The Arguments must be at least 3")
		print("1st Argument : excecutable .py script")
		print("2nd and 3rd Argument : .pdf files")
		print("> 3rd Argument : other .pdf files for merging")
		sys.exit()
	# checking all input files
	for i in range(1,len(sys.argv)):
		#print(sys.argv[i])
		print(f"\nChecking file : {sys.argv[i]}")
		existence = os.path.exists(sys.argv[i])
		print(f"----> Existence : {existence}")
		if(existence==False):
			print("Error Occured : This File does not exist")
			print("All inserted files must be .pdf (not encrypted) and exist ... Program Has Been Terminated")
			sys.exit()
		isPDF = sys.argv[i].endswith(".pdf")
		print(f"----> is PDF : {isPDF}")
		if(isPDF==False):
			print("Error Occured : This File is not .pdf")
			print("All inserted files must be .pdf (not encrypted) and exist ... Program Has Been Terminated")
			sys.exit()
		_isEncrypted = PdfFileReader(open(sys.argv[i], 'rb')).isEncrypted
		print(f"----> is Encrypted : {_isEncrypted}")
		if(_isEncrypted==True):
			print("Error Occured : This File is encrypted")
			print("All inserted files must be .pdf (not encrypted) and exist ... Program Has Been Terminated")
			sys.exit()
	# start merging here
	try:
		# the new file will be saved to the folder of the first .pdf given
		output_filename_path = os.path.splitext(sys.argv[1])[0]+"_merged_"+str(int(round(time.time() * 1000)))+".pdf"
		#print(output_filename_path)
		print("Merging...")
		output_pdf = PdfFileWriter()
		for i in range(1,len(sys.argv)):
			print(sys.argv[i])
			with open(sys.argv[i], "rb") as in_file:
				input_pdf = PdfFileReader(in_file)
				output_pdf.appendPagesFromReader(input_pdf)
				with open(output_filename_path, "ab") as out_file:
					output_pdf.write(out_file)
		print(f"\nProgram Finished Successfully ... The new file has been created at {output_filename_path}")
	except:
		print("An Error Occured While Merging ... Program Finished Unsuccessfully")
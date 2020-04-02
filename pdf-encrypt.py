# install the PyPDF2 package before use the .py script
# pip install PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import os
import time

if __name__=="__main__":
	if(len(sys.argv)!=3):
		print("Arguments must be exactly 3")
		print("1st Argument : excecutable .py file")
		print("2nd Argument : .pdf file to be encrypted")
		print("3rd Argument : the password for encryption")
		sys.exit()
	if(sys.argv[1].endswith(".pdf")==False):
		print("The file you want to encrypt is not .pdf")
		sys.exit()

	output_filename = os.path.splitext(sys.argv[1])[0]+"_encrypted_"+str(int(round(time.time() * 1000)))+".pdf"
	#print(output_filename)
	try:
		with open(sys.argv[1], "rb") as in_file:
			input_pdf = PdfFileReader(in_file)
			if(input_pdf.isEncrypted):
				print("The .pdf file is already encrypted\n")
				sys.exit()
			output_pdf = PdfFileWriter()
			output_pdf.appendPagesFromReader(input_pdf)
			output_pdf.encrypt(sys.argv[2])
			with open(output_filename, "wb") as out_file:
				output_pdf.write(out_file)
		print(f"Program Finished, the encrypted file has been created at : {output_filename}")
	except:
		print("An Error Occured . Possible reasons :")
		print("a) The file you inserted does not exist")
		print("b) Error occured while encrypting")
		print("c) Error occured while writing to new file")
		print("d) The .pdf file is already encrypted")
# You have to install the package : PyPDF2 first to use this script
# pip install PyPDF2 is the shell command
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import sys

if __name__ == "__main__":
	try:
		assert(len(sys.argv)==3)
	except AssertionError:
		print("The Arguments must be 3")
		print("1st Argument : excecutable .py script")
		print("2nd Argument : .pdf file to be cracked")
		print("3rd Argument : .txt file which contains passwords you want to try on .pdf")
		sys.exit()
	try:
		assert(sys.argv[1].endswith(".pdf") and os.path.exists(sys.argv[1]) and PdfFileReader(open(sys.argv[1], 'rb')).isEncrypted)
	except AssertionError:
		print(f"The file : {sys.argv[1]} either IS NOT .pdf or DOES NOT EXIST or IS NOT ENCRYPTED")
		sys.exit()
	try:
		assert(sys.argv[2].endswith(".txt") and os.path.exists(sys.argv[2]))
	except AssertionError:
		print(f"The file : {sys.argv[2]} either IS NOT .txt or DOES NOT EXIST")
		sys.exit()
	try:
		num_lines = sum(1 for line in open(sys.argv[2]))
		print(f"The file has {num_lines} passwords")
		txtFile = open(sys.argv[2])
		pdfFile = open(sys.argv[1],"rb")
		input_pdf = PdfFileReader(pdfFile)
		for i in range(num_lines):
			password = txtFile.readline().strip()
			if(input_pdf.decrypt(password)==0):
				print(f"Trying Password : {password} , ({i+1}/{num_lines}) ----> Failed")
			else:
				print(f"Trying Password : {password} , ({i+1}/{num_lines}) ----> Success . Password Found")
				raise ValueError() # it is just for escaping because of found password
	except ValueError:
		print()
	except:
		print("An Error Occurred . Posible Reasons :")
		print(f"Error in opening file : {sys.argv[2]}")
		print(f"Error in opening file : {sys.argv[1]}")
	finally:
		txtFile.close()
		pdfFile.close()
# pdf-processing-python
In this repository i provide python scripts which help the processing of a pdf file.To be more specific you the scripts are about pdf encryption,decryption,merging,splitting,turning every pdf file (every page) into images (this is about to save disk space if you want) and a program to crack the password of a protected pdf file.
It is kwown that all the above can be done using software (e.g PDFSamBasic) or online tools , but with these .py files there is no need for extra software or upload to internet (which can be dangerous if it is about personal data).

# Essential setups
You must only install PyPDF2  and pdf2image by :<br>
`pip install PyPDF2`<br>
`pip install pdf2image`

## pdf-encrypt.py
This .py script gets a non-protected pdf file and encrypt it with a password user gives

#### Arguments
* argv[0] : pdf-encrypt.py
* argv[1] : your .pdf file (decrypted)
* argv[2] : the password you want to be used

#### Output
A new .pdf file (encrypted) at the same folder as the decrypted

## pdf-decrypt.py
Decrypt an already encrypted .pdf file

#### Arguments
* argv[0] : pdf-decrypt.py
* argv[1] : your .pdf file (encrypted)
* argv[2] : the password you want to be used

#### Output
A new .pdf file (decrypted) at the same folder as the encrypted

## pdf-merge.py
Turns many .pdf files into one

#### Arguments
* argv[0] : pdf-merge.py
* argv[1] ... argv[N] : .pdf files to be used at the merge procedure

#### Output
.pdf file which contains all the .pdf inserted saved at the path of the first

## pdf-split.py

#### Arguments

#### Output

## pdf-to-images.py

#### Arguments

#### Output

## pdf-crack.py

#### Arguments

#### Output

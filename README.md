# pdf-processing-python
In this repository i provide python scripts which help the processing of a pdf file.To be more specific you the scripts are about pdf encryption,decryption,merging,splitting,turning every pdf file (every page) into images (this is about to save disk space if you want) and a program to crack the password of a protected pdf file.
It is kwown that all the above can be done using software (e.g PDFSamBasic) or online tools , but with these .py files there is no need for extra software or upload to internet (which can be dangerous if it is about personal data).

# Essential setups
You must install first packages : img2pdf,natsort,pdf2image,Pillow,PyPDF2<br>
`pip install img2pdf`<br>
`pip install natsort`<br>
`pip install pdf2image`<br>
`pip install Pillow`<br>
`pip install PyPDF2`

## pdf-encrypt.py
This .py script gets a non-protected pdf file and encrypt it with a password user gives<br>
`python argv[0] argv[1] argv[2]`

#### Arguments
* argv[0] : pdf-encrypt.py
* argv[1] : your .pdf file (decrypted)
* argv[2] : the password you want to be used

#### Output
A new .pdf file (encrypted) at the same folder as the decrypted

## pdf-decrypt.py
Decrypt an already encrypted .pdf file<br>
`python argv[0] argv[1] argv[2]`

#### Arguments
* argv[0] : pdf-decrypt.py
* argv[1] : your .pdf file (encrypted)
* argv[2] : the password you want to be used

#### Output
A new .pdf file (decrypted) at the same folder as the encrypted

## pdf-merge.py
Turns many .pdf files into one<br>
`python argv[0] argv[1]...argv[N]`

#### Arguments
* argv[0] : pdf-merge.py
* argv[1] ... argv[N] : .pdf files to be used at the merge procedure (decrypted)

#### Output
.pdf file which contains all the .pdf inserted saved at the path of the first

## pdf-split.py
Splits a .pdf file from page.X to page.Y where X,Y are page numbers user gives<br>
`python argv[0] argv[1] argv[2] argv[3]`

#### Arguments
* argv[0] : pdf-split.py
* argv[1] : .pdf file to be split (decrypted)
* argv[2] : from which page to start
* argv[3] : to which page it will stop

#### Output
New .pdf file which contains only the pages in range [page.X,page.Y]

## pdf-to-images.py
Turn a .pdf file into mutilple .jpg images (each page a single .jpg file)<br>
`python argv[0] argv[1] argv[2]`

#### Arguments
* argv[0] : pdf-to-images.py
* argv[1] : .pdf file to turn into images (decrypted)
* argv[2] : dpi of image (bigger dpi means better resolution and bigger size)

#### Output
New folder which contains each .pdf page as image

## pdf-crack.py
Tries passwords given from a .txt file to find the password of an encrypted .pdf<br>
`python argv[0] argv[1] argv[2]`

#### Arguments
* argv[0] : pdf-crack.py
* argv[1] : .pdf to be cracked (encrypted)
* argv[2] : the .txt containing the possible passwords

#### Output
In which password we had success (or no success)

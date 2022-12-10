# DocuSep | Imports
## Main files needed are DocuSep_OCR.py, Functions.py, and if you want images to test there are images in the images folder.
-Ignore Handwritten_Test.ipynb that is what we used as a foundation for the two main files.
## Link for patent: https://patents.google.com/patent/US7072514B1/en
## For this to work there are some imports that need to be done.
### You will need to download Pytesseract and Poppler.
- Once that is done you will need to list the path for them:
### PyTesseract
- Download Link: https://github.com/UB-Mannheim/tesseract/wiki
```
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
### Poppler
- Download Link: https://blog.alivate.com.au/poppler-windows/ grab the latest binary
- Then extract in you where you downloaded it. Then move to C:\Program Files\poppler-0.68.0\bin
```
  poppler_path=r'C:\Program Files\poppler-0.68.0\bin'
```
### Pip Installs
```
pip install opencv-python
pip install numpy
pip install pytesseract
pip install image2pdf
pip install tk
pip install pillow
pip install pdf2image
```
### Images will be resized to 400x650
### Once the GUI opens if you resize the width of the window the scrollbar will activte
### More than 6 iamges in a window will mess up the labels for the catagories

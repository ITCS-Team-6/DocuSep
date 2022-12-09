# DocuSep | Imports
## For this to work there are some imports that need to be done.
### You will need to download Pytesseract and Poppler.
- Once that is done you will need to list the path for them:
### PyTesseract
- Download Link: https://github.com/UB-Mannheim/tesseract/wiki
```
pytesseract.pytesseract.tesseract_cmd =r'<full_path_to_your_tesseract_executable>'
```
### Poppler
- Download Link: https://blog.alivate.com.au/poppler-windows/ grab the latest binary
```
  poppler_path=r'<full_path_to_your_plopper_bin_folder>'
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

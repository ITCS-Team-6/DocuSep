# DocuSep | Imports
## For this to work there are some imports that need to be done.
### You will need to dowmload Pytesseract and Poppler.
- Once that is done you will need to list the path for them:
### PyTesseract
```
pytesseract.pytesseract.tesseract_cmd =r'<full_path_to_your_tesseract_executable>'
```
### Plopper
```
  poppler_path=r'<full_path_to_your_plopper_bin_folder>'
```
### Pip Installs
```
pip install opencv-python
pip install numpy
pip install pytesseract
pip install image2pdf
pip install tkinter
pip install pillow
```
#### Glob and OS are already part of python, no install is necessary.

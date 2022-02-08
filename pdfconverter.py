""" PyPDF2 License """
""" Copyright (c) 2006-2008, Mathieu Fenniak
Some contributions copyright (c) 2007, Ashish Kulkarni <kulkarni.ashish@gmail.com>
Some contributions copyright (c) 2014, Steve Witham <switham_github@mac-guyver.com>

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
* The name of the author may not be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE. """

""" Tkinter License """
""" MIT License

Copyright (c) 2018 Packt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from io import open
import PyPDF2
import sys

""" ---- Inicio Funciones ---- """

"""Merge funtions"""
def openMergeWindow():
  global fileEntryMerge1
  global fileEntryMerge2
  # Array con los PDFs
  global pdfsList
  pdfsList = list()
  pdfsList = [None] * 2
  
  # Root mergeWindow
  mergeWindow = Toplevel(root)
  mergeWindow.geometry("500x550")
  mergeWindow.resizable(False, False)
  mergeWindow.config(bd = 30, relief = FLAT, background = "#CACECF")
  mergeWindow.title('Combinar archivos')
  
  definicion = Frame(mergeWindow)
  definicion.pack(padx = 0, pady = 0)
  Label(definicion, text = "Combinar dos archivos PDF\nen un archivo resultante",  
        bg="#CACECF", font = ("Helvetica", 12)).pack()
       
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
  
  # Leer el primer archivo 
  archivo1 = Label(mergeWindow, text = "Archivo 1: ",  bg="#CACECF", font = ("Helvetica", 12))
  archivo1.pack()
                   
  fileEntryMerge1 = Entry(mergeWindow, font = ("Helvetica", 16), width = 40)
  fileEntryMerge1.pack()
  
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
        
  btn1 = Button(mergeWindow, text = "Seleccionar", relief = RAISED, bg = "#000000", 
       fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: btn1_click())
  btn1.pack()
  
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
        
  btnC1 = Button(mergeWindow, text = "Limpiar", relief = RAISED, bg = "#000000", 
       fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: btnC1_click())
  btnC1.pack()
  
  # Leer el segundo archivo
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
        
  archivo2 = Label(mergeWindow, text = "Archivo 2:", bg = "#CACECF", font = ("Helvetica", 12))
  archivo2.pack()
  
  fileEntryMerge2 = Entry(mergeWindow, font = ("Helvetica", 16), width = 40)
  fileEntryMerge2.pack()
  
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
        
  btn2 = Button(mergeWindow, text = "Seleccionar", relief = RAISED, bg = "#000000",
                fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: btn2_click())
  btn2.pack()
  
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
        
  btnC2 = Button(mergeWindow, text = "Limpiar", relief = RAISED, bg = "#000000", 
       fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: btnC2_click())
  btnC2.pack()
  
  # Juntar archivos 
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
  Label(mergeWindow, text = "", bg = "#CACECF").pack()
  
  btn3 = Button(mergeWindow, text = "Juntar", relief = RAISED, bg = "#000000",
                fg = "#FAFAFA", font = ("Helvetica", 15), activebackground = "#11B0D8", command = lambda: btn3_click())
  btn3.pack()

# Handlers
def btn1_click():
  openFiles(1)
def btnC1_click():
  try:
    pdfsList[0] = None
  except: 
    fileEntryMerge1.delete(0, END)
  fileEntryMerge1.delete(0, END)
  
def btn2_click():
  openFiles(2)
def btnC2_click():
  try:
    pdfsList[1] = None
  except: 
    fileEntryMerge2.delete(0, END)
  fileEntryMerge2.delete(0, END)
  
def btn3_click():
  if len(pdfsList) == 2:
    PDFMerge()
  else:
    messagebox.showwarning("Advertencia","Por favor selecciona dos archivos")

# Open File
def openFiles(flag):
  if flag == 1: 
    
    file1 = askopenfilename(initialdir = "/", defaultextension = ".pdf", filetypes = [("Archivos PDF", ".pdf")])
    if file1 == "":
      file1 = None
      messagebox.showwarning("Advertencia","Archivo invalido o falta de archivo")
    else: 
      fileEntryMerge1.delete(0, END)
      fileEntryMerge1.config(fg = "#000000")
      fileEntryMerge1.insert(0, file1)
      # Insertamos en la lista
      pdfsList[0] = file1
      
  elif flag == 2: 
    
    file2 = askopenfilename(initialdir = "/", defaultextension = ".pdf", filetypes = [("Archivos PDF", ".pdf")])
    if file2 == "":
      file2 = None
      messagebox.showwarning("Advertencia","Archivo invalido o falta de archivo")
    else: 
      fileEntryMerge2.delete(0, END)
      fileEntryMerge2.config(fg = "#000000")
      fileEntryMerge2.insert(0, file2)
      # Insertamos en la lista
      pdfsList[1] = file2
    
def PDFMerge():
  # Objeto Merger 
  try:
    if fileEntryMerge1 == None or fileEntryMerge2 == None:
      messagebox.showwarning("Advertencia","Por favor selecciona dos archivos")
    else:
      pdfMerger = PyPDF2.PdfFileMerger()
      
      # Appending pages 
      for pdf in pdfsList: 
        pdfMerger.append(pdf)
      
      try:
        pdfMerger.write(asksaveasfilename(initialdir = "/", defaultextension = '.pdf',
                         filetypes = [("PDF File", ".pdf")]))
        pdfMerger.close()
      except: 
        messagebox.showwarning("Advertencia","Porfavor ingresa el nombre del nuevo archivo")
  except:
    messagebox.showwarning("Advertencia","Verificar que el archivo sea valido")
  
"""End Merge Functions"""

"""Split Functions"""
def openSplitWindow():
  global fileEntrySplit1
  global fileEntrySplit2
  global num1
  num1 = IntVar()
  global num2
  num2 = IntVar()
  # Root Split Window
  splitWindow = Toplevel(root)
  splitWindow.geometry("500x550")
  splitWindow.resizable(False, False)
  splitWindow.config(bd = 30, relief = FLAT, background = "#CACECF")
  splitWindow.title("Separar Archivos")
  
  definicion = Frame(splitWindow)
  definicion.pack(padx = 0, pady = 0)
  Label(definicion, text = "Separar archivos PDF",  
        bg="#CACECF", font = ("Helvetica", 12)).pack()
        
  Label(splitWindow, text = "", bg = "#CACECF").pack()
        
  # Leer archivo a separar
  archivo1 = Label(splitWindow, text = "Archivo: ",  bg="#CACECF", font = ("Helvetica", 12))
  archivo1.pack()

  fileEntrySplit1 = Entry(splitWindow, font = ("Helvetica", 16), width = 40)
  fileEntrySplit1.pack()
  
  Label(splitWindow, text = "", bg = "#CACECF").pack()
        
  splitBtn = Button(splitWindow, text = "Seleccionar", relief = RAISED, bg = "#000000", 
       fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: splitBtn_click())
  splitBtn.pack()
  
  Label(splitWindow, text = "", bg = "#CACECF").pack()
        
  splitBtnC = Button(splitWindow, text = "Limpiar", relief = RAISED, bg = "#000000", 
       fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: splitBtnC_click())
  splitBtnC.pack() 
  
  # Nuevo nombre
  Label(splitWindow, text = "Nombre de los nuevos archivos [nombre1-n]:", bg="#CACECF", font = ("Helvetica", 12) ).pack()
  fileEntrySplit2 = Entry(splitWindow, font = ("Helvetica", 16), width = 40)
  fileEntrySplit2.pack()
  
  # Botones funciones
  Label(splitWindow, text = "", bg = "#CACECF").pack()
  Label(splitWindow, text = "", bg = "#CACECF").pack()
  
  # Splitsome
  splitSomeE = Frame(splitWindow, bg = "#CACECF", width = "150")
  splitSomeE.pack(side = LEFT)
  
  Label(splitSomeE, text = "Separar un grupo de paginas\nen especifico", bg = "#CACECF").pack()
  Label(splitSomeE, text = "De:", bg = "#CACECF").pack()
        
  Entry(splitSomeE, font = ("Helvetica", 10), width = 15, textvariable = num1).pack()
  
  Label(splitSomeE, text = "Hasta:", bg = "#CACECF").pack()
        
  Entry(splitSomeE, font = ("Helvetica", 10), width = 15, textvariable = num2).pack()
  
  Label(splitSomeE, text = "", bg = "#CACECF").pack()
        
  splitSomeBtn = Button(splitSomeE, text = "Separar", relief = RAISED, bg = "#000000",
                fg = "#FAFAFA", font = ("Helvetica", 15), activebackground = "#11B0D8", command = lambda: splitSome_click())
  splitSomeBtn.pack()    
  
  # Splitall 
  splitAll = Frame(splitWindow, bg = "#CACECF", width = "250")
  splitAll.pack(side = RIGHT)
  
  Label(splitAll, text = "Separar todos los elementos del archivo\nen paginas separadas", bg = "#CACECF").pack()
        
  Label(splitAll, text = "", bg = "#CACECF").pack()
        
  splitAllBtn = Button(splitAll, text = "Separar", relief = RAISED, bg = "#000000",
                fg = "#FAFAFA", font = ("Helvetica", 15), activebackground = "#11B0D8", command = lambda: splitAll_click())
  splitAllBtn.pack()
  
# Handlers
def splitBtn_click():
  openFile(fileEntrySplit1)
def splitBtnC_click():
  fileEntrySplit1.delete(0, END)
def splitSome_click():
  PDFsplitsome()
def splitAll_click():
  PDFsplitall()
  
def PDFsplitsome(): 
    try:
      pdfFileObj = open(fileEntrySplit1.get(), 'rb')
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
      pathName = askdirectory(initialdir = "/")
      try:
        startPage = int(num1.get())
        endPage = int(num2.get())
      except:
        exit
      for i in range(startPage -1, endPage):
        output = PyPDF2.PdfFileWriter()
        output.addPage(pdfReader.getPage(i))
        k = str(fileEntrySplit2.get())
        name = pathName + "/{}{}.pdf".format(fileEntrySplit2.get(),i+1)
        output.write(open(name,'wb'))
        pdfFileObj.close()
    except:
      messagebox.showwarning("ERROR","Verificar que el archivo sea valido.\nIngresar valores enteros")
      
def PDFsplitall():
  try:
    pdfFileObj = open(fileEntrySplit1.get(), 'rb')
    # PDF reader objetct 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pathName = askdirectory(initialdir = "/")
    for i in range(pdfReader.numPages):
        output = PyPDF2.PdfFileWriter()
        # Obtenemos cada una de las paginas y hacemos un archivo nuevo 
        output.addPage(pdfReader.getPage(i))
        name = pathName + "/{}{}.pdf".format(fileEntrySplit2.get(),i+1)
        output.write(open(name, 'wb'))
    
    # Cerramos el PDF inicial 
    pdfFileObj.close()
  except:
    messagebox.showwarning("ERROR","Verificar que el archivo sea valido e ingresar valores enteros")
    
"""End Split Functions"""      

"""Rotate Functions"""
def openRotateWindow():
  
  global fileEntryRotate1
  global fileEntryRotate2
  
  # Root Rotate Window
  rotateWindow = Toplevel(root)
  rotateWindow.geometry("500x400")
  rotateWindow.resizable(False, False)
  rotateWindow.config(bd = 30, relief = FLAT, background = "#CACECF")
  rotateWindow.title("Girar Archivo")
  
  definicion = Frame(rotateWindow)
  definicion.pack(padx = 0, pady = 0)
  Label(definicion, text = "Rotar un archivo",
        bg = "#CACECF", font = ("Helvetica", 12)).pack()
  
  Label(rotateWindow, text = "", bg = "#CACECF").pack()
        
  # Leer archivo
  archivo1 = Label(rotateWindow, text = "Archivo:", bg = "#CACECF", font = ("Helvetica", 12))
  archivo1.pack()
  
  fileEntryRotate1 = Entry(rotateWindow, font = ("Helvetica", 16), width = 40)
  fileEntryRotate1.pack()
  
  Label(rotateWindow, text = "", bg = "#CACECF").pack()
        
  rotateBtn = Button(rotateWindow, text = "Seleccionar", relief = RAISED, bg = "#000000",
                     fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: rotateBtn_click())
  rotateBtn.pack()

  Label(rotateWindow, text = "", bg = "#CACECF").pack()

  rotateBtnC =  Button(rotateWindow, text = "Limpiar", relief = RAISED, bg = "#000000",
                     fg = "#FAFAFA", font = ("Helvetica", 9), activebackground = "#11B0D8", command = lambda: rotateBtnC_click())
  rotateBtnC.pack()
  
  # Nuevo nombre
  Label(rotateWindow, text = "", bg = "#CACECF").pack()
  Label(rotateWindow, text = "Nombre del nuevo archivo:", bg="#CACECF", font = ("Helvetica", 12) ).pack()
        
  fileEntryRotate2 = Entry(rotateWindow, font = ("Helvetica", 16), width = 40)
  fileEntryRotate2.pack()
  
  # Rotar 
  Label(rotateWindow, text = "", bg = "#CACECF").pack()
  
  rotate = Button(rotateWindow, text = "Rotar", relief = RAISED, bg = "#000000",
                  fg = "#FAFAFA", font = ("Helvetica", 15), activebackground = "#11B0D8", command = lambda: rotate_click())
  rotate.pack()
  
def rotateBtn_click():
  openFile(fileEntryRotate1)
def rotateBtnC_click():
  fileEntryRotate1.delete(0, END)
def rotate_click():
  PDFRotate()
  
def PDFRotate():
    
  try:
    # Pdf object
    pdfFileObj = open(fileEntryRotate1.get(), 'rb')
    
    # Reader 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    pathName = askdirectory(initialdir = "/")
    
    #Writer
    pdfWriter = PyPDF2.PdfFileWriter()
    
    for page in range(pdfReader.getNumPages()):
        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(270)
        
        # Anadimos la pagina 
        pdfWriter.addPage(pageObj)
    name = pathName + "/{}.pdf".format(fileEntryRotate2.get())  
    pdfWriter.write(open(name, 'wb'))
    
    pdfFileObj.close()
  except:
    messagebox.showwarning("ERROR","Verificar que el archivo sea valido")

"""End Rotate Functions"""

""" Open File (single) """
def openFile(fileEntry):
  file1 = askopenfilename(initialdir = "/", defaultextension = ".pdf", filetypes = [("Archivos PDF", ".pdf")])
  if file1 == "":
      file1 = None
      return
  else: 
      fileEntry.delete(0, END)  #fileEntry1
      fileEntry.config(fg = "#000000")
      fileEntry.insert(0, file1)
      # Insertamos en la lista
      nuevoPdf = file1
""" End open file (single) """

""" ---- Fin funciones ---- """


""" Inicio Tkinter """
# Raiz 
root = Tk()
root.title('PDFs converter')
root.resizable(width = 0, height = 0)
root.geometry("700x560")
root.config(bd = 30, relief = FLAT, background = "#CACECF")


# Oopciones
frame = Frame(root) 
frame.pack(padx = 0, pady = 0)
#Agragamos un label       
Label(frame, text = "\nManipulador de PDFs", bg="#CACECF", font = ("Helvetica", 24)).pack()
      
Label(root, text="", bg = "#CACECF").pack()
      
# Frame por opcion.
""" MERGE """
merge = Frame(root, bg = "#CACECF")
merge.pack()

Label(merge, text = "Juntar archivos", bg = "#CACECF", font = ("Helvetica", 20)).pack()
      
Label(merge, text = "Combinar archivos PDF en uno solo", bg = "#CACECF", font = ("Helvetica", 16)).pack()
      
Button(merge, text = "Ir", width = 15, height = 1, relief = RAISED, bg = "#000000", 
       fg = "#FAFAFA", font = ("Helvetica", 14), activebackground = "#11B0D8", command = openMergeWindow).pack()

""" SPLIT """
split = Frame(root, bg = "#CACECF")
split.pack()

Label(split, text = "Separar archivo", bg = "#CACECF", font = ("Helvetica", 20)).pack()
      
Label(split, text = "Seprar paginas de un PDF", bg = "#CACECF", font = ("Helvetica", 16)).pack()
      
Button(split, text = "Ir", width = 15, height = 1, relief = RAISED, bg = "#000000", 
         fg = "#FAFAFA", font = ("Helvetica", 14), activebackground = "#11B0D8", command = openSplitWindow).pack()

""" ROTATE """
rotate = Frame(root, bg = "#CACECF")
rotate.pack()

Label(rotate, text = "Rotar archivo", bg = "#CACECF", font = ("Helvetica", 20)).pack()
      
Label(rotate, text = "Rotar un arhivo PDF", bg = "#CACECF", font = ("Helvetica", 16)).pack()
      
Button(rotate, text = "Ir", width = 15, height = 1, relief = RAISED, bg = "#000000", 
       fg = "#FAFAFA", font = ("Helvetica", 14), activebackground = "#11B0D8", command = openRotateWindow).pack()


# Loop 
root.mainloop()

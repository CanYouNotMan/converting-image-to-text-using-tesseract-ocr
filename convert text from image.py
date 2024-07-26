#converting Image to text using tesseract ocr
import pyautogui
from PIL import Image  
from pytesseract import *

#accessing the tesseract command intepreter
pytesseract.tesseract_cmd =(r"C:\Users\nickh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe")

#now testing the interpreter
print ("opening and reading text...")
image = Image.open("splitFunctionTest.png")
#(optional)
# #making the bigger so the text can read it better
# print("resizing image...")
# new_size = tuple(4*x for x in img.size)
# image = image.resize(new_size, Image.ANTIALIAS)

#output the message
print("outputting the message now...")
output = pytesseract.image_to_string(image)
print(output)

#(optional)
#we can separate value with comma by using the split function
output = output.split(',')
#this will turn output into as many container as number appear in the text. So if output have 9822,5012 it would turn into output[0] = 9822 and output[1] = 5012 ***still a string***
print(output[0])
print(output[1])
print(output)

#convert text to another language (doesn't work as you need more file)
# output2 = pytesseract.image_to_string(image,lang='fra')
# print(output2)
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:05:47 2021

@author: Ishan
"""
import pyttsx3 as tts
from tkinter import filedialog as fd
import docx2txt

def select_file():
    file_path = fd.askopenfilename(title='Open a file', initialdir='/',)
    return file_path




choice = input('Do you have a file or any particular sentence you want read aloud?(F/S) \n')
if choice == 'F':
	file_path = select_file()
	text = docx2txt.process(file_path)

elif choice == 'S':
	text = input('Enter your text: \n')

engine = tts.init()
engine.setProperty('rate',125)
engine.say(text)
engine.runAndWait()



from gtts import gTTS
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
import os


try:
    Tk().withdraw()
    filelocation = askopenfilename()
    pdf_File = open(filelocation, 'rb')
    pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
    count = pdf_Reader.numPages
    textList = []    
    for i in range(count):
        try:
            page = pdf_Reader.getPage(i)
            textList.append(page.extractText())
        except:
            pass


    textString = " ".join(textList)
    myAudio = gTTS(text=textString, lang='en', slow=False)
    audio_name = input("Enter name of your audio book : ")
    print("wait working")
    myAudio.save(audio_name + ".mp3")
    while True:
        preference = input("Do you want to play audio 'y' for yes 'n' for no  ").lower()
        if preference == 'y':
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            audio_file_path = os.path.join(BASE_DIR, audio_name + '.mp3')
            open(audio_file_path)
            os.startfile(audio_file_path)
            break
        elif preference == 'n':
            print("your file saved ")
            break
        else:
            print("enter correct option ")
            continue
except:
    print('try again')


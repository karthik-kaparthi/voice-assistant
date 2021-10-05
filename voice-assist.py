import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import speedtest #pip install speechRecognitation
import wikipedia   #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os 
import pyautogui #pip install pyautogui #pip install pillow
import random 
import json
import requests
import wolframalpha #pip install wolframalpha
import time
import sys
import pywhatkit
import cv2
import numpy as np



from wikipedia.wikipedia import search
from urllib.request import urlopen


engine= pyttsx3.init()
wolframalpha_app_id="7A8TXX-H59JRJPVYQ"



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time =datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour time -H #for 12 hours use I
    speak('the current time is ' + Time)
def date():
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    date= datetime.datetime.now().day
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)
def wishme():
    speak("Thanks for waking up me...")
    #greetings
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir...")
    elif hour>=12 and hour<18:
        speak("good afternoon sir...")
    elif hour>=18 and hour<24:
        speak("good evening sir...")
    else:
        speak("good night sir...")
    speak("i am CMR EC voice assistant. please tell me how can i help you...")
def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=0) as source: #(device_index = 0 or 1 0r 2.....)
        print("Listening...")
        r.pause_threshold= 1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language="en-US")
        print (query)
    except Exception as e:
        print("e")
        print("say that again please...")
        return "none"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    #for this function you must enable low security in your gmail which which you are going to use as sender
    server.login("188r1a04f2@gmail.com","1630105470")
    server.sendmail("188r1a04f2@gmail.com",to,content)
    server.close()
def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)
    battery= psutil.sensors_battery()
    speak('battery is at')
    speak(battery)
def joke():
    speak(pyjokes.get_joke())
def screenshot():
    img= pyautogui.screenshot()
    img.save('C:\\Users\\karthik\\OneDrive\\Pictures\\Screenshots\\img.png')
    speak("captured screen shot")


def taskexecution():
    wishme()
    while True:
        query= TakeCommand().lower()
        # all commands will be stored in lower case in query
        #for easy recognisation 
        if "wikipedia" in query:
            speak("searching")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak('accrording to wikipedia')
            print(result)
            speak(result)
        elif "offline" in query:
            speak('going offline..., thanks for using me.')
            quit()
        elif "send mail" in query:
            try:
                speak("what should i say?")
                content =TakeCommand()
                #provide reciever email
                speak("who is the reciever")
                reciever=input("enter Receiver's Email :")
                #reciever="nagakarthik13122000@gmail.com"
                to= reciever
                sendEmail(to,content)
                speak(content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("unable to send email")
        elif "search" in query:
            speak('what should i search')
            chromepath =r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            #chrome locatation
            search = TakeCommand().lower()
            wb.register('chrome', None, wb.BackgroundBrowser(chromepath))
            wb.get('chrome').open_new_tab(search+'.com')  #open web sites end with .com
        elif "open youtube" in query:
            speak('what should i search')
            searchterm = TakeCommand().lower()
            speak("here we go to youtube")
            wb.open("https://www.youtube.com/results?search_query="+searchterm)
        elif "open google" in query:
            speak('what should i search')
            searchterm = TakeCommand().lower()
            speak("searching...")
            wb.open("https://www.google.com/search?q="+searchterm)
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            joke()
        elif "vlc"  in query:
            vlc=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player"
            os.startfile(vlc)
        elif "notepad"  in query:
            notepad=r"C:\Program Files\Notepad++\notepad++.exe"
            os.startfile(notepad)
        elif "command prompt"  in query:
            cmd=r"C:\Users\karthik\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt"
            os.startfile(cmd)
        elif "file explorer"  in query:
            file=r"C:\Users\karthik\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\File Explorer"
            os.startfile(file)
        elif "write note" in query:
            speak("what should i write sir...")
            notes= TakeCommand()
            file=open("notes.txt","w")
            speak('sir should i include date and time?')
            ans=TakeCommand().lower()
            if "yes" in ans or "sure" in ans:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak('Done taking notes , sir!')
            else:
                file.write(notes)
                speak('Done taking notes , sir!')
        elif 'show note' in query:
            speak("showing notes")
            file =open("notes.txt",'r')
            print(file.read())
            speak(file.read())
        elif "screenshot" in query:
            screenshot()
        elif 'play music' in query:
            songs_dir ="C:\\Users\\karthik\\Music"
            music=os.listdir(songs_dir)
            print(len(music))
            print(music)
            speak('which i want to play')
            ans= TakeCommand().lower()
            while("number" not in ans and "random" not in ans):
                speak("i couldn't understand you. please type the number...")
                ans=input("enter the song number... \nex:number 1 : ").lower()
            if "number" in ans:
                num =int (ans.replace('number',""))
            elif "random" in ans:
                num=random.randint(1,len(music)-1)
            os.startfile(os.path.join(songs_dir,music[num]))
        elif 'play movies' in query:
            movies_dir ="C:\\Users\\karthik\\Videos"
            movie=os.listdir(movies_dir)
            print(movie)
            speak('which i want to play')
            speak("please enter the movie number")
            ans= input("enter the movie number... \nex:number 1 : ")
            num =int (ans.replace('number',""))
            os.startfile(os.path.join(movies_dir,movie[num]))
        elif 'remember it' in query:
            speak("what should i remmber?")
            memory =TakeCommand()
            speak("you asked me to remember that "+memory)
            remember=open("memory.txt","w")
            remember.write(memory)
            remember.close()
        elif "do you remember anything" in query:
            remember=open("memory.txt","r")
            speak("you asked me to remember that "+remember.read())
        elif "entertainment news" in query:
            try:
                jsonobj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=176a0c1fd76b4168ac04158e84f0c779")
                data=json.load(jsonobj)
                i=1

                speak("here are top headlines from entertainment indusrty")
                print("*******TOP HEADLINES********")
                for item in data["articles"]:
                    print(str(i)+". "+item["title"]+"\n")
                    print(str(item["description"])+"\n")
                    speak(item["title"])
                    i += 1

            except Exception as e:
                print(str(e))
        elif "sports news" in query:
            try:
                jsonobj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=176a0c1fd76b4168ac04158e84f0c779")
                data=json.load(jsonobj)
                i=1

                speak("here are top headlines from sports")
                print("*******TOP HEADLINES********")
                for item in data["articles"]:
                    print(str(i)+". "+item["title"]+"\n")
                    print(str(item["description"])+"\n")
                    speak(item["title"])
                    i += 1

            except Exception as e:
                print(str(e))
        elif "business news" in query:
            try:
                jsonobj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=176a0c1fd76b4168ac04158e84f0c779")
                data=json.load(jsonobj)
                i=1

                speak("here are top headlines from bussiness indusrty")
                print("*******TOP HEADLINES********")
                for item in data["articles"]:
                    print(str(i)+". "+item["title"]+"\n")
                    print(str(item["description"])+"\n")
                    speak(item["title"])
                    i += 1

            except Exception as e:
                print(str(e))
        elif 'where is' in query:
            query = query.replace('where is',"")
            location= query
            speak('user asked to locate'+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
        elif "calculate" in query:
            
            app_id = "7A8TXX-H59JRJPVYQ"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("7A8TXX-H59JRJPVYQ")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)
        elif "log out" in query:
            os.system("shutdown -l")
        elif "restart" in query:
            speak("system is going to restart")
            os.system("shutdown /r /t 1")
        elif "shutdown" in query:
            speak("system is going to shudown")
            os.system("shutdown /s /t 30")
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif "record video" in query or "webcam" in query:
            cap = cv2.VideoCapture(0)

            # Check if the webcam is opened correctly
            if not cap.isOpened():
                raise IOError("Cannot open webcam")

            while True:
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
                cv2.imshow('Input', frame)

                c = cv2.waitKey(1)
                if c & 0xFF ==ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()
#image processing functions
        elif "image processing" in query:
            speak("i know some image processing techniques please select from below")
            ans=input("Here some the img prossessing functions i can do:\n 1.blur\n 2.gray scale\n 3.smoothing\n 4.collage\n 5.invert\n 6.sketch\n 7.edge detection\nplease select any one number: ")
            if "1" in ans:
                img = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg') 
    
                # make sure that you have saved it in the same folder
                # You can change the kernel size as you want
                blurImg = cv2.blur(img,(10,10)) 
                cv2.imshow('blurred image',blurImg)
                
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif "2" in ans:
                image = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg')
                cv2.waitKey(0)
                
                # Use the cvtColor() function to grayscale the image
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                
                cv2.imshow('Grayscale', gray_image)
                cv2.waitKey(0) 
                
                # Window shown waits for any key pressing event
                cv2.destroyAllWindows()
            elif "3" in ans:
                src = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg', cv2.IMREAD_UNCHANGED)
                dst = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)

                cv2.imshow("Gaussian Smoothing",np.hstack((src, dst)))
                cv2.waitKey(0) 
                cv2.destroyAllWindows()
            elif "4" in ans:
                image1 = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg')
                image2 = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg')
                cv2.imshow("collage",np.hstack((image1,image2)))
                cv2.waitKey(0) 
                cv2.destroyAllWindows()
            elif "5" in ans:
                image_grey = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg',cv2.IMREAD_GRAYSCALE)
                tresh=128
                imagebinary= cv2.threshold(image_grey,tresh,255,cv2.THRESH_BINARY)[1]
                cv2.imshow("invert",imagebinary)
                cv2.waitKey(0) 
                cv2.destroyAllWindows()
            elif "6" in ans:
                img = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg')
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                gray=cv2.medianBlur(gray,5)
                edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

                color =cv2.bilateralFilter(img,9,250,250)
                cartoon=cv2.bitwise_and(color,color,mask=edges)

                cv2.imshow("sketch",edges)
                cv2.waitKey(0) 
                cv2.destroyAllWindows()

            elif "7" in ans:
                img = cv2.imread('C:\\Users\\karthik\\vs python\\cat.jpg')
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                gray=cv2.medianBlur(gray,5)
                edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

                color =cv2.bilateralFilter(img,9,250,250)
                cartoon=cv2.bitwise_and(color,color,mask=edges)

                cv2.imshow("edge detection",cartoon)
                cv2.waitKey(0) 
                cv2.destroyAllWindows()
#here on words college facilities
        elif "college fee" in query or "hostel fee" in query or "transport fee" in query   :
            speak("you can pay fee here")
            wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/StudentRegularFeeCollection.aspx")
        elif "bonafide certificate" in query or "study certificate" in query or "it returns certificate" in query or "clearance certificate" in query:
            speak("you can apply certificates here")
            wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/StudentApplyCertificates.aspx")
        elif "my attendance" in query:
            speak("you can check your attendance here")
            wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/StudentOverallAttendance.aspx")
        elif "exam fee" in query :
            print("REGULAR or SUPPLEMENTARY ")
            speak('You want to pay regular or supplementary')
            ans= TakeCommand().lower()
            while("regular" not in ans and "supplementary" not in ans and "supply" not in ans):
                speak("i couldn't understand you. please reapeat...")
                ans= TakeCommand().lower()
            if "regular" in ans:
                speak("you can pay regular exam fee here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/ExamFeePaymentReg.aspx")
            elif "supplementary" in ans or "supply" in ans:
                speak("you can pay supplementary exam fee here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/ExamFeePaymentSupply.aspx")
        elif "exam time table" in query :
            print("INTERNAL or EXTERNAL ")
            speak('Which time table you want internal or external')
            ans= TakeCommand().lower()
            while("internal" not in ans and "external" not in ans):
                speak("i couldn't understand you. please reapeat...")
                ans= TakeCommand().lower()
            if "internal" in ans:
                speak("your internal time table will available here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/InternalTimeTable.aspx")
            elif "external" in ans:
                speak("your external time table will available here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/ExternalTimeTable.aspx")
        elif "condonation fee" in query:
            speak("you can pay condonation fee here")
            wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/CondonationFeeCollectionStudent.aspx")
        elif "my marks" in query :
                speak("you can check your marks here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/overallMarks.aspx")
        elif "cgpa" in query or "sgpa" in query :
                speak("you can check your c g p a and s g p a here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/OverallResultStudent.aspx")
        elif "hall ticket download" in query or "download hall ticket" in query :
                speak("you can download your hallticket here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/StudentHallTicketDownload.aspx")       
        elif "placements" in query :
                speak("you can check upcoming placement drives here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/PlacementAnnouncementsDisplay.aspx")
        elif "my mentor" in query or "my class teacher" in query :
                speak("you can check your mentor details here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/SessionDetails.aspx")
        elif "feedback" in query:
                speak("you can give feedback to your faculty here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/Student/StudentFeedBackForEmployee.aspx")
        elif "class time table" in query or "my class" in query or "my section" in query :
                speak("you can check your section or class details here")
                wb.open("https://cmrecerp.com/BeesERP/StudentLogin/MainStud.aspx")
#date and time
        elif "time" in query: #tell us time when asked
            time()
        elif "date" in query: #tell us date when asked
            date()


if __name__ == "__main__":
    while True:
        permission=TakeCommand()
        if "wake up" in permission:
            taskexecution()
        elif "goodbye" in permission:
            speak("thanks for using me sir , have a good day")
            sys.exit()


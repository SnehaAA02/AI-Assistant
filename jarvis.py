from ast import main
import datetime
from logging import exception
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

engine =pyttsx3.init("sapi5")
voices =engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def WishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("good morning")
   elif hour>=12 and hour<18:
      speak("good afternoon")
   else:
      speak("good evening")




speak("I am Otto. How may I help you!")

def takeCommand():
  # 

   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening..")
      r.pause_threshold=1
      audio=r.listen(source)

      try:
         print("Recognizing..")
         query=r.recognize_google(audio,language='en.in')
         print(f'User said:{query}\n')

      except Exception as ex:
         print("Say that again please")
         return "None"
      return query
   
if __name__ == "__main__":
   WishMe()
   #speak("Sneha is strong")
   while True:
      query=takeCommand().lower()
      if 'wikipedia' in query:
         speak('Searching wikipedia..')
         query=query.replace("wikipedia", "")
         results=wikipedia.summary(query,sentences=2)
         speak("According to wikipedia") 
         print(results) 
         speak(results)

      elif 'open youtube' in query:
         webbrowser.open('youtube.com')

      elif 'open google' in query:
         webbrowser.open('google.com')

      elif 'play music' in query:
          music_dir='D:\\songs'
          songs=os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[0]))

         
      elif 'time' in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"{strTime}")

      elif 'send a message' in query:
         pywhatkit.sendwhatmsg("+918971171310","Hi  ",18,00)

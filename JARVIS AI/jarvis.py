import speech_recognition as sr
import speech_recognition as r
import pyautogui
import wikipedia
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<=12:
          speak("Good Morning")

     elif hour>=12 and hour<18:
          speak("Good Afternoon")  

     else:
         speak("Good Evening")  

         speak("I am Jarvis Mam. Please tell me how may I help you")

if __name__ =="__main__":
     speak("Arpita is a good girl")
     wishMe()

def handle_command(command):
     if "open" in command:
          pyautogui.press('win')   
          pyautogui.typewrite(command.replace("open", ""))
          pyautogui.press('enter')
     elif "search"  in command:
          result = wikipedia.summary(command.replace("search", ""),sentences=2)
          engine.say(result)
          engine.runAndWait()
     elif "send email"  in command:
          pass
     else:
          engine.say("I didn't understand that command.")  
          engine.runAndWait()

     import webbrowser
     import speech_recognition as sr 

     def listen():
          r= sr.Recognizer()
          with sr.Microphone()as source:
               print("Listening...")
               audio= r.listen(source)
          try: 
               query = r.recognize_google(audio, language='en-IN')
               return query
          except sr.UnknownValueError:
               print("Could not understand audio")
               return None
          except sr.RequestError:
               print("Request error")
               return None
          
     def open_google(query):
          url ="(link unavailable)" + query
          webbrowser.open(url)

     def open_wikipedia(query):
          url ="(link unavailable)" + query
          webbrowser.open(url)  


          query =listen()
          if query:
               if"Google" in query:
                    open_google(query.replace("Google", ""))
               elif"Wikipedia" in query:
                    open_wikipedia(query.replace("Wikipedia", ""))    
            

   
     
               


     

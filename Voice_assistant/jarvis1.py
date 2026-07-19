# pyttsx3 ek Text-to-Speech library hai. Iski help se computer text ko bol sakta hai.
# Example: "Hello Anshu" -> Speaker se voice me sunai dega.
import pyttsx3
# speech_recognition library speech ko text me convert karti hai.
import speech_recognition as sr

# Browser open karne ke liye.
# Example: webbrowser.open("https://google.com")
import webbrowser

# Current Date aur Time nikalne ke liye.
import datetime

# Random jokes generate karne ke liye.
import pyjokes
import os
import time

# ---------------------------------------------------
# Is function ka kaam hai:
# User ki voice sunna
# aur usse text me convert karna.
# ---------------------------------------------------
def sptext():

    # Recognizer object create kar rahe hain. Ye object speech ko process karega.Iske andar bahut methods hote hain:
    # listen() , recognize_google() , adjust_for_ambient_noise()
    recognizer = sr.Recognizer()

    # Microphone ko open kar rahe hain.
    # "with" ka use resource management ke liye hota hai. Matlab -Start me microphone ON -Kaam khatam - Automatically microphone OFF -Hume manually close nahi karna padta.
    with sr.Microphone() as source:
        # Screen pe message print hoga.
        print("bolo....")
        # Bahar ka noise measure karta hai.
        # Example: Fan chal raha hai ,AC chal raha hai , Keyboard ki awaaz aa rahi hai. Ye un sabko background noise maan leta hai. ,Fir sirf tumhari voice pe focus karta hai.
        recognizer.adjust_for_ambient_noise(source)
        # Ab microphone se audio record karo.
        # User jab bolega , uski voice "audio" variable me store ho jayegi. Ye text nahi hai ,Ye AudioData object hai.
        audio = recognizer.listen(source)

        try:
            print("sun rha hu...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        
        except sr.UnknownValueError :
            print("samajh nhi aa rha")
            return""

        except Exception as e:
            print(e)
            return ""

# Is function ka kaam hai:
# Jo bhi text is function ko diya jayega,
# us text ko computer apni voice me bol dega.
def tex_speech(x):
    # Ye speech engine create karta hai.
    # Is object ke through hum:Voice change kar sakte hain , Speed change kar sakte hain ,Volume change kar sakte hain ,Text ko speech me convert kar sakte hain.
    engine = pyttsx3.init()

    # Computer me jitni bhi voices installed hain,unki list le rahe hain.
    # voices[0] -> Male Voice
    # voices[1] -> Female Voice
    voices = engine.getProperty('voices')

    # Voice select kar rahe hain, .id har voice ka unique identifier hota hai.
    engine.setProperty('voice' , voices[1].id)

    # Is variable "rate" ka baad me use nahi hua.Ye line optional hai. Ye basically current speed rate nikalta h system ka default rate
    rate = engine.getProperty('rate')

     # Speaking speed set kar rahe hain.
    engine.setProperty('rate' , 130)

    # Jo text function me aaya hai us text ko speech queue me add kar do.
    # Abhi sirf queue me add hua hai. Abhi speaker se kuch nahi nikla.
    engine.say(x)
    
     # Queue me jitni bhi speech hai usko execute karo.
    # Agar ye line nahi likhenge to engine.say() kuch bhi nahi bolega. Ye function tab tak wait karta hai jab tak poori speech complete nahi ho jati.
    engine.runAndWait()

# tex_speech("hello ,i welcome you, lets have a cup of coffee")

if __name__ == '__main__':
    
    if("hey peter" in sptext().lower()):

        while True:
                data1 = sptext().lower()

                if("name" in data1):
                    name1 = "my name is peter"
                    tex_speech(name1)

                elif("old are you" in data1):
                    age = "I am 13 years old"
                    tex_speech(age)

                elif("time" in data1):
                    time2 = datetime.datetime.now().strftime("%I%M%p")
                    tex_speech(time2)

                elif("youtube" in data1):
                    webbrowser.open("https://www.youtube.com/watch?v=awYJWalvK_0")

                elif("joke" in data1):
                    joke1 = pyjokes.get_joke(language="en" , category="neutral")
                    print(joke1)
                    tex_speech(joke1) 
                    
                elif "exit" in data1 :
                    tex_speech("Thank you")
                    break

                time.sleep(5)
        
    else:
        print("Thanks")





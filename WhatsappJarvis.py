import speech_recognition as sr
import w
import pyttsx3

r = sr.Recognizer()

def voiceInput():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text
def bot():      
    try:
        speaker = pyttsx3.init()
        voices = speaker.getProperty("voices")
        speaker.setProperty("voice",voices[1].id)  
        speaker.say("Hello ,Shlok how may I help you")
        speaker.runAndWait()
        print("Listening")
        text = voiceInput().lower()
        if text == 'open whatsapp':
            w.openWhatsapp()
        elif "open " in text:
            name = text.replace("open",'')
            name = name.strip()
            w.openChat(name)
        elif "message" in text:
            message = text.replace("message","")
            w.sendMsg(message)
        elif "call to" in text:
            name = text.replace("call to",'')
            name = name.strip()
            w.call(name)
        elif "video to" in text:
            name = text.replace("video to",'')
            name = name.strip()
            w.videoCall(name)
        elif "close whatsapp" in text:
            w.closeWhatsapp()
            print("I shall take my leave")
            
        else:
            print("Command is not recognized")
            
        print("It's done sir")
            
    except:
        print("Sorry, I could not understand your voice input.")

bot()

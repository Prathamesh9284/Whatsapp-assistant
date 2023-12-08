# import speech_recognition
# import pywhatkit as wa
# import pyttsx3
# from datetime import datetime

# speaker = pyttsx3.init()
# voices = speaker.getProperty("voices")
# speaker.setProperty("voice",voices[1].id)
# speaker.say("Hello ,Shlok how may I help you")
# speaker.runAndWait()

# listener = speech_recognition.Recognizer()
# def getSpeech():
#     try:
#         with speech_recognition.Microphone() as source:
#             listener.adjust_for_ambient_noise(source,duration=0.5)
#             print("Listening...")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             print(command)
#             return command
#     except:
#         print("No command")
#         return None
    
# phone_no_dict = {"sumit":"+919373197797","susmit":"+918767617811"} 
# def getNum(phone_no_dict,command):
#     for i in phone_no_dict.keys():
#         if i == command:
#             no = phone_no_dict[i]
#             return no
#     return None

# command = getSpeech()
# if 'send message to' in command:
#         name = command.replace("send message to",'')
#         no = getNum(phone_no_dict,name)
#         speaker.say("what would you like to send")
#         speaker.runAndWait()
#         name = name.strip()
        
#         message = getSpeech()
#         speaker.say("message has been sent to "+name)
#         speaker.runAndWait()
#         now = datetime.now()
#         hour = int(now.strftime("%H"))
#         min = int(now.strftime("%M"))
#         wa.sendwhatmsg_instantly(no,message,10)

import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as source
with sr.Microphone() as source:
    print("Say something...")
    # adjust the recognizer's sensitivity threshold to ambient noise
    r.adjust_for_ambient_noise(source)
    # listen for the user's voice input
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # convert voice input into text
    text = r.recognize_google(audio)
    print("You said: ", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand your voice input.")
except sr.RequestError:
    print("Sorry, my speech recognizer service is currently down.")

import speech_recognition as sr

recording = sr.Recognizer()
with sr.Microphone() as source: 
    recording.adjust_for_ambient_noise(source)
    print("Listening... ")
    audio = recording.listen(source)
    global wasSaid

#english en-in, en-us
#mandarin zh

try: 
    wasSaid = recording.recognize_google(audio, language='en-in')
    print("You said: \n",wasSaid)
except Exception as e:
    print(e)
words = str(wasSaid).split(' ')
#print("this is the list: ",words)

if(words.__contains__("weather")):
    print("you need help its alr cold...duh")
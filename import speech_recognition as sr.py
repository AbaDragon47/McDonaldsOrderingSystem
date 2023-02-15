import speech_recognition as sr
from numpy import loadtxt
import tensorflow as tf
from keras.models import Sequential
#CALVIN  FUNNNNNNN
def speakerListener():
    recording = sr.Recognizer()
    with sr.Microphone() as source: 
        recording.adjust_for_ambient_noise(source)
        print("Listening... ")
        audio = recording.listen(source)
        global wasSaid
    ####################################################################
    #random stuff DO NOT ignoge
    #n is 5... but remember 3n is 7                <==      *IMPORTSNT*
    #english en-in, en-us
    #mandarin zh
    #wo de ming zi shi fun wen bing ==> My name is Fun Wen-Bing (Calvin)
    #####################################################################
    try: 
        wasSaid = recording.recognize_google(audio, language='en-in')
        print("You said: \n",wasSaid)
    except Exception as e:
        print(e)
    words = str(wasSaid).split(' ')
    #print("this is the list: ",words)

speakerListener()




if(words.__contains__("weather")):
    print("you need help its alr cold...duh")
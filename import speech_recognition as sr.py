from gtts import gTTS
import os

import speech_recognition as sr
from numpy import loadtxt
import tensorflow as tf
from keras.models import Sequential
from pandas import read_excel
#CALVIN  FUNNNNNNN
def speakerListener():
    recording = sr.Recognizer()
    with sr.Microphone() as source: 
        recording.adjust_for_ambient_noise(source)
        print("Listening... ")
        audio = recording.listen(source)
        print("Recognizing... ")
        global wasSaid, words
    ####################################################################
    #random stuff DO NOT ignoge
    #n is 5... but remember 3n is 7                <==      *IMPORTSNT*
    #english en-in, en-us
    #mandarin zh
    
    #WWOH DUH MING ZSOU SU FUN WHEN BIENG 
    #wo de ming zi shi fun wen bing ==> My name is Fun Wen-Bing (Calvin)
    #####################################################################
    try: 
        saying = recording.recognize_google(audio, language='en-in')
        wasSaid= (str)(saying)
        wasSaid= wasSaid.title()
        return wasSaid
        #print("You said: ",wasSaid)
    except Exception as e:
        print(e)
    #words = str(wasSaid).split(' ')
    #print("this is the list: ",words)
    
speakerListener()

#Dict is a 'Map' in python

#need to make a method  that take everything in spreadsheet, put it into dict
# then can take what was said in listening() and figure out what person wants

senStemsWTags= dict()
qSheet= "questions"
file_name= 'D:\github stuff\Robacal\menu.xlsx'
df= read_excel(file_name,sheet_name= qSheet)

#heheeheh... this works lmao
for i in range(0, len(df)):
    sen=(str)(df.iloc[i][0])
    senStemsWTags.update({sen.title():df.iloc[i][1:].values.tolist()})
# dictionary of stems and tags
#print(senStemsWTags.items())


#method checks to see if sen stems are in what customer says
tags= []
def match(words):
   # print("running")
    keys=[]
    count=0
    for key in senStemsWTags.keys():
        count+=1
        actual=key.split(" (")[0]
        actual=actual.split("With")[0]
        if actual in words:
            tags.extend(senStemsWTags[key])
            keys.append(key)

    for item in tags:
        if isinstance(item,float):
            tags.remove(item)
    if len(keys)>0:
        tags.append("Items ==> ")
    tags.extend(keys)

    if len(tags)==0:
        return "customer doesnt want to order"
    else:
        return tags 

print(match(wasSaid.title()))


#clarification method to get specfic tags
copy=wasSaid.title()
def clarify(list):
    #re.split(r'#|#',(str))
    newList=[]
    regList=[]
    for value in list[list.index("Items ==> ")+1:]:
        newList.append(value.replace("With"," (").split(" (")[0])
        regList.extend(value.replace("With"," (").replace(")"," (").split(" (")[1:])
    for item in newList:
        if newList.count(item)>1:
            print("")
    return regList

#should return the clarifying tags
print(clarify(tags))




#buying method if order
#def matchTags():
 #   if(match(wasSaid)=="customer doesnt want to order"):




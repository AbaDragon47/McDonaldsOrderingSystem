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
    
#speakerListener()
wasSaid="I Want A Big Mac A Vanilla Shake A Dr Pepper A McRib A McDouble A Sausage McGriddles And A Cheeseburger"
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
            print("")
    #print("the entire dictionary: ",senStemsWTags)        
    #print("tags in first method: ",tags)
    print("keys in first method: ",keys)

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

#remember dictionary put items in order as they appear in menu
#clarification method to get specfic tags
copy=wasSaid.title()
regList=[]
def clarify(list):
    returning=[]
    #re.split(r'#|#',(str))
    newList=[]
    
    for value in list[list.index("Items ==> ")+1:]:
        newList.append(value.replace("With"," (").split(" (")[0])
        regList.extend(value.replace("With"," (").replace(")"," (").split(" (")[1:-1])
        #print ("regList: ",regList)
        
 
    print("newList: ",newList)#in order as it is in the dict
    print("reg: ",regList)
    #how to check which key based on tags vvv
    needToCheck=[]
    #whatTosay="Could you clarify what you want pls "
    whatTosay=""
    for item in newList:
        if newList.count(item)>1:
            needToCheck.append(item)
    i=0
    for value in list[list.index("Items ==> ")+1:]:
        if value.replace("With"," (").split(" (")[0] == needToCheck[0]:
            whatTosay+=("\n")+regList[i]
            a=needToCheck.count(needToCheck[0])
            needToCheck.remove(needToCheck[0])
            i+=1
            if a<2 or len(needToCheck)==0:
                i=0
                print("Could you clarify what you want pls ",whatTosay)
                ans=whatTosay.split()
                sec=speakerListener().split()
                final=listContains(ans,sec)
                #returning.append(list.index(value.replace("With"," (").split(" (")[0])+regList.index(final))
                for item in list[list.index("Items ==> ")+1:]:
                    if item.replace("With"," (").replace(")"," (").split(" (")[0]!=value.replace("With"," (").replace(")"," (").split(" (")[0]:
                        returning.append(item)
                    else:
                        print("Final: ",final.split())
                        print("clarification identifiers: ",item.replace("With"," (").replace(")"," (").split(" ("))
                        if final in item.replace("With"," (").replace(")"," (").split(" ("):
                            print("yes!  ",item)
                            returning.append(item)
            
                print("\nValue: ",value.replace("With"," (").split(" (")[0])
                print("\nfinal: ",final)
                print("\nreturning: ",returning)
                #ok it works but it just returns the other stuff too when the program runs
                #AWESOME JOB ABAAAAAAAAAAA!
            
   # for i in range(len(needToCheck))-1:
    #    a=needToCheck.count(needToCheck[i])
     #   if needToCheck.count(needToCheck[i]>1):
      #      whatTosay+="\n",regList[i]


    return returning

def listContains(list1,list2):
    for m in list1:
        for n in list2:
            if m==n:
                return m
#should return the clarifying tags
print("reglist: ",regList)
print(clarify(tags))




#buying method if order
#def matchTags():
 #   if(match(wasSaid)=="customer doesnt want to order"):




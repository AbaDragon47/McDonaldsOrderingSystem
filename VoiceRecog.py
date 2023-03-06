from gtts import gTTS
import os
import mcData as mD
import speech_recognition as sr
from numpy import loadtxt
import tensorflow as tf
from keras.models import Sequential
from pandas import read_excel

from gtts import gTTS 
import os
cart = []
total = 0

#grab specfic item user wants to order and adds it to cart(array of food items)
def order(item):
    cart.extend(item)
    total = total + mD.getPrice(item) #adding up price of order
    speaking="Your item was added!\nWould you like to order anything else (y/n)?"
    
    speech=gTTS(text=speaking, lang= 'en',slow=False)
    speech.save("speaking.mp3")
    os.system("start speaking.mp3")
    print(speaking)
    answ = speakerListener()

    if(answ.contains("Y")):
        print("What would you like to order?")
        answ = speakerListener() #speakers reponse
        tags = match(answ) #returns list of key words in response
        listItems = clarify(tags) #figures out what items it wants to order from key words, returns a list
        if listItems.len > 0:
            massOrder(listItems)
        order(listItems[0])
    #after finishing ordering, calls methods for paying
    else:
        print("You've finished ordering!\nYour total is: " + total)
        remaining = mD.getCardAmount() - total
        print("Your bank account balance is: " + remaining)
        print("Your food will be delivered in 15 min\nP.S ice cream machine still broken..." )

        
#method when ordering more than 1 item at a time
def massOrder(listItems):
    numberOfItems = listItems.len
    for i in range(numberOfItems):
        mItem = listItems[i]
        if i == numberOfItems-1:
            order(mItem)
        cart.append(mItem)
        total = total + getPrice(mItem)  
  
# Using the special variable 
# __name__

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
#wasSaid="I Want A Big Mac A Vanilla Shake A Dr Pepper A McRib A McDouble A Sausage McGriddles And A Cheeseburger"
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
    #print("keys in first method: ",keys)

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

#print(match(speakerListener().title()))

#remember dictionary put items in order as they appear in menu
#clarification method to get specfic tags
#copy=wasSaid.title()

def clarify(list):
    returning=[]
    #re.split(r'#|#',(str))
    newList=[]
    regList=[]
    for value in list[list.index("Items ==> ")+1:]:
        newList.append(value.replace("With"," (").split(" (")[0])
        regList.extend(value.replace("With"," (").replace(")"," (").split(" (")[1:-1])
        #print ("regList: ",regList)
        
 
   # print("newList: ",newList)#in order as it is in the dict
    #print("reg: ",regList)
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
                #checks and see what off the clarfiy that user said
                final=[listContains(ans,sec), value.replace("With"," (").replace(")"," (").split(" (")[0]]
                #final=["Large","Dr Pepper"]
                for item in list[list.index("Items ==> ")+1:]:
                    #for every item
                    if item.replace("With"," (").replace(")"," (").split(" (")[0]!=value.replace("With"," (").replace(")"," (").split(" (")[0]:
                        #if item is not equal to value that needs to be clarified; and if it is not there is not multiple of it
                        if newList.count(item.replace("With"," (").replace(")"," (").split(" (")[0])<2:
                            returning.append(item)
                    else:
                        #print("Final: ",final)
                        #print("clarification identifiers: ",item.replace("With"," (").replace(")"," (").split(" ("))
                        if all(x in final for x in item.replace("With"," (").replace(")"," (").split(" (")[:-1]):
                            #print("yes!  ",item)
                            returning.append(item)
            
               # print("\nValue: ",value)
                #print("\nfinal: ",final)
                #print("\nreturning: ",returning)
                #ok it works but it just returns the other stuff too when the program runs
                #neverrrr mindddddddd we doneeeeeeeeeeee (technically but i never made the tags to keys method... this just keys to tags)
                #AWESOME JOB ABAAAAAAAAAAA!
            

    done=[]
    [done.append(x) for x in returning if x not in done]
    return done

def listContains(list1,list2):
    for m in list1:
        for n in list2:
            if m==n:
                return m
#should return the clarifying tags
#print("reglist: ",regList)
#print(clarify(tags))


# Defining main function
def main():
    speaking="Hello customer!\nWhat would you like to do today?"
    print(speaking)
    speech=gTTS(text=speaking, lang= 'en',slow=False)
    speech.save("speak.mp3")
    os.system("start speak.mp3")
    iWant=speakerListener().title()
    whatCustomerWants=match(iWant)
    if "order" in whatCustomerWants:
        speaking="Oh, then you would like to order? Lets see..."
        order(clarify(whatCustomerWants))

if __name__=="__main__":
    main()

#buying method if order
#def matchTags():
 #   if(match(wasSaid)=="customer doesnt want to order"):




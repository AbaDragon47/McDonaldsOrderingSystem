import VoiceRecog as vr
from gtts import gTTS 
import os
cart = []
total = 0

# Defining main function
def main():
    speaking="Hello customer!\nWhat would you like to do today?"
    print(speaking)
    speech=gTTS(text=speaking, lang= 'en',slow=False)
    speech.save("speaking.mp3")
    os.system("start speaking.mp3")
#grab specfic item user wants to order and adds it to cart(array of food items)
def order(item):
    cart.append(item)
    total = total + getPrice(item) #adding up price of order
    speaking="Your item was added!\nWould you like to order anything else (y/n)?"
    print(speaking)
    speech=gTTS(text=speaking, lang= 'en',slow=False)
    speech.save("speaking.mp3")
    os.system("start speaking.mp3")
    answ = vr.speakerListener()

    if(answ.contains("y")):
        print("What would you like to order?")
        answ = vr.speakerListener() #speakers reponse
        tags = vr.match(answ) #returns list of key words in response
        listItems = vr.clarify(tags) #figures out what items it wants to order from key words, returns a list
        if listItems.len > 0:
            massOrder(listItems)
        order(listItems[0])
    #after finishing ordering, calls methods for paying
    else:
        print("You've finished ordering!\nYour total is: " + total)
        remaining = getCardAmount() - total
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
if __name__=="__main__":
    main()
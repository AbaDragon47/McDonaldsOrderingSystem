#Rocio's login reading class
import csv
import pandas as pd
 
logArr =[]
allLogin = []
numberLogins = 0
loginInfo = []
df = pd.read_csv('login.csv')

# reading the CSV file
with open('login.csv') as login:
    log = csv.reader(login) #array of array
    loginInfo = next(login).split(",")#delimeter for commas
    #adding rows of each menu item (with nutritional info) to menu array
    for row in log: 
        logArr.append(row)
        numberLogins += 1
    allLogin = logArr.pop(0)

#all information available from database(calories, sat fats, sodium, carbs, sugar)
def logInfo():
    return loginInfo

def allLogins():
    logArr.clear()
    with open('login.csv') as login:
        log = csv.reader(login) #array of array
        for row in log: 
            logArr.append(row)
        logArr.pop(0)
        allLogin = logArr
    return allLogin

def addLogin(un, pw):
    if(findUserIndex(un) != -1):
        print("Username already in system")
    else:
        df.loc[numberLogins + 1,'Username'] = un
        df.loc[numberLogins + 1,'Password'] = pw
        df.to_csv("login.csv", index=False)

def userArrLen(un):
    repopulate()
    num = 0
    userArr = []
    for login in logArr:
        if(login[0] == un):
            userArr = login
    item = userArr[0]
    while item != "":
        num += 1
        item = userArr[num]
    return num

def addPrefrence(un, cart):
    i = userArrLen(un) - 2
    if i < 0:
        i = 0
    print(i)
    for pref in cart:
        df.loc[findUserIndex(un)-1,"pref" + str(i)] = pref
        i += 1
    df.to_csv("login.csv", index=False)

def repopulate():
    logArr.clear()
    numberLogins = 0
    with open('login.csv') as login:
        log = csv.reader(login) #array of array
        for row in log: 
            logArr.append(row)
            numberLogins += 1

def findUserIndex(un):
    index = 0
    repopulate()
    for user in logArr:
        if(user[0] == un):
            return index
        index += 1
    return -1

print("\n")
addLogin("RocioS", "easyPass")
addPrefrence("firstTest", ["McFry"])
addPrefrence("RocioS", ["pepsi"])
addPrefrence("RocioS", ["McShake"])
addPrefrence("firstTest", ["McBurger"])

print(allLogins())
            

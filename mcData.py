#Rocio's API reading class
import pandas
import csv
 
menu =[]
# reading the CSV file
with open('menu.csv') as menuData:
    m = csv.reader(menuData) 
    dataInf = next(menuData)
    #adding rows of each menu item (with nutritional info) to menu array
    for row in m: 
        menu.append(row)
 
def dataInfo():
    return dataInf

def allData():
    return menu
 
#get category of menu item
#copy method and change index in return portion to fit certain info needed

#gets catgeory of item: breakfast, beef & pork, chicken & fish, salads snacks and sides
#desserts, beverages, coffee and tea, smoothies and shakes
def getCategory(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][0]
        indexItem = indexItem + 1
#gets serving size of item in oz and g
def getServingSize(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][2]
        indexItem = indexItem + 1
#gets calories of item
def getCalories(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][3]
        indexItem = indexItem + 1
#gets calories from fat of item
def getFatCalories(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][4]
        indexItem = indexItem + 1
#gets total fat of item
def getTotalFat(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][5]
        indexItem = indexItem + 1
#gets percentage that the fat contained in item is of the daily percentage
def getFatDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][6]
        indexItem = indexItem + 1
#gets saturated fat of item
def getSatFat(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][7]
        indexItem = indexItem + 1
#gets percentage that the saturated fat contained in item is of the daily percentage
def getSatFatDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][8]
        indexItem = indexItem + 1
#gets trans fat of item
def getTransFat(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][9]
        indexItem = indexItem + 1
#gets total cholesterol of item
def getCholesterol(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][10]
        indexItem = indexItem + 1
#gets percentage that the cholesterol contained in item is of the daily percentage
def getCholesterolDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][11]
        indexItem = indexItem + 1
#gets total sodium of item
def getSodium(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][12]
        indexItem = indexItem + 1
#gets percentage that the sodium contained in item is of the daily percentage
def getSodiumDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][13]
        indexItem = indexItem + 1
#gets total carbohydrate(carbs) of item
def getCarbs(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][14]
        indexItem = indexItem + 1
#gets percentage that the carbohydrates(carbs) contained in item is of the daily percentage
def getCarbsDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][15]
        indexItem = indexItem + 1
#gets total dietary fiber of item
def getDietaryFiber(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][16]
        indexItem = indexItem + 1
#gets percentage that the dietary fiber contained in item is of the daily percentage
def getDietaryFiberDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][17]
        indexItem = indexItem + 1
#gets total sugars of item
def getSugar(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][18]
        indexItem = indexItem + 1
#gets total Protein of item
def getProtein(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][19]
        indexItem = indexItem + 1
#gets total Vitamin A of item
def getVitaminA(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][20]
        indexItem = indexItem + 1
#gets total Vitamin C of item
def getVitaminC(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][21]
        indexItem = indexItem + 1
#gets percentage that the calcium contained in item is of the daily percentage
def getCalciumDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][22]
        indexItem = indexItem + 1
#gets percentage that the iron contained in item is of the daily percentage
def getIronDailyPerc(item):
    indexItem = 0
    for menuItem in menu:
        for name in menuItem:
            if(item == name):
                return menu[indexItem][23]
        indexItem = indexItem + 1

#checking
print(dataInfo())
#print(allData())
eggMc = "Egg McMuffin"
print("Item: "+ eggMc)
print("Category: " + getCategory(eggMc))
print("Serving Size: " + getServingSize(eggMc))
print("Calories: " + getCalories(eggMc))
print("FatCalories: " + getFatCalories(eggMc))
print("Total Fat: " + getTotalFat(eggMc))
print("Fat Daily Perc: " + getFatDailyPerc(eggMc))
print("Saturated Fats: " + getSatFat(eggMc))
print("Saturated Fat Daily Perc: " + getSatFatDailyPerc(eggMc))
print("Trans Fat: "+ getTransFat(eggMc))
print("Cholesterol: " + getCholesterol(eggMc))
print("Cholesterol Daily Perc: "+ getCholesterolDailyPerc(eggMc))
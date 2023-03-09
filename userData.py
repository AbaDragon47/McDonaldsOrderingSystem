import mcData as data
import numpy as np

#Creating a new class of the user information and data
class User:
    #Constructors
    def __init__(self, name : str, password : str, itemPreferences : list, previousOrders : set):
        self.name = name
        self.password = password
        self.itemPreferences, self.previousOrders = []

    #Methods
    def addOrder(self, list : list):
        self.previousOrders.__add__(list)
        



def main():
    p1 = User("Calvin", 1234567)
    print(p1.name)
    print(p1.password)
    order = [1, 2, 3, 4, 5]
    p1.addOrder(order)
    print(p1.previousOrders)


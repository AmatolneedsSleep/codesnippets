# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:16:27 2020

@author: wang_

"""

"""
Store
- Name
- Slogan
- Tax rate
- Customer Limit
- Open/Close Time

    - Item list
        - stock and price
    - Restock the items
    - Block items that are sold out
    
"""
class Store:
    def __init__(self, name, slogan, tRate, cLim, oT, cT):
        self.name = name
        self.slogan = slogan
        self.taxRate = tRate
        self.cLimit = cLim
        self.openTime = oT
        self.closeTime = cT
        self.items = {}
        
        print("Store:", self.name, "has been created. Please stock your shelves" +
              "using the stockUp() function.")
    
    def stockUp(self, sItems):
        self.items = sItems
        print(self.name, "has been fully stocked!")
        for item in self.items:
            cartItem = self.items[item]
            print("\t",cartItem["Name"], "-- Price:$", cartItem["Price"], "Stock:", cartItem["Stock"])
        
    def showStock(self):
        print("stock is seen below:")
        for item in self.items:
            cartItem = self.items[item]
            print("\t", item, ":",cartItem["Name"], "-- Price:$", cartItem["Price"], "Stock:", cartItem["Stock"])
    
    def getItem(self, index):
        if index in self.items:
            return self.items[index]
        else: 
            print("This item does not exist!")
            return {}
    
    def makePurchase(self, buyer, buyList):
        itemsBought = []
        for buyItem in buyList:
            currItem = self.getItem(buyItem)
            
            if buyer.money >= currItem["Price"]:
                if currItem["Stock"] >= 1:
                    self.items[buyItem]["Stock"] -= 1
                    buyer.money -= float(currItem["Price"])
                    itemsBought.append([currItem["Name"], currItem["Price"]])
                else:
                    print(currItem["Name"], "is out of stock! It will restock soon")
            else:
                print(buyer.name, "... You cannot afford this! finalizing Purchases.")
                break
        print("\n~~~~~~~~ PURCHASE MADE ~~~~~~~~") 
        for item in itemsBought:
            print(1, "\t", item[0], "   $", item[1])
        print("\n Thank you for shopping at", self.name, "!")
        print("\t", self.slogan)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        return buyer
        
   
"""
Shopper
- Name
- Money
"""
class Shopper:
    def __init__(self, name, money, store):
        self.name = name
        self.money = money
        self.store = store
        
    def purchase(self):
        buyItems = []
        choice = 0
        while not choice == -1:
            self.store.showStock()
            print(self.name,", You have:$", self.money)
            choice = input("Please enter item code of what would you like to buy (-1 to exit): ")
            
            if not int(choice) == -1:
                curItem = self.store.getItem(int(choice))
                print("BUYING:",curItem["Name"], "-- Price:$", curItem["Price"], "Stock:", curItem["Stock"])
                stockChoice = int(input("Please enter the quantity you would like to buy: "))
                
                if stockChoice <= curItem["Stock"] and not stockChoice == 0:
                    for count in range(stockChoice):
                        buyItems.append(int(choice))
                    print("PUCHASE VALID")
                elif stockChoice > curItem["Stock"]:
                    print("QUANTITY EXCEEDS CURRENT STOCK. PURCHASE FAILED.")
                else:
                    print("PURCHASE FAILED.")
            else:
                break
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    
        return buyItems
    

storeItems = {0:{"Name":"Shirt", "Price":15.99, "Stock":3}, 1:{"Name":"Laptop", "Price":299.99, "Stock":1},
              2:{"Name":"Mask", "Price":10.99, "Stock":3}, 3:{"Name":"Candy Bar", "Price":1.50, "Stock":7},
              4:{"Name": "Sanitizer", "Price":4.99, "Stock": 2}, 5:{"Name":"Apples", "Price":3.99, "Stock":3},
              6:{"Name":"tissues", "Price":1.99, "Stock":5}, 7:{"Name": "Soap Bar", "Price":5.99, "Stock": 4}}

myStore = Store("Shophere", "Quality Stuff, Shop here", 0.15, 3, "9:00 AM", "9:00 PM")
myStore.stockUp(storeItems)
myStore.showStock()

alex = Shopper("Alex", 200.50, myStore)
alexBag = alex.purchase()
myStore.makePurchase(alex, alexBag)
myStore.showStock()
from random import random


inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger': 1, 'arrow':12}
dragonLoot = {'gold coin': 3000, 'Axe of Booty Destruction': 1}

def displayInventory(inventory):
    print("Inventory")
    item_total = 0
    gold_total = inventory.get('gold coin', 0)
    for i, v in inventory.items(): #for every item and value in inventory.items
        print(str(v) + ' '+i)         # print the value as a string plus a empty string to add the items name
        if(i != "gold coin"):
            item_total += v             #add up the item total
    print("Total number of items: "+ str(item_total)) #print the total number of items with a space with how many items the loop has counted
    print("You have " + str(gold_total) + " gold")

def addToInventory(inventory, addedItems):
    for i, v in addedItems.items():
        print(str(v) + '' + i + 'added to Inventory.')
        inventory.setdefault(i,v)

addToInventory(inventory, dragonLoot)


displayInventory(inventory)


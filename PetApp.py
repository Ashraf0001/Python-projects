#Pet shop application
#Acts like a mini inventory
#Use what we have learned so far

"""
Imports
class
---add
---remove
---save
---load

Main
Test

"""


import json
import os.path

#Inventory Class

class Inventory:
    pets = {}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        q = 0
        if key in self.pets :
            v = self.pets[key]
            q = v + qty

        else:
            q = qty
        self.pets[key] = q
        print (f'Added {qty} {key}: total ={ self.pets[key]}')

    def remove(self, key, qty):
        q = 0
        if key in self.pets:
             v = self.pets[key]
             q = v - qty
        if q < 0:
            q = 0

        self.pets[key] = q
        print(f'Removed {qty} {key}: total = {self.pets[key]}')



    def display(self):
         for key, value in self.pets.items():
             print(f'{key} = {value}')




    def save(self):
        print('Saving Inventory')
        with open ('Inventory.txt', 'w') as f:
            json.dump(self.pets, f)

        print('saved!')



    def load(self):
        print("Load Inventory!")
        if not os.path.exists("Inventory.txt"):
            print( "Skipping, Nothing to load! ")
            return
        with open('Inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('Loaded')



def main():
     inv = Inventory()

     while True:

         action = input('Actions: add, remove, list , save, exit: ')
         if action == 'exit':
             break
         if action == 'add' or action == 'remove':
             key = input('Enter the key , I meant animal:')
             qty = int(input('Enter the qunatity'))
             if action == 'add':
                 inv.add(key, qty)
             if action == 'remove':
                 inv.remove(key, qty)
         if action == 'list':
             inv.display()

         if action == 'save':
             inv.save()

     inv.save()





if __name__ == '__main__':
     main()












# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:55:28 2021

@author: bbarber

Project Name: QWER Hacks
    
Project Description:
"""

#Library Imports (Delete as Needed)
import random



class newProfile:
    def __init__(self):
        #Input lists
        firstNames = ["Olivia","Emma","Ava","Sophia","Isabella","Charlotte","Amelia","Mia","Harper","Evelyn","Abigail","Emily","Ella","Elizabeth","Camila","Luna","Sofia","Avery","Mila","Aria","Scarlett","Penelope","Layla","Chloe","Victoria","Madison","Coilette","Arya","Sansa","Lyanna","Rose","Martha","Donna","Amy","Clara","Bill","Jaz"]
        lastInitials = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        cities = ["NYC", "LA", "San Fran", "Dallas", "Austin", "Boston", "Philly", "Annapolis"]
        
        self.age = max(round(random.normalvariate(24,5)),18) #Age 18 or older, ~N(24,5) 
        self.firstName = random.choice(firstNames)
        self.lastInitial = random.choice(lastInitials)
        self.bio = "Hi, I'm "+self.firstName+" "+self.lastInitial+"., I'm "+str(self.age)+", and I'm a recent transplant from "+random.choice(cities)+". If you can show me around, let me know ;)" #Generate a really simple random bio
        
    def whoAmI(self):
        print(self.age)
        print(self.firstName)
        print(self.lastInitial)
        print(self.bio)
        
    def getAge(self):
        return self.age
    
    def getFirstName(self):
        return self.firstName
    
    def getLastInitial(self):
        return self.lastInitial
    
    def getBio(self):
        return self.bio
        
newBot = newProfile()
print(newBot.getBio())
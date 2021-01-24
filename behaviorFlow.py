# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:02:06 2021

@author: bbarber

Project Name:QWER Hacks
    
Project Description: Behavioral Pattern for Tinder Bot
"""

#Library Imports (Delete as Needed)
import random
import time

class behaviorFlow:
    def __init__(self):
        #initialize the decision tree
        random.seed()            #seed the generator
        self.iterationsMax = 20   #How many iterations
        self.iterationCurrent = 0 #which iteration are we on?
        
    def chooseBehavior(self, driver):
        if self.iterationCurrent<=self.iterationsMax:
            choice = random.uniform(0,1)
            if choice<0.2:
                self.shortSleep()
            elif choice<0.3:
                self.longSleep()
            elif choice<0.6:
                self.swipe(driver)
                self.shortSleep()
            else:
                self.message(driver)
                self.shortSleep()
            self.iterationCurrent+=1
            self.chooseBehavior(driver)
        else:
            print("Done")
            return
        
    def shortSleep(self):
        #1-3 second nap
        sleepTime = random.uniform(1,3)
        print('Sleeping for {} seconds'.format(str(sleepTime)))
        time.sleep(sleepTime) #comment out to speed up run
        return
    
    def longSleep(self):
        #5-8 second nap
        sleepTime = random.uniform(5,8)
        print('Sleeping for {} seconds'.format(str(sleepTime)))
        time.sleep(sleepTime) #comment out to speed up run
        return
    
    def swipe(self, driver):
        #Choose what direction to swipe
        swiper = random.uniform(0,1)
        if swiper<0.2:
            print("Swipe left")
        else:
            print("Swipe Right")
        return
    
    def message(self,driver):
        #Lets do some chatting
        print("Message")
        return
        
driver = 0
coilette = behaviorFlow()
coilette.chooseBehavior(driver)
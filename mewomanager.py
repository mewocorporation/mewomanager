#!/usr/bin/env python3

import pygame_textinput as pygameti
import pygame
from sys import exit
from pathlib import Path
from json import load as jsonload
from json import dump as jsondump

pygame.init()

# chatgpt code for building on windows cuz i use linux
import sys
from os import path as ospath

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return ospath.join(sys._MEIPASS, relative_path)
    return ospath.join(ospath.abspath("."), relative_path)

######## variables
# display         = pygame.display.set_mode((1863,1048))
# display         = pygame.display.set_mode((1280,100))
display         = pygame.display.set_mode((1280,720))
displaysize     = pygame.display.get_window_size()
bgcolor         = pygame.Color(255,100,100)
txtbgcolor      = pygame.Color(255,127,128)
homeDir         = str(Path.home())
# font            = pygame.font.Font(homeDir+"/jetbrainsmononerd.ttf", 24)
# chatgpt font for windows
font   = pygame.font.Font(resource_path("jetbrainsmononerd.ttf"), 24)
passwordinput   = pygameti.TextInputVisualizer(font_color='White', font_object=font, cursor_color='White')
passwordtext    = font.render("password: "+passwordinput.value, True, 'White')
unlocked        = False
passwords       = { "yoink": 2 }
unlockPassword  = "mewo"
viewPasswords   = [ False ]
seePasswordstr  = [ "<o>" ]
canClick        = True
addingPassword  = False
areWeAddingThePlatformOrThePasswordQuestionMarkTrueIsPlatformFalseIsPassword = True
addPasswordInput= pygameti.TextInputVisualizer(font_color='White', font_object=font, cursor_color='White')
platformAdding  = ""
passwordsAdding =""

"""special character:
•••••••••. this is a place
that you can copy the character"""

# getPasswords() = set passwords to dictionary of the json file
"""def getPasswords():
    with open(homeDir+"/.pwsForMewoManager.json") as file:
        return jsonload(file)
original getpasswords function"""

# chatgpt getpasswords for if .pwsForMewoManager doesnt exist
def getPasswords():
    path = homeDir + "/.pwsForMewoManager.json"
    try:
        with open(path) as file:
            return jsonload(file)
    except FileNotFoundError:
        # create file with empty dict
        with open(path, "w") as file:
            jsondump({}, file)
        return {}

def setPasswords(arrayer):
    with open(homeDir+"/.pwsForMewoManager.json", "w") as file:
        jsondump(arrayer, file)
        
# display = pygame.display.set_mode((720,len(list(getPasswords().keys()))*40 + 100))

while True:
    """ok this will be a possibly long comment telling you what onko is.
    onko is the variable that basically has a number which is the array
    index- sorry, LIST index that can be used for the current password
    we are on for use in the if unlocked statement. does that make sense?
    no, probably not. please try understanding my code and make a pull
    request with a comment that makes sense. thank you for reading this
    madness."""
    onko = 0
    keys = pygame.key.get_pressed()
    display.fill(bgcolor)
    events = pygame.event.get()
    
    passwordinput.update(events)
    
    # handle exit
    for i in events:
        if i.type == pygame.QUIT:
            print("\n\nBYE")
            exit()
    
    # handle the correct password being inputted when not unlocked
    if keys[pygame.K_RETURN] and passwordinput.value == unlockPassword and not unlocked:
        unlocked = True
        passwords = getPasswords()

    # all the code for handling blitting the correct text and stuff
    if unlocked:
        if getPasswords() != passwords:
            passwords = getPasswords()
        for platform, password in passwords.items():
            # handle viewPasswords and seePasswordstr having less items than passwords in .pwsForMewoManager
            if onko > len(viewPasswords) - 1:
                viewPasswords.append(False)
            if onko > len(seePasswordstr) - 1:
                seePasswordstr.append("<o>")
                
            # set the string var with <•> if viewPasswords is true, else <o>
            if viewPasswords[onko] == True:
                seePasswordstr[onko] = "<•>"
                # delete password button
                deleteButton = pygame.draw.rect(display, txtbgcolor, [(20,(onko *40) +eee+3), (30,25)])
                display.blit(font.render("Ø", True, 'White'), (30, (onko * 40) + eee))
                if pygame.mouse.get_pressed()[0] and deleteButton.collidepoint(pygame.mouse.get_pos()) and canClick:
                    canClick = False
                    tempPass = dict(passwords)
                    tempViewPasswords = list(viewPasswords)
                    del tempPass[platform]
                    setPasswords(tempPass)
            else:
                seePasswordstr[onko] = "<o>"
                password = "•••••"
                platform = f"{platform[0]}{platform[1]}••••"#{platform[2]}•••• "
            
            # what am i supposed to call this variable????
            eee = 150
            # blit custom text
            display.blit(font.render(f"{platform}: {password}", True, 'White'), (150, (onko * 40) + eee))
            # button bg
            viewButton = pygame.draw.rect(display, txtbgcolor, [(70,(onko *40) +eee+3), (60,25)])
            # button
            display.blit(font.render(seePasswordstr[onko], True, 'White'), (80, (onko * 40) + eee))
            # handle clicking button
            if pygame.mouse.get_pressed()[0] and viewButton.collidepoint(pygame.mouse.get_pos()) and canClick:
                canClick = False
                viewPasswords[onko] = not viewPasswords[onko]

            # add 1 to onko, and let u clik again
            onko += 1
            #print(viewPasswords, end="    \r")
            if not pygame.mouse.get_pressed()[0] and not keys[pygame.K_RETURN]:
                canClick = True

        #print(passwords)
        # button bg
        addPasswordButton = pygame.draw.rect(display, txtbgcolor, [(20, 30), (190,30)])
        # button to add a passsword
        display.blit(font.render("add password", True, 'White'), (30, 30))

        # handle adding passwords???? try to understand it urself i
        # wont write a very long comment or a lot of 1line comments.
        if pygame.mouse.get_pressed()[0] and addPasswordButton.collidepoint(pygame.mouse.get_pos()) and canClick:
            canClick = False
            addingPassword = True
        if areWeAddingThePlatformOrThePasswordQuestionMarkTrueIsPlatformFalseIsPassword == False and addingPassword == False:
            areWeAddingThePlatformOrThePasswordQuestionMarkTrueIsPlatformFalseIsPassword = True
            setPasswords(passwords)
        if addingPassword == True:
            addPasswordInput.update(events=events)
            display.blit(addPasswordInput.surface, (180, 80))
            if areWeAddingThePlatformOrThePasswordQuestionMarkTrueIsPlatformFalseIsPassword == True:
                display.blit(font.render("platform: ", True, 'White'), (30,80))
                if keys[pygame.K_RETURN] and canClick:
                    areWeAddingThePlatformOrThePasswordQuestionMarkTrueIsPlatformFalseIsPassword = False
                    platformAdding = addPasswordInput.value
                    canClick = False
                    addPasswordInput.value = ""
            else:
                display.blit(font.render("password: ", True, 'White'), (30,80))
                if keys[pygame.K_RETURN] and canClick:
                    addingPassword = False
                    canClick = False
                    areWeAddingThePlatformOrThePasswordQuestionMarkTrueIsPlatformFalseIsPassword = True
                    passwordsAdding = addPasswordInput.value
                    passwords |= { platformAdding: passwordsAdding }
                    setPasswords(passwords)
                    passwordsAdding = ""
                    platformAdding =  ""
                    addPasswordInput.value = ""
        if not pygame.mouse.get_pressed()[0] and not keys[pygame.K_RETURN]:
            canClick = True
            
    else:
        display.blit(passwordtext, (30,30))
        display.blit(passwordinput.surface, (160,30))
        
    pygame.display.update()
    pygame.time.Clock().tick(144)

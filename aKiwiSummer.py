#import modules I will use- Random and Time
import random
import time
import os
#set up initial variables with blank or false values
NAME = ""
achievments = []
def reset():
    global readyToStart
    global earthquakeEvent
    global validInput
    global daysRemaining
    global restart
    global measured
    global aucklAdventure
    global coneThere
    global conePath
    readyToStart = False
    earthquakeEvent = False
    validInput = False
    daysRemaining = random.randint(3,5)
    restart = ""
    measured = False
    aucklAdventure = ""
    coneThere = False
    conePath = ""

reset()

def startGame():
    #define the fuction that begins the game
    global premise
    premise = input("")
    if premise == "a":
        study()
    elif premise == "b":
        holiday()
    else:
        print("Sorry, that's not a valid input.")
        startGame()


def welcome():
    #define the function that welcomes the player and introduces the game
    #declare the global variables for this function
    global NAME
    global readyToStart
    global premise
    print("\033[0;37mWelcome to the game")
    #get player name if they haven't entered it before
    if NAME == "":
        NAME = input("What is your name? ")
    if readyToStart == False:
        #introducde the premise
        print("The premise is that you are a WC kid, and summer has just started. What are you going to do with it?")
        print("Most choices you'll make by typing 'a', 'b', or 'c' into the console")
        while readyToStart == False:
            #if the player is ready to start, start. otherwisae, ask them again
            begin = input("Ready to start? (Y/N) ")
            begin = begin.upper()
            if begin == "Y":
                print("That's great!")
                readyToStart = True
            else:
                print("Sorry to here that. I'll ask again.")
    #choose the main path for the game
    print("What do you want to do with your summer?\n"+"a. Stay at home and study\n"+"b. Go on holiday with your family")
    startGame()


def dayDone():
    #decide whether the number of days left in the game has run out
    global daysRemaining
    daysRemaining -= 1
    print(daysRemaining," days left of your trip!")
    if daysRemaining <= 0:
        gameOver()


def gameOver():
    #end the game
    global restart
    print("\033[1;31mGame Over")
    #print acheivments that have been unlocked
    achievmentCount = len(achievments)
    print("\033[1;33mYou got",achievmentCount,"/7 acheivments")
    print("\033[0;37m")
    time.sleep(1)
    #ask if they want to play again
    restart = input("Would you like to play again? (Y/N)")
    restart = restart.upper()
    if restart == "Y":
        print("restarting...")
        time.sleep(2)
        print("")
        reset()
        if os.name == "posix":
            os.system('clear')
        else:
            os.system('cls')
        welcome()
    else:
        #end the game
        print("I hope you enjoyed the game!\n"+"")
        time.sleep(5)
        exit    


def study():
    #if you chose to study, this will happen
    print("You decide to stay at home for the whole holidays and study.\n"+"What are you even studying for? The school year is over.")
    doStudy = random.randint(1,4)
    #decides wether you actually study
    # 75% chance of giving up studying
    #if you study you'll probably get a better grade
    if (doStudy == 1 or 2 or 3):
        print("After some thinking, you give up on the studying idea")
        grade = random.randint(0,75)
    elif doStudy == 4:
        print("Somehow, you actually end up studying")
        grade = random.randint(50,100)
    #tell the player their grade
    time.sleep(1)
    print("A few months later, you get back your grades for the first test of the year")
    print("Grade: ",grade,"%")
    time.sleep(1)
    if grade > 75:
        if "Nerd" not in achievments:
            achievments.append("Nerd")
            print("\033[1;33mAcheivment unlocked: Nerd!")
            print("\033[0;37m")
            time.sleep(1)
    gameOver()


def auckland():
    global validInput
    global measured
    global aucklAdventure
    global RangitotoAdv
    global conePath
    global coneThere
    print("You take a long train ride to Auckland")
    #TODO add train games- blackjack?
    print("When you get there, you go have a look at the Sky Tower")
    #measure the sky tower minigame
    print("You wonder how big it is. Should you try measure it?(Y/N)")
    validInput = False
    while validInput == False:
        measureTower = input("")
        measureTower = measureTower.upper()
        if measureTower == "Y":
            validInput = True
            measured = True
            print("What do you want to use to measure it? (enter the name of the object)")
            measureWith = input("")
            print("you try to mesaure the Sky Tower with a",measureWith,". You get a new perspective for how tall it is")
            if measureWith == "banana":
                if "Banana for scale" not in achievments:
                    achievments.append("Banana for scale")
                    print("\033[1;33mAcheivment unlocked: Banana for Scale!")
                    print("\033[0;37m")
        elif measureTower == "N":
            validInput = True
            print("You're kinda sad about the missed oportunity, but it doesn't really bother you")
            #finish auckl
        else:
            print("Sorry, that's not a valid input here. Answer Y or N.")
    dayDone()
    print("You decide to explore around Auckland today.")
    print("Where do you want to head?\n"+"a. Try get under the Sky Tower\n"+"b. Explore Rangitoto Island")
    validInput = False
    while validInput == False: 
        global aucklAdventure
        aucklAdventure = input("")
        aucklAdventure.lower()
        if aucklAdventure == "a":
            validInput = True
        elif aucklAdventure == "b":
            validInput = True
        else:
            print("That's not a valid input right now")
    validInput = False
    if aucklAdventure == "a":
        print("You head off to the sky Tower")
    elif aucklAdventure == "b":
        print("You head down to the ferry terminal and hop on the first ferry over to Rangitoto")
        time.sleep(1)
        print("After some time on the ferry, you arrive on the island")
        print("What do you want to do here?\n"+"a. Explore the caves\n"+"b. Climb to the top")
        while validInput == False:
            RangitotoAdv = input("")
            RangitotoAdv.lower()
            if RangitotoAdv == "a":
                validInput = True
            elif RangitotoAdv == "b":
                validInput = True
            else:
                print("That's not a valid input right now, try again")
        validInput = False
        if RangitotoAdv == "a":
            caveQuality = random.randint(1,3)
            if caveQuality == 1:
                print("The caves are kinda mid")
            elif caveQuality == 2:
                print("The caves are decent")
            elif caveQuality == 3:
                print("The caves are lit")
        elif RangitotoAdv == "b":
            print("For about an hour and a half, you try to walk up to the top")
            time.sleep(0.25)
            print("When you finally get there, you go for a walk around the rim")
            time.sleep(0.25)
            print("You look up, and it looks a bit cloudy, so you decide to head back down before it starts raining")
            time.sleep(0.25)
            print("While on your way down, you notice another path. It might be faster")
            time.sleep(0.25)
            print("Do you take it? (Y/N)")
            validInput = False
            while validInput == False:
                conePath = input("")
                conePath.upper()
                if conePath == "Y":
                    validInput = True
                elif conePath == "N":
                    validInput = True
                else:
                    print("That's not a valid input right now. Enter Y or N")
            validInput = False
            if conePath == "Y":
                coneThere = random.randint(1,2)
                if coneThere == 1:
                    #based on another true story
                    print("While going along the alternate path, you come across a very old and mossy road cone")
                    if "Wild Cone" not in achievments:
                        achievments.append("Wild Cone")
                        print("\033[1;33mAcheivment unlocked: Wild Cone!")
                        print("\033[0;37m")
                        print("Finally, the truth on how to get new roadcones has been uncovered! They do actually grow on trees!")
            elif conePath == "N":
                print("The path back is uneventful")
            else:
                print("Error: You broke the game")
        print("You head back to the bottom of the island, just in the nick of time to catch the ferry back")
    print("After that exhausting day, you head back to your hotel for the night")
    dayDone()    


def taupo():
    global validInput
    global daysRemaining
    print("You take a six hour bus ride up to Taupo")
    event = random.randint(1,4)
    if event == 1:
        #I dont have any pent up frustration about this no not at all
        print("Some of your friends are on the bus, too. After some joking around, they take your phone, spam it with selfies, then get your PIN wrong enough times that you get locked out for half an hour and are unable to buy dinner")
    else:
        print("The bus ride is uneventful")
    event = 0
    print("You arrive in Taupo at around 4 pm") 
    #TODO: Taupo
    #fill with based-on-a-true-event stories
    print("You start to get settled in, then dinner time rolls around")
    #pick dinner
    print("What do you want for dinner?\n"+"a. Pizza\n"+"b. Noodles\n"+"c. Cheesey bacon")
    validInput = False
    while validInput == False:
        dinner = input("")
        if dinner == "a":
            validInput = True
            dinnerLocation = random.randint(1,3)
            if dinnerLocation == 1:
                event = random.randint(1,3)
                print("You order pizza from Dominos")
                if event == 1:
                    #based on a true story
                    print("You take it to a table outside the Sushi paradise, despite the sign saying 'Sushi Paradise customer use only.' What a rebel.")
                    if "Criminal" not in achievments:
                        achievments.append("Criminal")
                        print("\033[1;33mAcheivment unlocked: Criminal!")
                        print("\033[0;37m")
            elif dinnerLocation == 2:
                print("You order pizza from Hell's")
                if "Go to Hell" not in achievments:
                        achievments.append("Go to Hell")
                        print("\033[1;33mAcheivment unlocked: Go to Hell!")
                        print("\033[0;37m")
            elif dinnerLocation == 3:
                print("You order pizza from Pizza Hut")
            print("It's tasty enough, if a bit greasy")
            #maybe add a thing where the quality is random or is based on the brand?
        elif dinner == "b":
            validInput = True
            print("You get noodles. They're noodles. What more did you expect?")
        elif dinner == "c": 
            validInput = True
            print("It's cheesy bacon. Litterly bacon with melted cheese on it. Why")
            #why
        else: 
            print("Invalid input. Remember, use a single, lower case letter out of the options provided")
    print("With dinner eaten, you go to bed for the day")
    validInput = False
    dayDone()


def earthquake():
    #decide if an earthquake will happen
    event = random.randint(1,10)
    if event == 10:
        earthquakeEvent == True
    if earthquakeEvent == True:
        #if an earthquake happens they die
        #rip
        print("Suddenly, an earthquake strikes!\n"+"Typical Christchruch")
        print("You get struck by a piece of debris")
        print("You die")
        #give earthquake acheivment
        if "Earthquake" not in achievments:
            achievments.append("Earthquake")
            print("\033[1;33mAcheivment unlocked: Earthquake!")
            print("\033[0;37m")
        earthquakeEvent == False
        gameOver()
    

def christchurch():
    global validInput
    earthquake()
    print("You arrive in Christchurch safely, and go to your hotel for the night")
    dayDone()
    print("Day two of Christchurch: what should you do?")
    print("a. Disaster Tourism\n"+"b. just hang out and look around")
    #can you tell that i didnt add christchuirch for any reason but earthquakes and I cant think of anything else?
    validInput == False
    while validInput == False:
        christchurchExploration = input("")
        validInput == True
        if christchurchExploration == "a":
            print("theres still some ruins left, and you go to explore them")
            print("Wow, disaster tourism? not cool")
            dayDone()
        elif christchurchExploration == "b":
            validInput == True
            print("You vibe for the day")
            dayDone()
        print("The next day, you realise you're as bored exploring Christchurch as I was when I made it, so you go home")
        gameOver()
        #maybe change this idk
    validInput == False
 

def southIsland():
    global validInput
    #pick where to go in the south island
    print("Where in the South Island are you going?\n"+"a. Bluff\n"+"b. Christchurch\n"+"c. Camping somewhere")
    validInput == False
    while validInput == False:
        #sadly due to running out of time christchurhc is the only path I could finish
        #the other two are both flooded
        #which funnily enough happened to me once, I was stuck in the south island for a week b/c of flooded roads
        southIslandPlace = input("")
        if southIslandPlace == "a":
            ##bluff()
            print("Sadly, the road is closed due to flooding")
            print("Maybe try somewhere else?")
            if "Flood" not in achievments:
                achievments.append("Flood")
                print("\033[1;33mAcheivment unlocked: Flood!")
                print("\033[0;37m")

        elif southIslandPlace == "b":
            christchurch()
            validInput = True
        elif southIslandPlace == "c":
            #camping()
            print("Sadly, the road is closed due to flooding")
            print("Maybe try somewhere else?")
            if "Flood" not in achievments:
                achievments.append("Flood")
                print("\033[1;33mAcheivment unlocked: Flood!")
                print("\033[0;37m")
    validInput = False


def holiday():
    #run the entire holiday path
    print("You go on holiday with your family")
    #where to?
    print("Where to?\n"+"a. Auckland\n"+"b. South Island\n"+"c. Taupo")
    validInput = False
    #run until they pick a path
    while validInput == False:
        holidayDestination = input("")
        if holidayDestination == "a":
            auckland()
            validInput = True
        elif holidayDestination == "b":
            southIsland()
            validInput = True
        elif holidayDestination == "c":
            taupo()
        validInput = True
    validInput = False

#this one line literally makes the whole game happen
welcome()
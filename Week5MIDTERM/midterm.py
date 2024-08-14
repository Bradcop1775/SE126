#MIDTERM

#Bradley Coppinger 
#Lab 5 MIDTERM
#8/14/24

#For your Midterm Project in SE126 you will be building a program of your own design! You must work individually to design a program and file of your choosing.  The program must include the following: a file to be read and processed, data stored into respective lists .csv or .txt import csv will work for both of these file types, but all data must be separated with a comma! >= 2 lists these can be populated from a file or by hand showcase understanding of control flow structures showcase understanding of self-built functions Starting Documentation include a brief program description include a variable dictionary with data types including your lists! Documentation for anything used not introduced in the course Creativity! This project should represent topics covered in the first half of the course and show design & development worthy of 6+ hours. 

#BUILD GUIDE - WORLD OF WARCRAFT 

#Variable list

#races = races
#Alliance
#classes_human = human 
#classes_dwarf =dwarf
#classes_night_elf = night elf
#classes_gnome = gnome 
#classes_draeni = draeni
#classes_worgen = worgen
#Horde
#classes_orc = orc
#classes_undead = undead
#classes_tauren = tauren
#classes_troll = troll
#classes_blood_elf = blood elf
#classes_goblin = goblin

#race_choice = [] input of race 


#------------------------------------------------------------------
races = []
game = "yes"
#Alliance
classes_human = []
classes_dwarf = []
classes_night_elf = []
classes_gnome = []
classes_draeni = []
classes_worgen = []
#Horde
classes_orc = []
classes_undead = []
classes_tauren = []
classes_troll = []
classes_blood_elf = []
classes_goblin = []

race_choice = []


#-----------------------------------------------------------------

#Import 
import random 
import csv 
import os
import time

#FUNCTIONS
def clear_terminal():
    # Check the operating system and clear the terminal accordingly
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

#def faction_decision(factionChoice):
    
    


#------MAIN CODE-----------------------------------------------------------

print("Welcome to the World of Warcraft character builder!")

print(f"\nYou have your choice between the mighty Horde and the heroic Alliance. \n\nBelow are a description of each\n\n\tThe Alliance is a faction of diverse races united by shared values of honor, justice, and mutual aid. Comprised of humans, dwarves, night elves, gnomes, draenei, worgen, and more, the Alliance values order and tradition. The faction is rooted in a strong sense of community and cooperation, often standing together to defend their lands and their people from external threats. The Alliance is known for its chivalric traditions and noble causes, often fighting for righteousness and against tyranny. Its capital cities are bastions of culture and civilization, where the light of justice is a guiding principle.\n\n\tThe Horde is a faction forged in battle, comprising races with a shared history of oppression, survival, and resilience. Made up of orcs, trolls, tauren, undead (Forsaken), blood elves, goblins, and others, the Horde is a coalition of diverse cultures that value strength, honor, and freedom. Though the Horde has a reputation for being more savage and warlike, it is also a haven for those seeking refuge from persecution. The Horde emphasizes individual strength, unity in diversity, and the importance of standing together against any who threaten their way of life. The faction's capital cities are centers of tribal culture and fierce independence, where survival and honor are paramount.")

while game == "yes":
    faction = input ("\nDo you choose the Alliance or Horde?: ").lower()
    clear_terminal()
    if faction == "alliance":
        print("Welcome to the Alliance!")

        description = input("Do you know what each class does? If not we have descriptions! (yes/no): ").lower()

        if description == "yes":
            print("Very nice! Continue on!")
        if description == "no":
            clear_terminal()
            print ("\n\tWarrior, Warriors equip themselves carefully for combat and engage their enemies head-on, letting attacks glance off their heavy armor. They use diverse combat tactics and a wide variety of weapon types to protect their more vulnerable allies. Warriors must carefully master their rage – the power behind their strongest attacks. \n\n\tHunters, Hunters battle their foes at a distance or up close, commanding their pets to attack while they nock their arrows, fire their guns, or ready their polearms. Though their weapons are effective at short and long ranges, hunters are also highly mobile. They can evade or restrain their foes to control the arena of battle. \n\n\tMage, Mages demolish their foes with arcane incantations. Although they wield powerful offensive spells, mages are fragile and lightly armored, making them particularly vulnerable to close-range attacks. Wise mages make careful use of their spells to keep their foes at a distance or hold them in place.\n\n\tRouge, Rogues often initiate combat with a surprise attack from the shadows, leading with vicious melee strikes. When in protracted battles, they utilize a successive combination of carefully chosen attacks to soften the enemy up for a killing blow. Rogues must take special care when selecting targets so that their combo attacks are not wasted, and they must be conscious of when to hide or flee if a battle turns against them. \n\n\tPriest, Priests use powerful healing magic to fortify themselves and their allies. They also wield powerful offensive spells from a distance, but can be overwhelmed by enemies due to their physical frailty and minimal armor. Experienced priests carefully balance the use of their offensive powers when tasked with keeping their party alive. \n\n\tWarlock, Warlocks burn and destroy weakened foes with a combination of crippling illnesses and dark magic. While their demon pets protect and enhance them, warlocks strike at their enemies from a distance. As physically weak spellcasters bereft of heavy armor, cunning warlocks allow their minions to take the brunt of enemy attacks in order to save their own skin. \n\n\tPaladin, Paladins start directly in front of their enemies, relying on heavy armor and healing in order to survive incoming attacks. Whether with massive shields or crushing two-handed weapons, Paladins are able to keep claws and swords from their weaker fellows – or they use healing magic to ensure that they remain on their feet. \n\n\tMonk, Whatever their combat role, monks rely mainly on their hands and feet to do the talking, and on strong connection with their inner chi to power their abilities. Monks can also heal their allies while at the same time damaging their enemies. \n\n\tDeath Knight, Death Knights engage their foes up-close, supplementing swings of their weapons with dark magic that renders enemies vulnerable or damages them with unholy power. They drag foes into one-on-one conflicts, compelling them to focus their attacks away from weaker companions. To prevent their enemies from fleeing their grasp, death knights must remain mindful of the power they call forth from runes, and pace their attacks appropriately \n\n\tDruid, Druids are versatile shapeshifters who can fill the role of a healer, tank, melee DPS, or ranged DPS. Their connection to nature allows them to transform into various animal forms, each providing different abilities. Druids can heal allies, deal damage from afar, or engage enemies directly in melee combat. Their ability to adapt to different situations makes them invaluable in any group. \n\n\tShaman, Shamans are spiritual guides and practitioners of elemental magic. They can call upon the powers of earth, air, fire, and water to deal damage or heal allies. Shamans are also capable of summoning totems that provide various benefits to themselves and their group. They can enhance the combat abilities of their allies and deal elemental damage to their enemies. \n\n\tDemon Hunter, Demon Hunters are agile, deadly warriors who have made a pact with dark powers to gain the ability to hunt demons. They can dual-wield glaives and use their enhanced mobility to outmaneuver opponents. Demon Hunters can also transform into demonic forms, gaining powerful abilities to unleash upon their enemies. Their high mobility and ability to tank or deal damage make them a versatile class. \n\n\tEvoker, Evokers are masters of draconic magic,channeling the power of dragons to cast devastating spells. They can both heal their allies and damage their enemies using the potent energy of dragons. Evokers excel at controlling the battlefield, using their powerful breath attacks and draconic abilities to turn the tide of combat.")


    #connected to file----------------------------------
        with open("Week5MIDTERM\Alliance.txt") as csvfile:

            file = csv.reader(csvfile)

            for rec in file: 
            #'file' is an example of a 2D list XD
                races.append(rec[0])
                classes_human.append(rec[1:])
                classes_dwarf.append(rec[1:])
                classes_night_elf.append(rec[1:])
                classes_gnome.append(rec[1:])
                classes_draeni.append(rec[1:])
                classes_worgen.append(rec[1:])
            time.sleep(5)
            print(f"\n\tThere are currently {len(races)} races to choose from in the Alliance.\nThey are: {races}")
            race_choice = input("What race would you like to be?: ").lower()
            if race_choice == "human":
                race_choice = races[0]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[0]} are {classes_human[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "dwarf":
                race_choice = races[1]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[1]} are {classes_dwarf[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "night elf":
                race_choice = races[2]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[2]} are {classes_night_elf[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "gnome":
                race_choice = races[3]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[3]} are {classes_gnome[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "draenei":
                race_choice = races[4]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[4]} are {classes_draeni[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "worgen":
                race_choice = races[5]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[5]} are {classes_worgen[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            

    elif faction == "horde":
        clear_terminal()
        print("For the Horde!")
        description = input("Do you know what each class does? If not we have descriptions! (yes/no): ").lower()

        if description == "yes":
            print("Very nice! Continue on!")
        if description == "no":
            clear_terminal()
            print ("\n\tWarrior, Warriors equip themselves carefully for combat and engage their enemies head-on, letting attacks glance off their heavy armor. They use diverse combat tactics and a wide variety of weapon types to protect their more vulnerable allies. Warriors must carefully master their rage – the power behind their strongest attacks. \n\n\tHunters, Hunters battle their foes at a distance or up close, commanding their pets to attack while they nock their arrows, fire their guns, or ready their polearms. Though their weapons are effective at short and long ranges, hunters are also highly mobile. They can evade or restrain their foes to control the arena of battle. \n\n\tMage, Mages demolish their foes with arcane incantations. Although they wield powerful offensive spells, mages are fragile and lightly armored, making them particularly vulnerable to close-range attacks. Wise mages make careful use of their spells to keep their foes at a distance or hold them in place.\n\n\tRouge, Rogues often initiate combat with a surprise attack from the shadows, leading with vicious melee strikes. When in protracted battles, they utilize a successive combination of carefully chosen attacks to soften the enemy up for a killing blow. Rogues must take special care when selecting targets so that their combo attacks are not wasted, and they must be conscious of when to hide or flee if a battle turns against them. \n\n\tPriest, Priests use powerful healing magic to fortify themselves and their allies. They also wield powerful offensive spells from a distance, but can be overwhelmed by enemies due to their physical frailty and minimal armor. Experienced priests carefully balance the use of their offensive powers when tasked with keeping their party alive. \n\n\tWarlock, Warlocks burn and destroy weakened foes with a combination of crippling illnesses and dark magic. While their demon pets protect and enhance them, warlocks strike at their enemies from a distance. As physically weak spellcasters bereft of heavy armor, cunning warlocks allow their minions to take the brunt of enemy attacks in order to save their own skin. \n\n\tPaladin, Paladins start directly in front of their enemies, relying on heavy armor and healing in order to survive incoming attacks. Whether with massive shields or crushing two-handed weapons, Paladins are able to keep claws and swords from their weaker fellows – or they use healing magic to ensure that they remain on their feet. \n\n\tMonk, Whatever their combat role, monks rely mainly on their hands and feet to do the talking, and on strong connection with their inner chi to power their abilities. Monks can also heal their allies while at the same time damaging their enemies. \n\n\tDeath Knight, Death Knights engage their foes up-close, supplementing swings of their weapons with dark magic that renders enemies vulnerable or damages them with unholy power. They drag foes into one-on-one conflicts, compelling them to focus their attacks away from weaker companions. To prevent their enemies from fleeing their grasp, death knights must remain mindful of the power they call forth from runes, and pace their attacks appropriately \n\n\tDruid, Druids are versatile shapeshifters who can fill the role of a healer, tank, melee DPS, or ranged DPS. Their connection to nature allows them to transform into various animal forms, each providing different abilities. Druids can heal allies, deal damage from afar, or engage enemies directly in melee combat. Their ability to adapt to different situations makes them invaluable in any group. \n\n\tShaman, Shamans are spiritual guides and practitioners of elemental magic. They can call upon the powers of earth, air, fire, and water to deal damage or heal allies. Shamans are also capable of summoning totems that provide various benefits to themselves and their group. They can enhance the combat abilities of their allies and deal elemental damage to their enemies. \n\n\tDemon Hunter, Demon Hunters are agile, deadly warriors who have made a pact with dark powers to gain the ability to hunt demons. They can dual-wield glaives and use their enhanced mobility to outmaneuver opponents. Demon Hunters can also transform into demonic forms, gaining powerful abilities to unleash upon their enemies. Their high mobility and ability to tank or deal damage make them a versatile class. \n\n\tEvoker, Evokers are masters of draconic magic,channeling the power of dragons to cast devastating spells. They can both heal their allies and damage their enemies using the potent energy of dragons. Evokers excel at controlling the battlefield, using their powerful breath attacks and draconic abilities to turn the tide of combat.")




    #connected to file----------------------------------
        with open("Week5MIDTERM\Horde.text") as csvfile:

            file = csv.reader(csvfile)

            for rec in file: 
            #'file' is an example of a 2D list XD
                races.append(rec[0])
                classes_orc.append(rec[1:])
                classes_undead.append(rec[1:])
                classes_tauren.append(rec[1:])
                classes_troll.append(rec[1:])
                classes_blood_elf.append(rec[1:])
                classes_goblin.append(rec[1:])
            time.sleep(5)
            print(f"There are currently {len(races)} races to choose from in the Horde.\nThey are: {races}")
            race_choice = input("What race would you like to be?: ").lower()
            if race_choice == "orc":
                race_choice = races[0]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[0]} are {classes_orc[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "undead":
                race_choice = races[1]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[1]} are {classes_undead[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "tauren":
                race_choice = races[2]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[2]} are {classes_tauren[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "troll":
                race_choice = races[3]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[3]} are {classes_troll[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "blood elf":
                race_choice = races[4]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[4]} are {classes_blood_elf[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")
            elif race_choice == "goblin":
                race_choice = races[5]
                clear_terminal()
                for i in range (0, 1):
                    print(f"The current classes available for {races[5]} are {classes_goblin[i]}")
                    time.sleep(5)
                    print("\nRemember: Choose the class that fits YOU! You having fun is most important!")
                    time.sleep(3)
                    print("Thanks for using our build guide!")



    else:
        print("Error found. Please Try again.")
        game = input ("Would you like to restart? [Yes or No]: ").lower()
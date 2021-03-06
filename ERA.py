
#ERA.py
#by Evelyn, Rachel, Alexis
#Code for the choose your own adventure game, ERA.

### Import Statements ###
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import random
root = Tk()
w = Label(root, text="ERA")
w.pack()

def intro():
    """Start of the story"""
    messagebox.showinfo ("Old Lady",
                         " You're walking down the street and you see a sweet "+\
                         "old lady trip and fall on her face.")
    oldlady = simpledialog.askinteger (" Please type the number corresponding to your desired class.",
                                    " To steal her purse while she's down, press 1 " +\
                                    " To mind your own buissness and walk past, press 2. " +\
                                    " To help her up, press 3.")


    if oldlady == 1:
        choice1()
    elif oldlady == 2:
        ignoreOldLady()
    elif oldlady == 3:
        helpOldLady()
    else:
        intro()

############################### Rachel's Function ###############################
def choice1():
    choice = messagebox.showinfo ("You steal her purse",
                             " You run by and snatch her purse as she struggles to get up."+\
                             " You hear her cursing at you as you run off into the near by forest."+\
                             " You feel you aren't bein chased, and begin rooting through her purse."+\
                             " Inside you find nothing but a bunch of old lady stuff, until a ragged old"+\
                             " paper catches your eye. You unfold it and see that it is a treasure map!"+\
                             " The treasure seems to be somewhere in the forest you're in now, so you set"+\
                             " off to find it.")
   

    messagebox.showinfo ("The Forest",
                             " As you're reading the map, you here voices behind you."+\
                             " 'That way! Into the forest!' you here and old lady shout."+\
                             " 'Okay mam we will get your purse back for you.' a deeper, younger"+\
                             " voice says. You get scared and run off further into the forest. Your"+\
                             " bad karma catches up to you, as you find yurself tripping into a river"+\
                             " you forgot was there. You make it to the other side, but part of the map"+\
                             " is ruined.")
    messagebox.showinfo(" Lost",
                            " You walk for a couple hours, trying to remember all of the map"+\
                            " you can, and have been successful so far, until now. You don't"+\
                            " remember if you should go left or right.")

    leftorright= simpledialog.askinteger ("Left or Right?",
                             " Press 1 for right, or 2 for left.")

    if leftorright ==1:
         Rchoice1 
    elif leftorright ==2:
        Rchoice2()
    else:
        choice1()

def Rchoice1 ():
    messagebox.showinfo(" Right",
                        " You try to remember, and you're fairly certain the map said to go right."+\
                        " You turn right, and after a bit of walking, you come to a dungeon, just like"+\
                        " the one the map described! You go down into the dungeon, and trip on a rock."+\
                        " You tumble down into a giant open room with a sleeping dragon, which is now awake"+\
                        " because of you. The giant dragon stands up and prepares to attack.")
           
            
    attack = simpledialog.askinteger (" Press 1 to attack.",
                                      " To attack, press 1. ") 
    if attack ==1:                
        dragonhp = random.randint (15,50)
        dragondmg = random.randint (5, 15)
        playerhealth = random.randint (20, 30)
        playerdamage = random.randint (5, 25)
        while playerhealth >= 0 or dragonhp >= 0:
            dragonhp -= playerdamage
            playerhealth -= dragondmg
            messagebox.showinfo ("Dragon Battle",
            "You took {} damage.".format(dragondmg) +\
            "Your health is now: {}".format(playerhealth)+\
            "The dragon has {} health" .format(dragonhp))
            if playerhealth <= 0 or dragonhp <= 0:
                break 

    if playerhealth <= 0:
        messagebox.showinfo("You died",
                                "The dragon burnt you with his firey breath, leaving"+\
                                " you dead on the floor, so close to the treasure.")

    elif playerhealth <= 0 and dragonhp <= 0:
        messagebox.showinfo("You both died",
                                " You both fall dead to the floor. You didn't live, but"+\
                                " you're happy that you killed the dragon too. In your last moment"+\
                                " of life, as the dragon's flames consume you, you see the"+\
                                " old woman run in, activate a hidden door on the wall, revealing the."+\
                                " treasure. She grabs as much as she can carry, and runs out with, smiling"+\
                                "  and thanking you as she runs past.")                           
        root.destroy
    elif playerhealth >= 1:
        messagebox.showinfo (" You won ",
                                 " Somehow, you managed to slay the dragon.")

        messagebox.showinfo (" You find the treasure...",
                                     " You slay the dragon, and you see part of the wall"+\
                                     " slide down behind it. You run in and see a huge treause"+\
                                     " chest, filled with gold and gems. You begin grabbing as many"+\
                                     " as you can carry. Suddenly, you see the old lady burst into"+\
                                     " the room. She runs in, trips you, and steals all of the treasure"+\
                                     " 'See!? How does it feel huh??? Not very good! Thats what you deserve'."+\
                                     " she shouts at you as she runs away laughing, leaving you on the ground"+\
                                     " with nothing.")
        root.destroy

                
                                
                                     
       
                                


    
def Rchoice2 ():
    messagebox.showinfo(" Left",
                             " You begin walking left. You walk for an hour or so with no signs of the dungeon the"+\
                             " map described. You do however come across an old house hidden in the woods. You are"+\
                             " tired and hungry, and decide to see if who ever is inside will help you. You walk in"+\
                             " and don't see anyone. You call out, and hear no response. Suddenly, the door slams"+\
                             " behind you, and you hear an old lady cackling. You see a figure step out of the shadows"+\
                             " and yuo recognize it as the old lady you stole from, except now, she is dressed in witch"+\
                             " clothes. Turns out she is actually a powerful caster, and she's very mad at you. You see"+\
                             " a fireball begin to burn in her hand, and she prepares to attack.")
                             
     
    lastbattle()


def lastbattle ():
    witchhp = random.randint (20,25)
    witchdmg = random.randint (3, 20)
    playerhealth2 = random.randint (20, 30)
    playerdamage2 = random.randint (5, 25)
    while playerhealth2 >= 0 or witchhp >= 0:
        attack = simpledialog.askinteger (" Press 1 to attack.",
                                            " To attack, press 1. " )
        


        if attack == 1:
            witchhp -= playerdamage2
            playerhealth2 -= witchdmg
            messagebox.showinfo ("Witch Battle",
            "You took {} damage.".format(witchdmg) +\
            "Your health is now: {}".format(playerhealth2)+\
            "The witch has {} health" .format(witchhp))
        if playerhealth2 <= 0 or witchhp <= 0:
            break 

    if playerhealth2 <= 0:
        messagebox.showinfo("You died",
                                "The old lady laughs as you fall dead to teh floor."+\
                                " 'Thats what you deserve for stealing from old ladies."+\
                                " Now you'll never do it again. Tehehehehe' she says as"+\
                                " she loots your dead body.")
        root.destroy()

    

    elif playerhealth2 >= 1:
        messagebox.showinfo (" You won ",
                                 " Somehow, you managed to kill the old lady.")

        messagebox.showinfo (" You kill the old lady...",
                                     " The witch falls dead at you feet, and you proceed to loot"+\
                                     " her house. You really didn't learn anything did you?")
        root.destroy

                

    
                        
    

    



############################## Alexis' Function #################################
def ignoreOldLady():
    """Ignore Helping the old lady"""
    choice = messagebox.showinfo("Walk Past Her",
                                     " Trying to avoid eye contact with the old lady you quickly"+\
                                     "  pull your hand up to your face and sheild your view of her as"+
                                     " you walk by, leaving her struggling to get up. After crossing"+\
                                     " the street you look to where the old lady was still attempting to get"+\
                                     " to her feet and think about going back to help her.")

    messagebox.showinfo ("Help or Leave",
                             "As you sit there the old lady glances across the steet and notices you."+\
                             " You are left with the choice to either go and help her up or turn "+\
                             " around and leave her in the street.")
        
    leaveorhelp = simpledialog.askinteger ( "Help or Leave",
                                              "Press 1 to help, or 2 to leave."
                                              "You decide to...")
                              

                         
    if (leaveorhelp == 1):
        messagebox.showinfo("Change of Heart",
                            "You feel bad for leaving the old lady laying in  the street"+\
                            "and you go back to help her up. She struggles for a moment but"+\
                            " seems alright when she finally gets to her feet.'Why thank you"+\
                            " young traveler, I would have never been able to get up all by my"+\
                            " self. I appreciate your assistance!'she says while fishing around"+\
                            " in her purse. After a moment she pulls out an old tatterd look paper"+\
                            " and places it in your hand.'I think you deserve this for your good deed"+\
                            " today,it is very fragile but of great importance! Do not loose this and"+\
                            " make sure you are well prepared before setting off. Have a nice day now.'"+\
                            " She takes off down the street as you stare at the paper in your hand.")
        
        messagebox.showinfo("The Map",
                            "You unfold the paper in your hand very carefully. Finally "+\
                            " opening the entire paper you realize this is a treasure map!"+\
                            " As you study the map you think back to what the old lady had said."+\
                            " 'She said something about being well prepaired.' You can either "+\
                            " prepare yourself first (1) or try to go without any supplies (2).")
        
        getting_ready = simpledialog.askinteger("Getting Ready",
                               "Supplies(1), Empty Handed(2)"+\
                               "You decide to...")
        
        

    elif (leaveorhelp == 2):
        messagebox.showinfo("Ignore Her",
                            " You decide she dosent need your help and walk away."+\
                            " You walk around town and look through the shops, forgetting"+\
                            " about the old lady. Eventually you get bored and go home to"+\
                            " live out your boring life. THE END.")
        
                                            ###WHY ERROR WHEN ENDDING leaveorhelp == 2 ?###
        
    else:
        ignoreOldLady()

    if getting_ready == 1:
        Prepaired()
        

    elif getting_ready == 2:
        Unprepaired()

    else:
        ignoreOldLady()
        

def Prepaired():
    """Prepairing for battle"""
    gold = 10
    
    messagebox.showinfo("Gearing Up",
                        "You walk into town while counting your money."+\
                        "You count out 10 gold as you walk into the town square."+\
                        "Looking around you decide to go into the blacksmith." )
    
    messagebox.showinfo("Blacksmith",
                        "You walk into the store and are welcomed in by the shopkeeper."+\
                        " 'What can i get for you today?' You think for a momment and decide"+\
                        " to purchase... A Sword(1), Chestplate(2), or both the Sword and Chestplate(3).")
    
    purchase = simpledialog.askinteger("Purchase",
                            "Sword (1) cost 5 gold, Chestplate(2) cost 5 gold, Both(3) cost 10 gold,"+\
                            "You decide to purchase...")


#Sword"
    if purchase == 1:
        gold = gold - 5

        messagebox.showinfo("This Will Do.",
                            "Now that you've got your sword you set of in the direction" +\
                            " that the map specifies.")
        
        messagebox.showinfo("Bear,",
                            "As you walk through the forest following the map you run into an angry"+\
                            " bear. She dosent look like she is going to let you go without a fight."+\
                            " Normaly you would run away from this situation but since you bought this sword"+\
                            " you feel pretty confident and decide to fight the bear.")

        
        messagebox.showinfo("Die.",
                            "As you swing the sword at the bear you manage to get a few good cuts in."+\
                            " After you balance yourself out again you look up at the bear to see the damage"+\
                            " you did. Looking at the bear you see it hasnt moved since you got there and is not"+\
                            " amussed with your attempt at defeating it.The  bear stands up and"+\
                            " takes you out with one big swipe of its claw and rips open your chest."+\
                            " Your body is left on the forest floor to be eaten by the bear cubs and any other"+\
                            " critter that walks by your lifeless body. Well at least you tried your best,"+\
                            " and hey now someone gets a free sword."+\
                            " THE END.")

        





#Chestplate#      
    elif purchase == 2:
        gold = gold - 5

        messagebox.showinfo("Protected.",
                            "Now that you can almost gurantee you most likely won't"+\
                            " get stabed through the chest you feel safe enough to set"+\
                            " of into the direction the map specifies.")
        
        messagebox.showinfo("Bear,",
                            "As you walk through the forest following the map you run into an angry"+\
                            " bear. She dosent look like she is going to let you go without a fight" +\
                            " Since you didnt buy a weapon to fight with you dont really know how your"+\
                            " going to get out of this besides running away. So you turn around as quickly"+\
                            " as you can and the bear swipes at your back making a loud clashing noise. She hit"+\
                            " the chestplate! As you continue running along deeper into the forest you notice the"+\
                            " bear is gone and you dropped the map ahwile ago while fleeing. As you come to a stop and"+\
                            " realize you're completly lost and have no idea where you are, you sit down next to the closest tree."+\
                            " You are completly exausted and start to fall asleep, but as you do you here a low growl."+\
                            " To tierd to get up you pass out and are ripped apart in your sleep by the bear."+\
                            " THE END.")

#Sword and Chestplate#         
    elif purchase == 3:
        gold = gold - 10

        messagebox.showinfo("Let's Go!",
                            "Now that you're looking good but broke you set off in the"+\
                            "direction the map specifies with your sword and chestplate.")

        messagebox.showinfo("Bear",
                            "As you walk through the forest following your map you run into"+\
                            " an angry looking bear. The bear dosent look like its going to let you"+\
                            " go without a fight. Not fearing the callange you pull out your sword and"+\
                            " aim for the bears heart.")
        messagebox.showinfo("Kill",
                            "You  swing the sword twords the bears heart and hit right on."+\
                            " The bear falls over and lets out a loud roar, knowing that it isnt going"+\
                            " to get back up you continue on your journy, paying close attention to the map.")
        Hero()

        
        




        
    else:
        Prepaired()


def Unprepaired():
    """Going to die"""
    messagebox.showinfo("Unsafe",
                        "You decide not to take the old ladys warning and figure you"+\
                        " can handle whatever it is this old lady is so affraid of, besides"+\
                        " its probably not that big of a deal anyways.")
    messagebox.showinfo("Fight!",
                        "As you walk along the trail paying close attention to the map,"+\
                        " you hear a low angry growl...You slowly peek up from the map"+\
                        " and see a very angry looking mother bear.")

    messagebox.showinfo("Died,",
                        "You are now looking right into the bears eyes and"+\
                        " she dosent look like she's going to let you go without"+\
                        " a fight. About this time you really regret not buying anything"+\
                        " to protect yourself back at the store. The Mother bear stands up and"+\
                        " takes you out with one big swipe of her claw and rips open your chest."+\
                        " Your body is left in the forest to be eaten by the bear cubs and any other"+\
                        " critter that walks by your corpse."+\
                        " THE END.")

                            ### Why errror when ending def Unprepaired? ###

    

def Hero():
    """ The Choice Where you live """
    
    messagebox.showinfo("Hero",
                        "You follow the map for a long while and end up at a large"+\
                        " cave. You attempt to peer inside but you are only meet with"+\
                        " darkness. ")
    
    messagebox.showinfo("Hero",
                        "You decide you have to go into the cave if you have already traveled"+\
                        " this far. As you walk in you hear a strange noise...")
    messagebox.showinfo("Dragon",
                        "As your eyes ajust to the dim light coming from deeper within the cave,"+\
                        " you are frozen in place by the sight of a dragon... Sitting ontop of all"+\
                        " this gold! Now you have to decide. Try to fight the dragon for the gold(1) or"+\
                        " sneak past it and try to collect as much as you can before he wakes up and you"+\
                        " escape(2).")
    sneak_or_steal = simpledialog.askinteger("Fight OR Flight",
                                             "1 for fighting the dragon or 2 for sneaking."+\
                                             " you decide to...")
    if sneak_or_steal == 1:
        messagebox.showinfo("Fight",
                            "You decide to walk strait up to the dragon and announce your"+\
                            " here. He slowly starts to get up looking strait at you. When the"+\
                            " dragon is almost fully standing you charge at it with your sword."+\
                            " The dragon suffers a massive cut right to the belly but continues to fight you.")
        dragon_Fight()
        
        

    elif sneak_or_steal == 2:
        messagebox.showinfo("Sneak",
                            "As you try your best to sneak around the dragon,"+\
                            " your sword scratchs the ground behind the beast and it"+\
                            " wake up. You try to find a place to hide but its to late."+\
                            " the dragon turns around and blasts you with fire. You are"+\
                            " now super crispy (and also dead) and the dragon returns to rest."+\
                            " THE END.")

def dragon_Fight():
    """ Fighting the dragon """
    
    dragon_hp = random.randint(50,150)
    dragon_dmg = random.randint(5,50)
    hero_hp = random.randint(100,200)
    hero_dmg = random.randint(25,50)

    while hero_hp >= 0 or dragon_hp >=0:
        attack = simpledialog.askinteger("Attack.",
                                         " Press 1 to attack dragon.")


        if attack == 1:
            dragon_hp -= hero_dmg
            hero_hp -= dragon_dmg
            messagebox.showinfo("Dragon Fight",
                                " You took {} damage.".format(dragon_dmg)+\
                                
                                " Your health is now {}.".format(hero_hp)+\
                                " The dragon has {}.".format(dragon_hp))

        if hero_hp <= 0 or dragon_hp <= 0:
            break
        if hero_hp <= 0:
            messagebox.showinfo("Died",
                                "As hard as you tried the dragon still manages to kill you."+\
                                " You have died. THE END.")
        elif hero_hp >=1:
                messagebox.showinfo("Won",
                                    "You kill the dragon and all the treasure is now yours."+\
                                    " The End.")

                root.destroy()
root.destroy()
                
        

############################## Evelyn's Function ################################
def helpOldLady():
    messagebox.showinfo("You help the old lady",
                        "You extend your hand to help her up and hobble to the nearest sitting area"+\
                        "She is really greatful of your kind act in helping her. She then asks if you" +\
                        "would like to go grab a bite to eat for lunch that she will gladly pay for you" +\
                        "You kindly accept and drive with her to the nearest Cafe in town. During the hearty meal" +\
                        "she says 'I have something important for you. It's a treasure map that holds many"+\
                        "exciting treasures that a person as kind as you deserves to find and possess." +\
                        "I would like you to be the person to have this treasure.")

    messagebox.showinfo("Accept or Deny Map",
                            "While taking in what the old lady has just told you, you contemplate this idea of"+\
                            "seeking out this treasure. You must now choose whether to accept the treasure map" +\
                            "or decline the idea.")
    AcceptOrDenyMap =simpledialog.askinteger ( "Accept or Deny Map",
                                                "Press 1 to accept, or 2 to deny Map."
                                                "Choose Wisely...")
    if (AcceptOrDenyMap == 1):
        messagebox.showinfo(" AcceptOrDeny","The old lady tells you to first be aware of the horrid dragon lurking in the"+\
                            "Western and Eastern sides of where the treasure is located. So you must approach"+\
                            "it through the Southern or Northern side of it. Behind the map there is a code"+\
                            "to open the treasure box but it can only be seen under the moonlight. But be"+\
                            "aware you only get one shot to put in the right code otherwise the treasure box will"+\
                            "desintegrate and be gone until another 100 years. Now this dragon that lurks guarding the"+\
                            "treasure only sleeps every two weeks on a Wednesday and has eyes like a hawk. But there is the choice of battling"+\
                            "the dragon and if you choose to do that the riches become greater for you than before but it" +\
                            "is the much more deadly and fatal route to take for you must stab it in the heart.")
        
        fight()

    elif (AcceptOrDenyMap == 2):
        deny()

def deny():
    messagebox.showinfo("Deny", "The old lady's heart saddens knowing that she had so much faith in you, bids you goodbye"+\
                             "and you both go your seperate ways both full of emptiness and a sense of loss.The End.")
    root.destroy()
        
                             

def fight():                             
    FightOrNot = simpledialog.askinteger ( "Fight the dragon",
                                           "Press 1 to fight, or 2 to wait for dragon to fall asleep"
                                           " Take your pick....")

    if (FightOrNot == 1):
        messagebox.showinfo("Fight","You must physically and mentally prepare to fight this dreadful dragon. That night"+\
                            "you find the code under the moonlight and wake up early in the morning to sharpen your"+\
                            "sword and spear. As you walk down the long pathway in the hillside where the dragon lays" +\
                            "you can begin to smell the deadly smoke the dragon has blowed and you begin to feel stick to" +\
                            "your stomach. The feelings of doubt begin to haunt you, but the reassuring words of the old lady"+\
                            "begin to come to you and the deep faith the old lady has in you helps you continue to push on"+\
                            "You are now sweating vigorously because of the hot humid breath the dragon's fire has released")
        
        messagebox.showinfo("Fight", "You can see the dragon it is black like the night with a long red stripe down it's back it is so"+\
                            "large you feel yourself getting smaller by the second as you come from the South side of it just as the"+\
                            "old lady has told you too. However the dragon has sensed that there is someone there and is pacing back"+\
                            "and forth letting out fire every second all around him. You are now inside a ring of fire alone with"+\
                            "the horrid dragon. The dragon has now spotted you and is roaring at you in rage and fury. You attempt"+\
                            "to climb it's back and stab the dragon for support to get you higher up closer to the heart")
                             
        messagebox.showinfo("Fight","You can feel the burn of your cuts from the scaly skin of the dragon tearing into you and buckets of"+\
                            "sweat dripping down your entire body. You are now spinning in circles and feel yourself in a whirlwind"+\
                            "You are clinging on for dear life as your hands are bleeding their way closer to the heart. Everything"+\
                            "has now become a worldwind you smell burning skin, hair and blood and it's making you feel queasy yet you"+\
                            "are so close to heart of the dragon you can feel and hear it's thumping heartbeats.You place your bloody"+\
                            "hand on it's heart and then you stab it so hard that you feel your hand being thrusted inside the dragon"+\
                            "you feel yourself being flung outside of the ring of fire and hit the ground so hard you feel you've broken"+\
                            "some bones. You have done it..You have killed the dragon! You then limp over to the cave where it had been"+\
                            "hidden and admire the beauty glowing from the golden box. You then put in the code and open the treasure........")
        share()                 
                            
    elif (FightOrNot == 2):
        messagebox.showinfo("Wait", "It is a Wednesday morning and you must wait another two weeks for the dragon to sleep."+\
                            ".....TWO WEEKS LATER..you're a bit nervous but anxious to see this treausre it's been"+\
                            "lingering on your mind for the past two weeks. You then finally start walking towards the"+\
                            "dragon making sure to come at it towards the Southern side. You then see the wild beast"+\
                            "breathing in and out the deadly smoke it produces. You walk as quietly as possible and make sure"+\
                            "to follow the instruction the old lady has told you. You then see the brown box, put the code in and"+\
                            "open the treasure......")

        share()

def share():
    ShareorKeep = simpledialog.askinteger( "Share or Keep",
                                            "Would you like to publically share your riches to the world or keep your finding to yourself"
                                            "Press 1 to keep findings to yourself, or 2 to share to the public"
                                            "Think wisely...")
    if (ShareorKeep == 1):
        messagebox.showinfo("Keep", "So since you have decided to keep to yourself you decide to write a novel on the journey"+\
                            "taken to get this treasure. You have decided that by keeping it to yourself it will be a family secret for your future "+\
                            "children and future descendants to enjoy and have as a family heirloom. You are content with your decision, because it"+\
                            "brings a sort of peace and content to yourself.")
    elif (ShareorKeep == 2):
        messagebox.showinfo("Share", "Since you've chosen to share with the public, there are now news reporters at your front door"+\
                            "throwing tons of questions at you on how you got the treasure and where the treasure is now...you're a bit"+\
                            "overwhelmed by all the publicity that you're getting, but now you've become a bit famous and you seem to be"+\
                            "enjoying yourself......at the present moment....")

        


                             
                            
                
        
                             
                            
                        







############################# Main ##############################################
intro()

root.destroy()








    

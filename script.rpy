# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#question 11 means question 1 out of the first
#question 12 means question 1 out of the second
define mc = Character("[mc_name]")
define unknown = Character("???")
define allen = Character("Allen Avadonia")
define riliane = Character("Riliane Lucifen D'Autriche")
define headmaid = Character("Mariam Phutapie")
define pollo = Character("Pollo")
define arte = Character("Arte")
define artepollo = Character("Arte and Pollo")
define banica = Character("Banica Conchita")
define chartette = Character("Chartette Langley")
define leonhart = Character("Leonhart Avadonia")


#flags

default question11 = False
default question21 = False
default opened_message = False

# The game starts here.


label start:

    stop music fadeout(2.0)
    scene outside
    
    "Okay... So I have been hired to take this job as a servant.."
    "Well... The message said I should go inside."

    "*You step inside*"

    scene entrance
    
    "This is where someone would meet me they said.."
    "*After a bit a servant opens the door.*"

    show allenimage at left with dissolve

    unknown "Are you the new guy?"
    "Are you the one the message said I would first meet at this time?"
    $ mc_name = renpy.input("Yes, correct. I am, My name is Allen, And you?", default="Alexia").strip()   #i dont know what else the default name should be so this looks good, gotta
    mc "I am [mc_name]"
    allen "So, shall I show you around?"
    mc "Yes, thank you!"
    allen "Okay then. Follow me."

    scene hallwayanorth

    allen "So this is Hallway North, known as Hallway A."

    scene hallwaybeast

    allen "This is Hallway East, known as Hallway B."

    scene hallwaycwest

    allen "This is Hallway West, known as Hallway C."

    scene hallwaydsouth

    allen "And as last, Hallway South, known as Hallway D."
    mc "Okay, got it."
    allen "Good. Remember it."
    show allenimage at center with dissolve
    mc "So will I get a house or room or what?"
    allen "You will get a room. It will be assigned to you shortly."
    mc "Okay, got it."
    allen "Shall I escort you to your room?"
    mc "Yes, thank you."

    scene servantsroomhallwaynearb
    show allenimage at center with dissolve
    allen "At room 205 will be your room."
    mc "Okay, got it."
    mc "Hey, will I get a new outfit, or will I serve with this on?"
    allen "Your outfits are in your room."
    mc "Okay, got it then."
    


    #first question
    label question1:
    menu:
        "Any more questions?"

        # This choice only shows if asked_where_go is False
        "Will there be duties outside?" if not question11:
            # Change the variable to True so it disappears next time
            $ question11 = True
            "Yes, there will be. Mostly it will be putting flowers or replacing them"
            jump question1 # Go back to the menu

        # This choice only shows if asked_where_be is False
        "What kind of duties will I have?" if not question21:
            $ question21 = True
            "It will depend on what the princess wants or if the castle needs cleaning or organizing."
            jump question1 # Go back to the menu

        "No, thanks that's all!":
            "Alright. Let's move on then."

    show allenimage at left with move
    allen "So, shall I-"

    show rilianeimage at right with dissolve
    riliane "Ohohoho! Kneel to me!"
    hide allenimage with dissolve
    "You quickly look at Allen who is kneeled and you quickly kneel too."
    allen "Good morning, your highness."
    riliane "Who is this?"
    allen "The new servant, your highness."
    riliane "Oh?~ A new servant?"
    allen "Yes-"
    riliane "Good, seems like he can clean my shoes whenever I want! What is his name?"
    allen "He is [mc_name]"
    riliane "[mc_name]... What a dumb name! Muahahah!"
    hide rilianeimage with dissolve
    "Riliane leaves the room"
    show allenimage at left with dissolve
    mc "*In a whispering tone* So that's the princess.."
    allen "Yes. Indeed."
    "*They both stand up*"
    allen "So, you better go to your room now, we'll speak tomorrow."
    hide allenimage with dissolve
    "*You nod and go to your room before Allen taps your shoulder*"
    show allenimage at center
    allen "You forgot this."
    "*He gave you the roster*"
    mc "Thank you."
    hide allenimage with dissolve
    "*Allen nodded and left*"
    scene roomtwozerofive
    mc "So this is my room.."
    "*You lay down in your bed*"
    "*Next day*"
    mc "Ugh, this bed is atleast better than the floor atleast"
    "*You go to your closet grab your new servant outfit and check your roster*"
    mc "Go to Mariam Phutapie on the first floor with a door that says HEADMAID.. Do your duties..."
    "After reading for a bit"
    mc "And if any questions left speak with Allen Avadonia.."
    mc "Okay, got it"
    scene stairs
    "*At the stairs you bump against someone*"
    unknown "Ugh! Watch where you're going!"
    mc "Sorry, I didn't see you there."
    unknown "Ugh, just don't get in my way again!"
    "*You didn't see who it was but you kept walking to the first floor*"
    "*You go to the first floor and find the door that says HEADMAID*"
    scene headmaidsoffice
    show mariamimage with dissolve
    unknown "Hello, you must be the new servant."
    mc "Yes."
    headmaid "I am Mariam Phutapie, the headmaid of this castle. I will give you duties to complete, did Allen Avadonia tell you about me?"
    mc "Kind of, he only gave me a roster and said to go to you for duties."
    headmaid "Atleast he gave you the roster, okay, good. I will give you your first duty in a bit"
    mc "So what will I be doing then?"
    headmaid "Go explore the castle for a bit and familiarize yourself with the layout."
    mc "Okay, got it."
    scene hallwaybeast
    "*You go explore around the castle and accidently bump into someone again*"
    unknown "Hey! Watch it!"
    mc "Sorry.."
    unknown "Wait... I don't recognize you.. Are you new here?"
    mc "Yeah, I just got hired as a servant yesterday."
    chartette "Oh, I see. I'm Chartette Langley, a maid."
    show chartetteimage with dissolve
    mc "Nice to meet you!"
    chartette "So, shall I show you around?"
    mc "No, thank you! Allen showed me around already."
    chartette "Oh, Allen.. Always ruining the moment I want to show someone about!"
    mc "Do you hate Allen for some reason?"
    chartette "No way! Never!"
    "*As if on cue Allen appears*"
    show chartetteimage at left with move
    show allenimage at right with dissolve
    allen "So, what is happening here?"
    chartette "Nothing, why?"
    allen "I heard my name, that's why."
    chartette "I was asking questions to the new servant. What's his name anyways?"
    allen "Don't make him resign like the others, okay? It is [mc_name]"
    chartette "What a nice name! But hey! I don't make people resign THAT easily!"
    chartette "Right?"

    menu:
        "Yes":
            chartette "See? I knew you'd agree!"

        "No":
            chartette "Hey! That's not true at all! Hmph."

        "Maybe":
            chartette "*She pouts* Atleast it's an maybe!"

    allen "Fine then. You guys have fun, I'll go serve the princess some tea."
    hide allenimage with dissolve
    chartette "Well.. There's not really much I can show you around here since Allen showed you the most."
    chartette "Hey, did you see outside?"
    mc "No, not rea-"
    "*Out of nowhere Mariam Phutapie came and whispered something into Chartette's ear and they both ran away*"
    show mariamimage at right with dissolve
    hide chartetteimage with dissolve
    hide mariamimage at right with dissolve
    mc "Well, that's them gone.."
    "*While walking around you find Allen running around*"
    scene hallwaycwest
    show allenimage with dissolve
    mc "Why are you running?"
    allen "I needed to serve Riliane but I'm late! I am so busy right now. Do you mind bringing her this?"
    "*Allen handed over a message to you*"
    mc "Yes, I will."
    allen "Great. Thank you"
    hide allenimage with dissolve
    "*He ran away*"
    mc "Well.. seems like he really is in a hurry.."
    "*You stared at the message*"

    menu:
        "Should I open this, look at the message, then close it?"

        "Open the message":
            $ opened_message = True
            
            "You open the letter. 'To Riliane, I am very sick and I can not proceed to serve you, Signed, Allen Avadonia'"

        "Leave it alone":
            "You decide not to open the letter."
    
    "You walk to Riliane's throne"
    scene rilianethroneroom
    show rilianeimage with dissolve
    riliane "Ohohoho! What do we have here?"
    mc "There's this message for you, from Allen."
    riliane "Guards? Let him through"
    "*The guards let you through*"
    mc "Here you go. *You bow*"
    "*You give her the message*"
    if opened_message:
        riliane "This looks open, Ah well."
    else:
        riliane "Hm, Good, Thank you."
    "*After Riliane reads it.*"
    riliane "Okay. Got it. Now leave."
    "*You quickly leave and go inform Allen in Hallway A*"
    scene hallwayanorth
    show allenimage with dissolve
    allen "So? Did you give her the message?"
    mc "Yes, I did"
    allen "Okay. Good."
    mc "Anything else?"
    allen "No, thank you."
    scene fountain
    mc "Hm.."
    "*You looked around and saw servants going around walking everywhere*"
    mc "What could they possibly be doing?"
    "*You looked to the right and saw Allen running towards you*"
    show allenimage with dissolve
    allen "Hey. I forgot to tell you, today is Riliane's birthday, Mariam will come any second now to give you a task, okay?"
    mc "Okay, got it."
    hide allenimage with dissolve
    "*Allen ran off*"
    "*After some time Mariam showed up*"
    show mariamimage with dissolve
    headmaid "Hey, you! Why are you doing nothing!?"
    mc "I was told that you would give me a duty."
    headmaid "Go help Allen and Chartette out! They are putting flowers! Go help them!"
    mc "I will."
    headmaid "But before you do that, what even is your name?"
    mc "It is [mc_name]"
    headmaid "[mc_name].. Okay then. Now go! Don't stay there and do nothing!"
    hide mariamimage with dissolve
    "*The headmaid left*"
    "*You go to Allen and Chartette who are in the garden picking out flowers*"
    scene flowers
    show allenimage at left with dissolve
    show chartetteimage at right with dissolve
    allen "Hey, you are gonna help us, right?"

    menu:
        "Yes":
            allen "Thank you. Let's get to work then"

        "No":
            chartette "Too bad, you will anyway!"
    
    chartette "Okay, so you do this and then that.."
    "*After learning and helping*"
    allen "Thanks for your help."
    chartette "Thank you too!"
    mc "So, what will I do now?"
    allen "Well, you can go to your room now if you want."
    chartette "Hey! What about me!?"
    allen "He's new, not you."
    chartette "Hmph!"
    "*You go back to your room*"
    scene roomtwozerofive
    mc "Ugh, what a long day.. I should go sleep now.."
    "*You go sleep after Riliane's birthday, you didn't see it cause only nobles were invited*"
    scene black
    "*You find yourself at the fountain*"
    scene fountain
    show allenimage at left with dissolve
    allen "Who are you?!"
    mc "I'm the new servant?"
    show rilianeimage at right with dissolve
    riliane "Who is this? A spy!?"
    mc "No!?"
    riliane "Guards? Is that [mc_name]? Take him away!"
    "*You suddenly get taken by the guards, you can't see the guards*"
    mc "Wait! What did I do? No!"
    scene black
    mc "AHH! What the!?"
    "*You open your eyes and see Allen and Chartette*"
    scene roomtwozerofive
    show allenimage at right with dissolve
    show chartetteimage at left with dissolve
    allen "Woah! You didn't need to scare us!"
    chartette "Yeah!"
    mc "Sorry.."
    allen "So Mariam sent us to see what's up with you, why didn't you wake up at 6AM?"
    mc "6AM?"
    chartette "Yeah! You slept till, what? 8AM?"
    allen "9AM."
    mc "Oops.."
    allen "Well, don't worry since your new I'll ignore it."
    chartette "Now you know!"
    hide allenimage with dissolve
    hide chartetteimage with dissolve
    "*After Allen and Chartette walked away you go to the headmaid's office for a duty*"
    scene headmaidsoffice
    "*You see the head maid and Chartette*"
    show chartetteimage at left with dissolve
    show mariamimage at right with dissolve
    headmaid "I can NOT have you messing around the palace!"
    chartette "Sorry..."
    headmaid "Now leave!"
    chartette "Will do, ma'am.."
    hide chartetteimage with dissolve
    headmaid "Now, what do you want?"
    mc "A duty, ma'am."
    headmaid "Go into the garden and organize the tables and stuff"
    mc "Yes ma'am will do."
    "*You leave and go to the garden*"
    scene fountain
    mc "Chairs.. Tables.."
    "*After a while*"
    scene fountainchairs
    show allenimage at right with dissolve
    allen "Woah, I am impressed by how well you did this."
    mc "Thank you!"
    show chartetteimage at left with dissolve
    chartette "Hehehe! Cool!"
    show servantsroomhallwaynearb
    show roomtwozerofive
    mc "Uuughh Today's been a looooong day.."
    "*You go to sleep*"


    return

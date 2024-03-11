for _ in range(100) :
    print("please select story \n 1 Hospital  2 weekend  3 letter  ")
    Templates = int(input(" write Number story: "))


    if  Templates == 1:
       print("you choosed Hospital")
       Number = int(input("please write number :"))
       Measure_of_time = str(input("Measure of time :"))
       Mode_of_Transportatino = str(input("Mode of Transportation :"))
       Adjective = str(input("write Adjective :"))
       Adjective2 =str(input("write Adjective2 :"))
       Noun =str(input("write noun :"))
       Color = str(input("write color :"))
       Part_of_time_Body = str(input("write Part of the Body :"))
       Verb = str(input("write verb:"))
       Number2 =int(input("write Number :"))
       Noun2 = str(input("write noun :"))
       Noun3 =str(input("write noun 3 :"))
       Part_of_time_Body2 =str(input("write part of time body :"))
       Verb2 = str((input("write verb :")))
       Noun4 = str(input("write noun : "))
       Adjective3 = str(input("write Adjective :"))
       Silly_Word =str(input("write Sillt word :"))
       Noun5 = str(input("write Noun :"))
       a =f""" It was about {Number} {Measure_of_time} ago when I arrived at the hospital in a {Mode_of_Transportatino}. The hospital is a/an {Adjective } place, there are a lot of { Adjective2 } {Noun} here. 
     There are nurses here who have {Color} {Part_of_time_Body }. If someone wants to come into my room I told them that they have to {Verb} first. Ive 
                decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their {Part_of_time_Body2}.1I heard that all 
                doctors {Verb2} {Noun4} every day for breakfast. The most {Adjective3} thing about being in the hospital is the {Silly_Word} {Noun5} !"""
       print(a)
    



    elif Templates == 2:
      print("you choosed weekend ! ")
      Persons_Name = str(input(f"write Persons Name:") )
      Noun = str(input("write Noun :"))
      Feeling = str(input("write feeling :"))
      Verb = str(input("write verb :"))
      Feeling2 =str(input("write Felling :"))
      Animal = str(input("write Animals :"))
      Verb2 = str(input("write verb :"))
      Color = str(input("write Color"))
      Verb_ing  = str(input("write Verb((ending in ing) ):"))
      Adverb_ly = str(input("Adverb (ending in ly) :"))
      Number = int(input("write Number :"))
      Measure_time = str(input("write  Measure of Time :"))
      Color2 =str(input("write color :"))
      Animal2  = str(input("write Animal :"))
      Number2 = int(input("write Number :"))
      Silly_Word = str(input("write Silly Word :"))
      Noun2  =  str(input("write Noun   :"))
      b = f""""This weekend I am going camping with ({Persons_Name}). I packed my lantern, sleeping bag, and ({Noun}). I am so ({Feeling}) to ({Verb}) in a tent. 
          I am  ({Feeling2}) we might see a(n) ({Animal}), I hear theyre kind of dangerous. While were camping, we are going to hike, fish, and ({Verb2}). I have heard that 
          the ({Color}) lake is great for (  ({Verb_ing} ). Then we will ({Adverb_ly}) hike through the forest for ({Number}) ({Measure_time}). If I see a ({Color2}) ({Animal2}) 
          while hiking, I am going to bring it home as a pet! At night we will tell ({Number2}) ({Silly_Word}) stories and roast ({Noun2}) around the campfire!!"""
      print(b)
    
    
    elif Templates == 3:
     print("you choosed letter ")
     Person_Name = str(input("write Perosan Name :"))
     Adjective =  str(input("write Adjective :")) 
     Color = str(input("write Color :"))
     Animal = str(input("write Animal :"))
     Place = str(input("write plase :"))
     Adjective2 = str(input("write Adjective :"))
     Magical_Creature = str(input("write Magical Creature (Plural) :"))
     Adjective3 = str(input("write Adjective :"))
     Magical_Creature2 = str(input("write Magical Creature (Plural) :"))
     Room_House = str(input("write Room in a House :"))
     Noun = str(input("write Noun :"))
     Noun2 = str(input("write Noun :"))
     Noun_Plural = str(input("write Noun(Plural) :"))
     Adjective4 = str(input("write Adjective :"))
     Noun_Plural2 = str(input(" write Noun(Plural) :"))
     Number = int(input("write Number  :"))
     Measure_of_time = str(input("write Measure of time :"))
     Verb_ing = str(input("write Verb (ending in ing) :"))
     Adjective5 = str(input("write Adjective :"))
     Noun5 = str(input("write Noun :"))

     c = f"""Dear ({Person_Name}), I am writing to you from a ({Adjective}) castle in an enchanted forest. I found myself here one day after going for a ride on a 
          ({Color}) ({Animal}) in ({Place}). There are ({Adjective2}) ({Magical_Creature}) and ({Adjective3}) ({Magical_Creature2}) here! In the ( {Room_House}) there is 
          a pool full of ({Noun}). I fall asleep each night on a ({Noun2}) of ({Noun_Plural}) and dream of ({Adjective4}) ( {Noun_Plural2}). It feels as though I have lived here for 
          ({Number}) ( {Measure_of_time}). I hope one day you can visit, although the only way to get here now is ({Verb_ing})) on a ({Adjective5}) ({Noun5})!!"""

     print(c)

    else :
     print("please select story \n 1 Hospital  2 weekend  3 letter :")
     Templates = int(input(" write Number story ! :  "))
   





















    




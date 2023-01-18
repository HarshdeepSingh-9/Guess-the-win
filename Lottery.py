minelist=[] # contians user input choice
luckynum=[] # contains generated number
matching=[] # contains matched digits
Draw=0 # initial game start at 0 
list_user_word_input=[]
genratedletter=[]
generatedcategory=[]
spin_the_wheel_choice=[]

def menu():#defining menu ---------------------------- 2
    print(
        '''
        This website is for the use of adults in the Province of Ontario, Canada. 
        Individuals must be 18 years of age or older to participate in lottery, 
        charitable gaming and in-store sports betting, in Ontario.  
        Individuals must be 19 years of age or older to visit casinos and slot facilities in Ontario, 
        and to participate in online casino gaming and online sports betting, in Ontario. 
        
        '''
    )
    print("ENTER THE NUMBER OF THE GAME ;")
    print("1- NINNING WUMBERS")
    print("2- SPIN THE WIN") 
    print("3- GAILY DRAND")
    collection={1:"NINNING WUMBERS",2: "MOTTO LAX",3:"GAILY DRAND"}
    z=int(input("Choose your type-"))
    if z == 1:
        NINNING_WUMBERS()# different function for different choice 
    if z== 2:
        SPIN_WIN()# choice 2 function
    if z== 3:
        GAILY_DRAND() # choice 3 function
        
def nin_wum(): # choice for nining wumbers ------------- 3A
    getstart=(input("choose your Draw - "))
    plm=int(getstart)
    global Draw
    Draw = plm 
    if plm == 0:
        menu()
    while getstart not in "4710":
        print("Enter Valid Choice")
        getstart=(input("choose your Draw - "))
    if getstart=="4":
        cb=4
        while cb!=0:
            chosenums=input("Enter Your Lucky Numbers -")
            while len(chosenums)!=1:
                print("Enter 1 Digit Number -")
                chosenums=input("Enter Your Lucky Numbers -")
            f_chosenums=int(chosenums)
            minelist.append(f_chosenums)
            cb=cb-1
    if getstart=="7":
        cb=7
        while cb!=0:
            chosenums=input("Enter Your Lucky Numbers -")
            while len(chosenums)!=1:
                print("Enter 1 Digit Number -")
                chosenums=input("Enter Your Lucky Numbers -")
            f_chosenums=int(chosenums)
            minelist.append(f_chosenums)
            cb=cb-1
    if getstart=="10":
        cb=10
        while cb!=0:
            chosenums=input("Enter Your Lucky Number -")
            while len(chosenums)!=1:
                print("Enter 1 Digit Number -")
                chosenums=input("Enter Your Lucky Numbers -")
            f_chosenums=int(chosenums)
            minelist.append(f_chosenums)
            cb=cb-1

        
        
    print("Numbers for $$$ are - ") 
    for i in minelist:
        print(i,end=" ")
    preprations()
    
def prizeMoney(): # RULE OF WINNING GAMES 
    print("-------Prize Money Rules-----")
    print(
        """
        When the main jackpot reaches $50 Million,
        we give you even more chances to dream! 
        To win a MAXMILLIONS draw, 
        CHECK BELOW RULES
        ----------------------------------->
        
        1 word matches - free next play 
        2 word matches - $100 (MOST COMMON)
        3 word matches - $500 (MOST COMMON)
        4 word matches - $1000 (FAIR)
        5 word matches - $10000
        6 word matches - $100000 
        7 word matches - $1000000 (FAIR)
        8 word matches - $10000000
        9 word matches - $100000000 (SO CLOSE)
        10 word matches - $1000000000 (JACKPOTTTTTTT)
       
       -------------------------------------->
        """
          )
        
def preprations():# CALLING OTHER INTERFACES ---------- 3B
    print("\n")
    print("Ready to Become a millionary or a Sportscar Rider-")
    z=input("Press L to see the luck --")
    if z =="L" or z=="l":
        prizeMoney()
        randomGenerator()
        matchedDigits()
    
def randomGenerator(): # number generator ------- 3C
    import random
    cho=[1,2,3,4,5,6,7,8,9,0]
    for i in range(Draw):
        sp=random.choice(cho)
        luckynum.append(sp)
    for j,k in enumerate(minelist):
        for p,l in enumerate(luckynum):
            if k==l:
                if j==p:
                    matching.append(k)
                else:
                    pass
            else:
                continue
    
def matchedDigits(): # checking the input digit with the generated digits 
    print("LIFE CHANGING DIGITS ARE -")
    print("\n")
    for i in luckynum:
        print(i,end=" ")
    print("\n")
    print("Your Chosen Numbers Are -")
    print("\n")
    for i in minelist:
        print(i,end=" ")
    print("\n")
    if len(matching)==0:
        print
        (
            '''Sorry at this Moment your Luck doesnt Supports ;
              You Can Try Again'''
        )
        zin=input("Wanna Try your Luck again ? Dont GIVE UP You can in the list of top millionaries---Y/N - ")
        if zin in "Yy":
            menu()
        else:
            print("Opps ! better luck Next time ---")
    else:
        print("Wow! Number of Matched Digits are - ",len(matching)) # displaying total matched number 
        print("SUPPPER DUPPER NUMBERSSS ARE - ","\n")
        for op in matching:
            print(op)
        print(
            '''-----CONGRATULATIONS CHAMP---'''
            ) 
        serialkey() # calling generated id to claim response
        print(
            '''
            Individuals or organizations with a qualifying website or mobile app can participate in this program.
            To claim Rewards Visit the Site --- olg.ca
            '''
            )
        
def serialkey(): # using random module completly because it is game of lottery that works with random picker -----------3D
    serialAlpha=["A","Q","W","X","S","G","H","E","N","C","L","Z"]
    serialNum=[1,6,3,9,0,2,4]
    import random
    gencodeY=[]
    for i in range(4):
        codekey=""
        gencodeX=[]
        for i in range(2):
            z=random.choice(serialAlpha)
            gencodeX.append(z)
        for i in range(2):
            z2=random.choice(serialNum)
            gencodeX.append(str(z2))
        random.shuffle(gencodeX)
        for pz in gencodeX:
            codekey+=pz
        gencodeY.append(codekey)
    print(
        '''
        USE THIS SERIAL ID TO CLAIM YOUR REWARD , DONOT SHARE THIS ....
        IT IS VALID TILL 12 HOURS FROM NOW 
        '''
        )
    for ps in range(len(gencodeY)):
        print(gencodeY[ps],end=" ")
        

def NINNING_WUMBERS(): # interface of ninning wumbers ------------------------------- 3
    print("WELCOME TO REBUILT YOUR FUTURE -")
    print("IN JUST 3 STEPS YOU WILL BE RIDING YOUR DREAM CAR .....ZUP")
    print(
    """
    STEP 1 , CHOOSE YOUR DRAW OF 4 , 7 OR 10 --------
    STEP 2 , CHOOSE YOUR NUMBERS AND HIT ENTER 
    STEP 3 , JUST CHILL
    TO REACH MENU YOU CAN PRESS 0
    """
    )
    nin_wum()
def gai_dra():
    genChoice=["A","B","G","M","C","T"]
    genCategory=["animal","country"]
    import random
    genratedletter.append(random.choice(genChoice))
    generatedcategory.append(random.choice(genCategory))
    print("---------WANNA SEE YOUR LUCKY LETTER---------")
    inL=input("PRESS L TO FULLFILL YOUR FOLDED CHAPTERS OF LIFE - / PRESS 0 TO REACH BACK TO THE MENU - ")
    if inL not in "Ll":
        menu()
    else:
        print("ONE IN A MILLION , TRILLION , BILLION ALPHABET IS - ", genratedletter[0].upper())
        print("ONE IN A MILLION , TRILLION , BILLION CATEGORY IS - ", generatedcategory[0].upper())
        choices_input_user()
         
    
def choices_input_user():
    print("\n","Now you may input 3 words begainning with GENERATED LETTER from GENERATED CATEGORY - ")
    x=3
    while x!=0:
        choice_from_user=input("Enter your word -")
        choice_into_list=choice_from_user+"\n"
        list_user_word_input.append(choice_into_list)
        x=x-1
    checking()
def checking():
    count=0
    if generatedcategory[0] == "animal":
        with open("LotteryWordsAnimals.txt","r") as pl :
            lc=pl.readlines()
            if list_user_word_input[0] in lc :
                    count+=1
            if list_user_word_input[1] in lc :
                    count+=1
            if list_user_word_input[2] in lc :
                    count+=1
    else:
        with open("LotteryWordsCountry.txt","r") as pl3 :
            op=pl3.readlines()
            if list_user_word_input[0] in op :
                    count+=1
            if list_user_word_input[1] in op  :
                    count+=1
            if list_user_word_input[2] in op :
                    count+=1
    if count == 3:
        print
        (
        """
        YUPPIEEEEEEE !!!! YOU MATCHED WITH THE HIGHEST IQ PERSON IN THE QUE , TRY YOUR LUCK AND EARN MONEY ----
        YOUR LUCK IS LUCKY WITH YOU THIS TIME , 
        DONT MISS OUT THIS AS THIS NEVER COME BACKKKKKKKKK !!!!!!!
        """
        )  
        
    else:
        print("Matched Words are - " , count)
        print
        (
        """
        UNFORTUNATELY , ITS NOT YOUR DAY TODAY , YOU DIDNT MATCHED ALL 
        """
        )

def SPIN_WIN():
    print("\nCHAMPIONS ALWAYS DIE HERE , BUT YOU ARE A LEGEND --")
    print("-SPIN THE LEVER TO MAKE YOUR DAY FULL OF STACKS TODAY -")
    print( 
    """
    -------------- !! READY !! ----------------
    STEP 1 , YOU ARE HAVING @ * $ ! AS SYMBOLS
    STEP 2 , AFTER YOU HIT SPIN THE LUCK , A FORTUNATE SEQUENCE OF SYMBOLS WILL APPEAR 
    STEP 3 , CHOOSE YOUR SPIN CHANCES --- 3 , 5 , 7
    STEP 4 , IF THE SEQUENCE MATCH THE REWARD RULES , YOU DEFINATELY GONNA CHANGE YOUR DAYS FROM TONIGHT
    STEP 5 , JUST RELAX AFTER HITTING L
    TO REACH MENU YOU CAN PRESS 0
    """
    )
    letgo_spin()
    
def letgo_spin():
    spin_choice=input("Enter Your Choice Y/N or 0 ")
    if spin_choice=="0":
        menu()
    if spin_choice=="Y" or spin_choice=="y":
        print("Ready to Roll Upp !!!!!! ")
        CHOICE_NUM_SPIN=input("Enter Your option , 3 , 5 , 7 ---> ")
        while CHOICE_NUM_SPIN not in "357":
            print("Enter Valid option -")
            CHOICE_NUM_SPIN=input("Enter Your option , 3 , 5 , 7 ----> ")
        runtine_number=int(CHOICE_NUM_SPIN)
        import random
        while runtine_number!=0:
            luckspin=input("PRESS L TO SPIN THE LUKCY VUKCY MUCKY LEVER-----")
            a=["@","*","$","!"]
            digits_in_spin=[]
            z=""
            for i in range(3):
                spining=random.choice(a)
                digits_in_spin.append(spining)
                z=z+spining
                z=z+"   "
            print(z)
            spin_the_wheel_choice.append(digits_in_spin)
            runtine_number=runtine_number-1
    if spin_choice=="N" or spin_choice=="n":
        choose()
        

               

def GAILY_DRAND():
    print("\n","WELCOME TO WORLD OF GRANDS , YOU ALSO WANT TO WIN SOME THICK STACKS ?")
    print("OFCOURSE YOU CAN BUY A HELICOPTER TO BUY GROCERIES !!!-")
    print(
    """
    RULE BOOK OF GAILY DRANDS
    STEP 1 , MAKE 3 WORDS WITH USING GENERATED ALPHABET 
    STEP 2 , USE GENERATED WORD AT THE BEGAINNING , USE UPPER CASE FOR 1 LETTER AND  LOWER CASE MODE FOR OTHER EG - <Tiger>
    STEP 4 , IT WILL SHOW UP A CATEGORY TO PICK WORDS FROM TO , AWARE OF THIS 
    STEP 3 , USE THE GENERATED WORD AT INDEX 0 OR START THE WORD FROM THE GENERATED ALPHABET 
    STEP 4 , JUST CHILL
    TO REACH MENU YOU CAN PRESS 0
    """
    )
    gai_dra()
    
def choose(): # starting interface ------------------- 1
    print("WELCOME TO THE LOTTERY PLACE")
    print("READY TO WIN $ 10000000000 !!???")
    a=input("Yes/No-")
    if a == "yes" or a =="Yes" or a=="y" or a =="Y":
        print("Lets go then !!")
        menu()
    else:
        print("Opps you loose the chance ! ")
        print("SomeOne else will be riding Mustang 🤡 ") 
 
choose()

    

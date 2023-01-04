minelist=[] # contians user input choice
luckynum=[] # contains generated number
matching=[] # contains matched digits
Draw=0 # initial game start at 0 


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
    print("1- NINNING WUMBERS")
    print("2- MOTTO LAX") 
    print("3- GAILY DRAND")
    collection={1:"NINNING WUMBERS",2: "MOTTO LAX",3:"GAILY DRAND"}
    z=int(input("Choose your type-"))
    if z == 1:
        NINNING_WUMBERS()# different function for different choice 
    if z== 2:
        MOTTO_LAX()# choice 2 function
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
        zin=input("Wanna Try your Luck agains ? Dont give You can in the list of top millionaries---Y/N")
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
    genChoice=["A","B","G","M","C","T","D","P"]
    
def Mywords():
    with open (LotteryWords.txt) as Lw:
        
    
def GAILY_DRAND():
    print("WELCOME TO WORLD OF GRANDS , YOU ALSO WANT TO WIN SOME THICK STACKS ?")
    print("OFCOURSE YOU CAN BUY A HELICOPTER TO BUY GROCERIES !!!-")
    print(
    """
    RULE BOOK OF GAILY DRANDS
    STEP 1 , MAKE 3 WORDS WITH USING GENERATED ALPHABET 
    STEP 2 , KEEP THE WORD LIMITED TO 5 LETTERS
    STEP 3 , USE GENERATED WORD ONLY ONCE 
    STEP 4 , USE THE GENERATED WORD AT INDEX 0 OR START THE WORD FROM THE GENERATED ALPHABET 
    STEP 5 , JUST CHILL
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

    
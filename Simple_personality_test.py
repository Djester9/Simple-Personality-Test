'''

personality game
questions:
1. which car would you prefer ? bently or ferrari - will tell me whether they
like to live fast or slow, flashy or modest 
2. Would you prefer a job through the city or a stroll along the beach ? 
fast or slow 
3. Wines with your friends in a high rise apartment or a campfire with marshmellow.
fast aor slow


'''

#create variables for fast and slow score


fast_score = 0
slow_score = 0

#print question

print("personality test")

print('would you prefer a 1. bently 2. ferrari ')
answer_0 = input("choose 1/2: " )

#If you make an answer which in favour of a fast life your' fast life_score will go up

if answer_0 == "1":
    slow_score = slow_score + 1 
elif answer_0 == "2":
    fast_score = fast_score + 1
else:
    print("input error")
    import sys
    sys.exit()


print("thanks for your answer, next question")

answer_1 = input("1. would you prefer a jog through the city or 2. a stroll along the beach 1/2:  ")

if answer_1 == "2":
    slow_score = slow_score + 1 
elif answer_1 == "1":
    fast_score = fast_score +1
else:
    print("input error")
    import sys
    sys.exit()


print("thanks for your answer next question")
answer_2 = input("1. wines with your friends in a high rise apartment or 2. a campfire with marshmellows 1/2:  " )

if answer_2 == "2":
    slow_score = slow_score + 1 
elif answer_2== "1":
    fast_score = fast_score + 1
    
elif answer_2.lower() == "easter egg":
    print("         (\ /)         ")
    print("        ( . .)         ")
    print("        C( )( )        ")
    import sys
    sys.exit()
elif answer_2.lower() == "easteregg":
    print("         (\ /)         ")
    print("        ( . .)         ")
    print("        C( )( )        ")
    import sys
    sys.exit()
else:
    print("input error")
    import sys
    sys.exit()
    

#final operation is checking to see if your fast score or slow score is higher

if fast_score < slow_score:
    print("      ")
    print ("you like to live relaxed and have fun ! rumour has it we can find you on a beach in thailand")
else:
    print("      ")
    print("you like to live the fast life. You are busy counting your money and dodging the traffic ; )  ")




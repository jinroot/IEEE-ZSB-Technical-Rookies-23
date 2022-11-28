import random

randNum = random.randint(100, 999)
hit=0
miss=0
randNum = str(randNum)

while(True):
    hit=0
    miss=0

    inp = input("enter your guess: ")
    for i in range(len(randNum)):
        if randNum[i] == inp[i]:
            hit += 1
        elif inp[i] in randNum:
            miss += 1
    if hit == 3:
        print("correct")
        break
    print(hit, "hit", miss, "miss")


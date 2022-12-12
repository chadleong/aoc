with open('input.txt') as f:
    data=f.readlines()
    f.close()

#A / X- Rock 1
#B / Y- Paper 2
#C / Z- Scissors 3

# win 6, lose 0, draw 3

#Example
# A Y - win - 6 2
# B X - lose - 0 1
# C Z - draw - 3 3

score=0

#Part 1
# for i in data:
#     if "B X" in i:
#         print("lose")
#         score+=1
#     elif "C Y" in i:
#         print("lose")
#         score+=2
#     elif "A Z" in i:
#         print("lose")
#         score+=3
#     elif "A Y" in i:
#         print("win")
#         score+=8
#     elif "B Z" in i:
#         print("win")
#         score+=9
#     elif "C X" in i:
#         print("win")
#         score+=7
#     elif "C Z" in i:
#         print("draw")
#         score+=6
#     elif "B Y" in i:
#         print("draw")
#         score+=5
#     elif ("A X") in i:
#         print("draw")
#         score+=4

#part 2
#X - lose
#Y - draw
#Z - win

#Example
#A - Rock 1
#B - Paper 2
#C - Scissors 3

# A Y - draw - 3 1
# B X - lose - 0 1
# C Z - win - 6 1

#A Rock 1, B Paper 2, C Scissors 3
for i in data:
    if "B X" in i:
        print("lose")
        score+=1
    elif "C Y" in i:
        print("draw")
        score+=6
    elif "A Z" in i:
        print("win")
        score+=8
    elif "A Y" in i:
        print("draw")
        score+=4
    elif "B Z" in i:
        print("win")
        score+=9
    elif "C X" in i:
        print("lose")
        score+=2
    elif "C Z" in i:
        print("win")
        score+=7
    elif "B Y" in i:
        print("draw")
        score+=5
    elif ("A X") in i:
        print("lose")
        score+=3


print(score)
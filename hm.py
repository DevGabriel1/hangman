import random

print("HEJ OCH VÄLKOMMEN TILL HÄNGA GUBBE!")
print("-----------------------------------")

answerlist = ["stefan" , "lazar" , "haris" ]

random.shuffle(answerlist)

answer = list(answerlist[0])

display = []

display.extend(answer)

for i in range (len(display)):
    display[i] = "_"

print(" ".join(display))
print()

count = 0

while count < len(answer):
    guess = input("gissa en bokstav: ")
    guess = guess.lower()
    print (count)

    for i in range (len(answer)):
        
        if answer[i] == guess :
            display[i] = guess
            count = count + 1

    print(' '.join(display))
    print()

print("Bra, du gissade rätt ord")
        




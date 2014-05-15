import random,time

s1 = ("- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n")
s2 = ("- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n")
s3 = ("- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n")
s4 = ("- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n")
s5 = ("- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n")
s6 = ("- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n")

def roll():
    print("rolling.....")
    roll = random.randint(1,6)


def show_dice():
    if roll == 1:
        print(S1)
    if roll == 2:
        print(s2)
    if roll == 3:
        print(s3)
    if roll == 4:
        print(s4)
    if roll == 5:
        print(s5)
    if roll == 6:
        print(s6)


roll()
time.sleep(1)
show_dice()


import numpy
import random
number_replace_list=[]
linesAndColumns=[line1,column1,line2,column2]= [0,0,0,0]
openedCardControl=0
while True:
    v_size=int(input("Vertical Size: "))
    h_size=int(input("Horizontal Size: "))
    if (v_size*h_size)%2!=0 or v_size*h_size>20:
        print("General size must be smaller than 20 or equal to 20 and an even number.")
        continue
    else:
        break
player_matrice=numpy.zeros((v_size,h_size),dtype=str)
for card_icon_i in range(len(player_matrice)):
    for card_icon_j in range(len(player_matrice[card_icon_i])):
        player_matrice[card_icon_i][card_icon_j]="█"

number_matrice=numpy.zeros((v_size,h_size))
for number in range(int((v_size*h_size)/2)):
    number_replace_list.append(number)
    number_replace_list.append(number)

for i in range(len(number_matrice)):
    for j in range(len(number_matrice[i])):
        number_matrice[i][j]=n=random.choice(number_replace_list)
        del number_replace_list[number_replace_list.index(n)]

def openCard1():
    global player_matrice
    while True:
        line=int(input("Enter the line: "))
        column=int(input("Enter the column: "))
        if len(player_matrice[0])<line-1 or len(player_matrice)<column-1 or player_matrice[line-1][column-1]!="█":
            print("Please enter appropriate column and line.")
        else:
            player_matrice[line-1][column-1]=number_matrice[line-1][column-1]
            print(player_matrice)
            print()
            linesAndColumns[0]=line-1
            linesAndColumns[1]=column-1
            return [line-1,column-1]

def openCard2():
    global player_matrice
    while True:
        line=int(input("Enter the line: "))
        column=int(input("Enter the column: "))
        if len(player_matrice[0])<line-1 or len(player_matrice)<column-1 or player_matrice[line-1][column-1]!="█":
            print("Please enter appropriate column and line.")
        else:
            player_matrice[line-1][column-1]=number_matrice[line-1][column-1]
            print(player_matrice)
            print()
            linesAndColumns[2]=line-1
            linesAndColumns[3]=column-1
            return [line-1,column-1]

def checkMatrice(openedCard1,openedCard2):
    global player_matrice
    global openedCardControl
    if openedCard1==openedCard2:
        openedCardControl+=2
        pass
    else:
        player_matrice[linesAndColumns[0]][linesAndColumns[1]]="█"
        player_matrice[linesAndColumns[2]][linesAndColumns[3]]="█"

def MatriceDesigner(player_matrice):
    for i in player_matrice:
        print("\n")
        for j in i:
            if j.isdigit():
                print(int(j),end="       ")
            else:
                print(j,end="       ")

def main():
    global linesAndColumns
    print(player_matrice)
    print()
    linesAndColumns[0],linesAndColumns[1]=openCard1()
    linesAndColumns[2],linesAndColumns[3]=openCard2()
    checkMatrice(player_matrice[linesAndColumns[0]][linesAndColumns[1]],player_matrice[linesAndColumns[2]][linesAndColumns[3]])
    if openedCardControl==v_size*h_size:
        print("Well done! You have found all of the cards.")
        quit()
    main()

main()
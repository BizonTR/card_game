import random
horizontal=1
vertical=1
empty_places_h=""
empty_places_v_and_h=""
empty_places_v_and_h_2=""
card_list=[]
number_list=[]
card_place_list=[]
card_place_list2=[]
card_1=""
card_2=""
card_place_list_after_check=[]
card_place_list_after_check_2=[]

def replace_cards():
    global empty_places_h
    global empty_places_v_and_h
    global horizontal
    global vertical
    global empty_places_v_and_h_2
    while horizontal*vertical%2!=0:
        print("Please enter horizontal and vertical sizes. But multiplication of both must be an even number and larger than 20 or equal to 20.")
        horizontal=int(input("Horizontal Size: "))
        vertical=int(input("Vertical Size: "))
        if not horizontal*vertical<=20:
            print("It have to be maximum 20 slots.")
    empty_places_h="█ "*horizontal
    empty_places_v_and_h=(f"\n{empty_places_h}\n"*vertical)
    empty_places_v_and_h_2=empty_places_v_and_h
    print(empty_places_v_and_h)

def replace_numbers():
    global number_list
    global card_list
    global horizontal
    global vertical
    global empty_places_h
    global empty_places_v_and_h
    card_list=[]
    for card in empty_places_v_and_h_2:
        card_list.append(card)
    place_lenght=0
    numbers_list=[]
    number_control=0
    for i in empty_places_v_and_h:
        if i=="█":
            place_lenght+=1
    while place_lenght!=len(numbers_list):
        for i in range(0,10):
            if place_lenght==len(numbers_list):
                break
            numbers_list.append(str(i))
            numbers_list.append(str(i))
            number_control+=1
    for card in card_list:
        if card=="█":
            index=card_list.index(card)
            random_number=random.choice(numbers_list)
            card_list[index]=random_number
            numbers_list.remove(random_number)
    print(card_list)
    print("".join(card_list))
    print(empty_places_v_and_h_2)

def card_places_list():
    global empty_places_v_and_h
    global card_place_list
    global card_place_list2
    for x in empty_places_v_and_h:
        card_place_list.append(x)

def enter_card_number_1():
    global card_1
    global empty_places_v_and_h_2
    global number_list
    global card_place_list
    global card_place_list_after_check
    card_ctrl=0
    card_index=0
    card_number_1=int(input("Enter Card Number: "))
    for card in card_place_list:
        if card=="█" or card in range(0,10):
            card_index=card_place_list.index(card)
            card_place_list.insert(card_index,"*")
            del card_place_list[card_index+1]
            card_ctrl+=1
            continue
        if card_ctrl==card_number_1:
            card_place_list.insert(card_index,card_list[card_index])
            card_1=card_list[card_index]
            del card_place_list[card_index+1]
            break
    card_place_list_after_check=""
    for star in card_place_list:
        if star=="*":
            star="█"
            card_place_list_after_check+=star
        else:
            card_place_list_after_check+=star
    print("".join(card_place_list_after_check))

def enter_card_number_2():
    global card_2
    global empty_places_v_and_h_2
    global number_list
    global card_place_list2
    global card_place_list_after_check
    global card_place_list_after_check_2
    card_ctrl=0
    card_index=0
    for x in card_place_list_after_check:
        card_place_list2.append(x)
    card_number_2=int(input("Enter Card Number: "))
    for card in card_place_list2:
        if card=="█" or card=="0" or card=="1" or card=="2" or card=="3":
            card_index=card_place_list2.index(card)
            card_place_list2.insert(card_index,"*")
            del card_place_list2[card_index+1]
            card_ctrl+=1
            continue
        if card_ctrl==card_number_2:
            card_place_list2.insert(card_index,card_list[card_index])
            card_2=card_list[card_index]
            del card_place_list2[card_index+1]
            break
    card_place_list_after_check_2=""
    for star in card_place_list2:
        if star=="*":
            star="█"
            card_place_list_after_check_2+=star
        else:
            card_place_list_after_check_2+=star
    print("".join(card_place_list_after_check_2))

replace_cards()
replace_numbers()
card_places_list()
enter_card_number_1()
enter_card_number_2()

#card 1 için seçilen card numarası > card 2 numarası olunca sorunsuz ama tam tersi olunca card 1 kapanıyor.
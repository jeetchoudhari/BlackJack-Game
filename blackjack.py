import random

#for A it can be 1 or 11 according to the condition(need to ask to user if they want 1 or 11)
#Add dictionary eg: for 3 it should show 3 for J it should display 10, for K it should display 10
#Select random nos from list of cards adn accordingly show their number

p_summ=0
c_summ=0
flag=0
cards_dict = {'A':1,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}
print("Welcome to BlackJack")
print("------------------------------------------------")

'''
print("TESTING------------------------------------------------")

random_key = random.choice(list(cards_dict.keys()))
print("Key: ", random_key)
random_value = cards_dict[random_key]
print("Value: ", random_value)


print("TESTING------------------------------------------------")
'''

for i in range(0,2):
    #random_number_computer = random.randint(1, 10)
    random_number_computer = random.choice(list(cards_dict.keys()))
    print("Card drawn by computer is: ", random_number_computer)
    random_computer_value = cards_dict[random_number_computer]
    c_summ = c_summ + random_computer_value
    print("\n")
print("After drawing two cards")
print("Computers total sum is ", c_summ)

for i in range(0,2):
    #random_number_player = random.randint(1, 10)
    random_number_player = random.choice(list(cards_dict.keys()))
    print("Card drawn by player is: ", random_number_player)
    random_player_value = cards_dict[random_number_player]
    p_summ = p_summ + random_player_value
    print("\n")
print("Players total sum is ", p_summ)

print("------------------------------------------------")
print("Player your turn")
if(p_summ==21):
    print("Player wins ")
else:
    player_input = input("Player : Enter draw to pick a card or stop to hold your sum:  ")
    if(player_input == 'draw'):
        flag=1
        while(flag==1):
            random_number_player = random.choice(list(cards_dict.keys()))
            print("Card drawn by player is: ", random_number_player)
            random_player_value = cards_dict[random_number_player]
            p_summ = p_summ + random_player_value
            print("Players total sum after drawing one more card is ", p_summ)
            if(p_summ>21):
                flag=3
                break
            if(p_summ==21):
                flag =4
                break
            player_input = input("Enter input:-> draw or stop:  ")
            if(player_input == 'stop' or p_summ >= 21):
                flag=0
                if(p_summ == c_summ and c_summ>16):
                    print(" -  -  -> Game tied <-  -  -  ")
    else:
        flag=0

if(flag==3):
    print("\n")
    print("Ooops!!  COMPUTER wins ")
elif(flag==4):
    print("\n")
    print("YAYYY!!! PLAYER wins :) ")
elif(flag==0):
    while(c_summ<17):
        random_number_computer = random.choice(list(cards_dict.keys()))
        print("Card drawn by computer is: ", random_number_player)
        random_computer_value = cards_dict[random_number_computer]
        c_summ = c_summ + random_computer_value
        print("Computers total sum after drawing one more card is ", c_summ)
        if(c_summ > p_summ and c_summ < 22):
            print("\n")
            print("Ooops!!  COMPUTER wins ")
        else:
            print("\n")
            print("YAYYY!!! PLAYER wins :) ")
            print("\n")


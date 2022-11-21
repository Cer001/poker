import random
#counts the number of rounds to rotate the dealer and play order
round_counter = 0

ante = 2
bet = ante
number_of_players = 3
betting_pot = ante * number_of_players

dealer = random.randint(1,number_of_players)

print(dealer)
player_1_dealer = False
player_2_dealer = False
player_3_dealer = False


if dealer == 1:
	player_1_dealer = True
elif dealer == 2:
	player_2_dealer = True
else:
	player_3_dealer = True

# assigns parameters to cards for the class function to use with poker weighting
values = list(range(2,15))

suits = ["clubs", "spades", "hearts", "diamonds"]

face_cards = {
	11: "Jack",
	12: "Queen",
	13: "King",
	14: "Ace"
}

weights_dict = {
	2: "2",
	3: "3",
	4: "4",
	5: "5",
	6: "6",
	7: "7",
	8: "8",
	9: "9",
	10: "10",
	11: "Jack",
	12: "Qeeen",
	13: "King",
	14: "Ace",
	"2": 2,
	"3": 3,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"10": 10,
	"Jack": 11,
	"Queen": 12,
	"King": 13,
	"Ace": 14
}

deck_list = []

# generates a deck of cards with mutually exclusive values, 52 cards total
class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

def generate_cards(values, suits):
	cards = []
	for value in values:
		for suit in suits:
			if value in face_cards:
				card_value = face_cards[value]
				cards.append(Card(card_value, suit))
			else:
				cards.append(Card(value, suit))
	return cards

# uses above class function to make cards in the format of 'type of card', 'suit'
cards = generate_cards(values, suits)

# makes a deck in form of a list
for card in cards:
	deck = ("{} of {}".format(card.value, card.suit))
	deck_list.append(deck)



card_1 = ""
card_2 = ""
card_3 = ""
card_4 = ""
card_5 = ""
card_6 = ""
card_7 = ""
card_8 = ""
card_9 = ""
card_10 = ""
card_11 = ""
card_12 = ""

# you are always player 1

player_1 = []
player_2 = []
player_3 = []
# public cards
flop = []
turn = ""
river = ""



# pops cards for the game and assigns them to player, the flop, river, etc. 
card_1 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_2 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_3 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_4 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_5 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_6 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_7 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_8 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_9 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_10 = deck_list.pop(random.randint(0,len(deck_list) - 1))
card_11 = deck_list.pop(random.randint(0,len(deck_list) - 1))

# stores the cards to each player in a list

player_1 = [str(card_1), str(card_2)]
player_2 = [str(card_3), str(card_4)]
player_3 = [str(card_5), str(card_6)]

# public cards
flop = [str(card_7), str(card_8), str(card_9)]
turn = str(card_10)
river = str(card_11)




# assigns numerical weights to the cards in the list for each player by referencing keys in the weights_dict dictionary
# recognizes the suit of each card for each player for later analysis

# player 1
for card in player_1[0]:
	card_splitter_list = player_1[0].split(" ")
	card_1_weight = weights_dict[card_splitter_list[0]]
	card_1_suit = card_splitter_list[2]

for card in player_1[1]:
	card_splitter_list = player_1[1].split(" ")
	card_2_weight = weights_dict[card_splitter_list[0]]
	card_2_suit = card_splitter_list[2]

# player 2
for card in player_2[0]:
	card_splitter_list = player_2[0].split(" ")
	card_3_weight = weights_dict[card_splitter_list[0]]
	card_3_suit = card_splitter_list[2]

for card in player_2[1]:
	card_splitter_list = player_2[1].split(" ")
	card_4_weight = weights_dict[card_splitter_list[0]]
	card_4_suit = card_splitter_list[2]

# player 3
for card in player_3[0]:
	card_splitter_list = player_2[0].split(" ")
	card_5_weight = weights_dict[card_splitter_list[0]]
	card_5_suit = card_splitter_list[2]

for card in player_3[1]:
	card_splitter_list = player_2[1].split(" ")
	card_6_weight = weights_dict[card_splitter_list[0]]
	card_6_suit = card_splitter_list[2]

# for public cards to be used in phases of the game
# flop
for card in flop[0]:
	card_splitter_list = flop[0].split(" ")
	card_7_weight = weights_dict[card_splitter_list[0]]
	card_7_suit = card_splitter_list[2]

for card in flop[1]:
	card_splitter_list = flop[1].split(" ")
	card_8_weight = weights_dict[card_splitter_list[0]]
	card_8_suit = card_splitter_list[2]

for card in flop[2]:
	card_splitter_list = flop[2].split(" ")
	card_9_weight = weights_dict[card_splitter_list[0]]
	card_9_suit = card_splitter_list[2]

# turn
for card in turn:
	card_splitter_list = turn.split(" ")
	card_10_weight = weights_dict[card_splitter_list[0]]
	card_10_suit = card_splitter_list[2]

# river
for card in river:
	card_splitter_list = river.split(" ")
	card_10_weight = weights_dict[card_splitter_list[0]]
	card_10_suit = card_splitter_list[2]



###########################


pre_flop_action_p1 = ""



##########
p1_hand_value = card_1_weight + card_2_weight
p2_hand_value = card_3_weight + card_4_weight
p3_hand_value = card_5_weight + card_6_weight



#check for suits
if card_1_suit == card_2_suit:
	p1_suited  = True
else:
	p1_suited = False

if card_3_suit == card_4_suit:
	p2_suited  = True
else:
	p2_suited = False

if card_5_suit == card_6_suit:
	p3_suited  = True
else:
	p3_suited = False

#check for pairs
if card_1_weight == card_2_weight:
	p1_pair = True
else:
	p1_pair = False

if card_3_weight == card_4_weight:
	p2_pair = True
else:
	p2_pair = False

if card_5_weight == card_6_weight:
	p3_pair = True
else:
	p3_pair = False

# checks for valid user input. if valid input, game proceeds
valid_user_input = True
while valid_user_input:
	print("________________________")
	print("Ante =  $", str(ante), "\n\n""Your hand: \n", player_1, "\n\ncheck/call (c) \nraise (r) \nfold (f)")
	pre_flop_action_p1 = input("\nYour turn...  ")
	if pre_flop_action_p1 != "c" and pre_flop_action_p1 != "r" and pre_flop_action_p1 != "f":
		print("________________________")
		print("!!!Try again: valid responses are c, r, or f")
	else:
		valid_user_input = False

# if fold, game ends
if pre_flop_action_p1 == "f":
	print("________________________")
	print("\nYou have quit the round.")
	round_counter += 1
	quit()


# if raise, game proceeds to ask how much the raise is
valid_raise = True
while valid_raise and pre_flop_action_p1 == "r":
	print("________________________")
	print("Raise by how much?  \n\nRecommended amounts:  $", str(ante * 2), ", $", str(ante * 4), ", $", str(ante * 8), 
		"\nOR\nEnter Custom Amount")
	flop_raise_p1 = int(input("Amount:  $"))
	round_counter += 1
	betting_pot += flop_raise_p1
	# checks whethe the raise is a number and only proceeds if user inputs valid int or float
	try:
		flop_raise_p1 = int(flop_raise_p1)
		break
	except:
		try:
			flop_raise_p1 = float(flop_raise_p1)
			break
		except:
			print("________________________")
			print("!!!Try again: valid responses are integers or floats ex. 1, 2, 1.2, 1.3, etc...")
	else:
		valid_raise = False









#def evaluate_hand(suited, paired, bet):
	#odds = bet / (bet + betting_pot)
	#if suited == True:


#define common cards are shared and that all players get hand value from them
def hands_r1(player):
	[player.append(card) for card in flop]
	return player

def hands_r2(player):
	[player.append(card) for card in turn]
	return player

def hands_r3(player):
	[player.append(card) for card in river]
	return player


#create functions to evaluate the hands strength in each round


def suited(player):
	card_suit = []
	i = 0
	for card in player:
		card_splitter_list = player[i].split(" ")
		card_suit.append(card_splitter_list[2])
		i += 1
	return card_suit

def pocket_suits_eval(player):
	if card_suit[0] == card_suit[1]:
		pocket_suits = True
	else:
		pocket_suits = False
	return pocket_suits

def pair_eval(player):
	i = 0
	pocket_pair = False
	for card in player:
		card_splitter_list = player[i].split(" ")
		card_weight = weights_dict[card_splitter_list[0]]
		pair = False
		i += 1
	if card_1 == card_2:
		pair = True


def hand_value(player):
	i = 0
	hand_value = 0
	for card in player:
		card_splitter_list = player[i].split(" ")
		card_weight = weights_dict[card_splitter_list[0]]
		hand_value += card_weight
		i += 1
	return hand_value



if pre_flop_action_p1 == "c":

	print(player_1)
	print(p1_hand_value)
	
	print(suited(player_1))
	print(hands_r1(player_1))
	print(hand_value(player_1))



#####################


############
#making the bot

if player_2_dealer == True:
	printpair_eval(player_2)
	pocket_suits_eval(player_2)
	hand_value(player_2)







































#for i, card in enumerate(deck_list, start = 1):
#	deck_dict = {i, card}
#print(deck_dict)

#print(random.randint(1,52))
#name = input("Enter your name: ")
#print("Hello there, {}!".format(name.title()))


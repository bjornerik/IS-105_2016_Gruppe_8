import collections
import itertools
import random

TYPE = ("Hjerter", "Spar", "Ruter", "Klover")
VERDI = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dronning", "Konge", "Ess")

class card:
    def __init__(self, numeral, suit):
        self.numeral = numeral
        self.suit = suit
        self.card = self.numeral, self.suit
    def __repr__(self):
        return self.numeral + "-" + self.suit

class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list
    def __repr__(self):
        short_desc = "Ingenting."
        numeral_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.numeral] += 1
            suit_dict[my_card.suit] += 1
        # Pair
        if len(numeral_dict) == 4:
            short_desc = "Et par."
        # Two pair or 3-of-a-kind
        elif len(numeral_dict) == 3:
            if 3 in numeral_dict.values():
                short_desc ="Tre like."
            else:
                short_desc ="To par."
        # Full house or 4-of-a-kind
        elif len(numeral_dict) == 2:
            if 2 in numeral_dict.values():
                short_desc ="Fult hus."
            else:
                short_desc ="Fire like."
        else:
            # Flushes and straights
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_numeral = min([VERDI.index(x) for x in numeral_dict.keys()])
            max_numeral = max([VERDI.index(x) for x in numeral_dict.keys()])
            if int(max_numeral) - int(min_numeral) == 4:
                straight = True
            # Ace can be low
            low_straight = set(("Ace", "2", "3", "4", "5"))
            if not set(numeral_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                short_desc ="Straight."
            elif flush and not straight:
                short_desc ="Flush."
            elif flush and  straight:
                short_desc ="Straight flush."
        enumeration = "/".join([str(x) for x in self.card_list])
        return "{enumeration} ({short_desc})".format(**locals())

class deck(set):
    def __init__(self):
        for numeral, suit in itertools.product(VERDI, TYPE):
            self.add(card(numeral, suit))
    def get_card(self):
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    def get_hand(self, number_of_cards=5):
        if number_of_cards == 5:
            return poker_hand([self.get_card() for x in range(number_of_cards)])
        else:
            raise NotImplementedError

for i in range(5):
    print(deck().get_hand())
import collections
import itertools
import random

TYPE = (u'\u0420\u043e\u0441\u0441\u0438\u044f', "Spar", "Ruter", "Klover")
VERDI = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dronning", "Konge", "Ess")

class card:
    def __init__(self, verdi, kortfarve):
        self.verdi = verdi
        self.kortfarve = kortfarve
        self.card = self.verdi, self.kortfarve
    def __repr__(self):
        return self.kortfarve + ' ' + self.verdi

class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list
    def __repr__(self):
        short_desc = "Ingenting."
        numeral_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.verdi] += 1
            suit_dict[my_card.kortfarve] += 1
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
                short_desc ="Hus."
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
        for verdi, kortfarve in itertools.product(VERDI, TYPE):
            self.add(card(verdi, kortfarve))
    def get_card(self):
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    def get_hand(self, number_of_cards=5):
        if number_of_cards == 5:
            return poker_hand([self.get_card() for x in range(number_of_cards)])
        else:
            raise NotImplementedError

for i in range(input("Hvor mange spillere skal delta?")):
    print(deck().get_hand())
    
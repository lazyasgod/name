import random
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 1,11
        else:
            return int(self.rank)

    def __str__(self):
        return self.rank + '-' + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
            random.shuffle(self.cards)

    def draw_card(self):
            if not self.cards:
                raise Exception("No more cards: empty deck!")
            card = self.cards.pop()
            return card

    def __str__(self):
            cards = []
            for c in self.cards:
                cards.append(str(c))
            return str(cards)

class Hand(Deck):
    def __init__(self, cards):
        self.cards = cards

    def add(self, card):
        self.cards.append(card)

    def value(self):
        total = 0
        num_aces = 0
        for card in self.cards:
            if card.rank == 'A':
                num_aces += 1
            else:
                total += card.value()

        total += num_aces
        if num_aces != 0 and total < 11:
            total += 10   

        return total

def test():
    deck = Deck()
    deck.shuffle()
    print ("Would you like to play?")
    answer = input("'yes' or 'no'")
    if answer == "yes":
          c1=deck.draw_card()
          c2=deck.draw_card()
          h = Hand([c1, c2])
          print (h)
          answer = input("Type either 'hit' or 'stay'")
          if answer == "hit":
                 c3=deck.draw_card()
                 h.add(c3)
                 print (h)
                 answer = input("Type either 'hit' or 'stay'")
                 if answer == "hit":
                    c4=deck.draw_card()
                    h.add(c4)
                    print (h)
                 else:
                    print ("let`s count")
          else:
              print ("let`s count")
          print(h.value())
          if h.value() > 21:
              print ("too much. you lost")
          else:
              print ("you win")
    else:
        print("you are disqusting")
         
                                
                                
                                
                                
          
                 
                 

test()


import random
import time
import datetime

#Todo
#Clean up, sort into functions  and make cleaner ways of doing somme things etc
#Allow dealer to do things maybe?
#Remove debug stuff
#Better naming for some things
#Commenting some things

class Game:
    dealer_deck = []
    player_deck = []

    player_score = 0
    dealer_score = 0

    dealer_hide = True
    
    def __init__ (self):
        #Comments starting with a * will prob be moved into func later
        #But for now this will do    

        #*Generate decks
        self.dealer_deck = Deck().generate_cards(2)
        print("dealer: ", self.dealer_deck)
        #time.sleep(0.1)
        self.player_deck = Deck().generate_cards(2)
        print("player: ", self.player_deck)

        #*Game happenings
        self.game_status()
        
        self.player_turn()

        self.dealer_hide = False

        self.game_status() 

        self.check_win()

    def game_status (self):
        self.calc_scores()
        self.show_dealer_cards()
        self.show_player_cards()

    def show_dealer_cards (self):
        print("Revealed Dealer cards:")
        if not self.dealer_hide:
            for dealer_card in self.dealer_deck:
                print(dealer_card.Type, dealer_card.Suit, end=" ")
        else:
            print(self.dealer_deck[0].Type, self.dealer_deck[0].Suit, end=" ") #Show first card
        #print(f"({self.dealer_score})") #Display score Debug 

    def show_player_cards (self):
        print("\nYour Cards:")
        for player_card in self.player_deck:
            print(player_card.Type, player_card.Suit, end=" ")
        print(f"({self.player_score})") #Display score

    
    def player_turn (self):
        while True:
            print("\nDo you want to Hit or Stand?")
            if input("(hit/Stand): ") == "hit":
                card = Deck().generate_cards(1)
                self.player_deck += card
                #print("You got card: ", card[0].Type, card[0].Suit) Debug
                self.game_status()
            else:
                break #I'm done taking cards

            for i, card in enumerate(self.player_deck):
                if card.Type == "A":
                    print("You have a A, set its value!")
                    if int(input("Value of A (1/11): ")) == 11:
                        self.player_deck[i].Value = 11

    def calc_scores (self):        
        self.calc_dealer_score()
        self.calc_player_score()

    def calc_dealer_score (self):
        for card in self.dealer_deck:
            self.dealer_score += card.Value
    def calc_player_score (self):
        self.player_score = 0 #reset
        for card in self.player_deck:
            self.player_score += card.Value

    def check_win(self):
        #Kinda messy way of doing this, but damn there are lots of things that needs checking
        #Will clean this up later
        if self.player_score <= 21 and self.player_score > self.dealer_score or self.dealer_score > 21 and self.player_score <= 21:
            print("You Win!")
        elif self.dealer_score <= 21 and self.dealer_score > self.player_score or self.player_score > 21 and self.dealer_score <= 21:
            print("Dealer Wins!")
        else:
            print("Draw")

class Deck:
    def generate_cards (self, amount):
        cards = []
        for _ in range(amount):
            cards.append(Card())
        return cards

class Card:
    Type: str
    Suit: str
    Value: int

    def __init__ (self):
        card_seed = random.randint(1,13) #There has to be a better name for this variable
        self.Type = self.set_card_type(card_seed)
        self.Value = self.set_card_init_value(card_seed)
        
        self.Suit = self.set_card_suit()

        #print("Created Card:", self.Type, self.Suit) #Debug

    def set_card_type(self, value):
        switcher = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }
        card_type = switcher.get(value, str(value))
        return card_type

    def set_card_suit(self):
        value = random.randint(1,4)
        switcher = {
            1: "♦",
            2: "♣️",
            3: "♥",
            4: "♠"
        }
        return switcher.get(value)

    def set_card_init_value(self, value):
        if value > 10:
            value = 10
        return value

    def set_display_type(self, value):
        switcher = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }
        return switcher.get(value, str(value))

game = Game()
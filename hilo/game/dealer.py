from game.user import User
import random


class Dealer:
    def __init__(self):
        self.c_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.p_card = 0
        self.c_card = random.choice(self.c_cards)
        self.c_point = 300

        # True is higher and False is lower
        self.higher = False

    def start_game(self):
        user01 = User()
        User.get_input(user01)
        pass

    def get_card(self):
        self.p_card = self.c_card
        self.c_card = random.choice(self.c_cards)

        if self.c_card > self.p_card:
            self.higher = True
        else:
            self.higher = False

    
    def get_point(self):

        if self.higher == User.guess:
            self.c_point += 100
        else:
            self.c_point -= 75
    

    def answer(self):

        pass

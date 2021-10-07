from game.user import User
import random


class Dealer:
    def __init__(self):
        self.c_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.p_card = 0
        self.c_card = random.choice(self.c_cards)
        self.c_point = 300
        self.user01 = User()
        # True is higher and False is lower
        self.higher = False

    def start_game(self):
        while self.user01.play_again:
            self.get_card()
            self.get_point()
            self.show_score()
            yesOrNo = input('Keep playing? [y/n]: ').lower()
            if yesOrNo == 'y':
                self.user01.play_again = True
            else:
                self.user01.play_again = False
        pass

    def get_card(self):
        self.p_card = self.c_card
        print(f'The card is: {self.p_card}')
        
        self.user01.get_input()
        self.c_card = random.choice(self.c_cards)
        print(f'The Next card: {self.c_card}')
        if self.c_card > self.p_card:
            self.higher = True
        else:
            self.higher = False

    
    def get_point(self):

        if self.higher == self.user01.guess:
            self.c_point += 100
        else:
            self.c_point -= 75
    

    def show_score(self):
        print(f'Your score is: {self.c_point}')
        pass

import random

class JowaGame:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.reject_count = 0

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def compliment(self, complimented, response):
        if complimented not in self.players:
            print(f"{complimented}는 게임에 없습니다.")
            return

        initiator = self.players[self.turn]
        print(f"{initiator} : {complimented} 좋아!")

        if response == "캌 퉤":
            print(f"{complimented} : {response} 😂")
            self.reject_count += 1
            if self.reject_count >= 3:
                print(f"{initiator}가 술을 마십니다! 🍻")
                return True
            
        else:
            print(f"{complimented} : 나도 좋아! 😊")
            self.reject_count = 0
            self.next_turn()

        return False
